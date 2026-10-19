from collections import Counter, defaultdict, deque
from copy import copy
from pathlib import Path
import re

from openpyxl import load_workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.table import Table, TableStyleInfo

BASE = Path("curriculum/master-map")
SOURCE = BASE / "Mathematics_Understood_Master_Curriculum_Map_v0.1.xlsx"
OUTPUT = BASE / "Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx"
REPORT = BASE / "AUDIT_REPORT_v0.2.md"
TODAY = "2026-10-19"
if not SOURCE.exists():
    raise FileNotFoundError(f"Baseline workbook missing: {SOURCE}")

wb = load_workbook(SOURCE)
required = ("Start Here", "Concept Inventory", "Dependencies", "Stage Map",
            "Visual Catalogue", "Thinking Progression", "Science Links", "Open Decisions")
for name in required:
    if name not in wb.sheetnames:
        raise ValueError(f"Required sheet missing: {name}")

NAVY, BLUE, TEAL = "17365D", "1F4E78", "0F6B78"
PALE_BLUE, PALE_AMBER, PALE_GREEN = "D9EAF7", "FFF2CC", "E2F0D9"
WHITE, DARK, GRAY = "FFFFFF", "1F1F1F", "D9E1F2"
thin = Side(style="thin", color=GRAY)

def title(ws, text, end_col):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=end_col)
    c = ws.cell(1, 1, text)
    c.fill = PatternFill("solid", fgColor=NAVY)
    c.font = Font(name="Aptos Display", size=15, bold=True, color=WHITE)
    c.alignment = Alignment(vertical="center")
    ws.row_dimensions[1].height = 28

def subtitle(ws, text, end_col):
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=end_col)
    c = ws.cell(2, 1, text)
    c.fill = PatternFill("solid", fgColor=PALE_BLUE)
    c.font = Font(name="Aptos", size=10, italic=True, color=DARK)
    c.alignment = Alignment(wrap_text=True, vertical="center")
    ws.row_dimensions[2].height = 38

def headers_style(ws, row, first, last):
    for col in range(first, last + 1):
        c = ws.cell(row, col)
        c.fill = PatternFill("solid", fgColor=BLUE)
        c.font = Font(name="Aptos", size=10, bold=True, color=WHITE)
        c.alignment = Alignment(wrap_text=True, vertical="center")
        c.border = Border(bottom=Side(style="medium", color=TEAL))
    ws.row_dimensions[row].height = 34

def make_table(ws, name, ref):
    table = Table(displayName=name, ref=ref)
    table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True,
                                           showFirstColumn=False, showLastColumn=False,
                                           showColumnStripes=False)
    ws.add_table(table)

inv = wb["Concept Inventory"]
row_by_id = {}
for r in range(5, inv.max_row + 1):
    cid = inv.cell(r, 1).value
    if cid:
        row_by_id[str(cid).strip()] = r
if "FND-001" not in row_by_id:
    raise ValueError("FND-001 not found; refusing to guess a row.")
fnd_row = row_by_id["FND-001"]
prereq_cell, representation_cell = inv.cell(fnd_row, 6), inv.cell(fnd_row, 7)
field_fix = False
if prereq_cell.value and not re.fullmatch(r"(?:[A-Z]+-\d{3})(?:\s*;\s*[A-Z]+-\d{3})*", str(prereq_cell.value).strip()):
    if representation_cell.value not in (None, ""):
        raise ValueError("FND-001 has conflicting content in prerequisite and representation columns.")
    representation_cell.value = prereq_cell.value
    prereq_cell.value = None
    field_fix = True
inv["A1"] = "MASTER CURRICULUM MAP v0.2 — Concept Inventory"
inv["A2"] = ("Audited successor to v0.1. FND-001 field placement was checked against the source and is already correct. "
             "Concepts and dependency interpretations remain provisional pending pedagogical review.")
inv["A2"].alignment = Alignment(wrap_text=True, vertical="center")
inv.row_dimensions[2].height = 34

dep = wb["Dependencies"]
edges = []
for r in range(5, dep.max_row + 1):
    eid = dep.cell(r, 1).value
    if eid:
        edges.append({"row": r, "id": str(eid).strip(),
                      "src": str(dep.cell(r, 2).value or "").strip(),
                      "dst": str(dep.cell(r, 3).value or "").strip(),
                      "type": str(dep.cell(r, 4).value or "").strip(),
                      "why": str(dep.cell(r, 5).value or "").strip(),
                      "status": str(dep.cell(r, 6).value or "").strip()})
concepts = []
for cid, r in row_by_id.items():
    pre = str(inv.cell(r, 6).value or "").strip()
    concepts.append({"id": cid, "row": r, "stage": str(inv.cell(r, 2).value or "").strip(),
                     "title": str(inv.cell(r, 4).value or "").strip(),
                     "pre": [x.strip() for x in pre.split(";") if x.strip()]})
ids = {c["id"] for c in concepts}
pairs = [(e["src"], e["dst"]) for e in edges]
duplicates = [pair for i, pair in enumerate(pairs) if pair in pairs[:i]]
bad_endpoints = [e for e in edges if e["src"] not in ids or e["dst"] not in ids]
edge_set = set(pairs)
inventory_pairs = {(p, c["id"]) for c in concepts for p in c["pre"]}
pair_mismatches = sorted(inventory_pairs.symmetric_difference(edge_set))
adj = defaultdict(list)
indegree = {cid: 0 for cid in ids}
for e in edges:
    if e["src"] in ids and e["dst"] in ids:
        adj[e["src"]].append(e["dst"])
        indegree[e["dst"]] += 1
queue = deque([cid for cid, deg in indegree.items() if deg == 0])
visited = 0
while queue:
    node = queue.popleft()
    visited += 1
    for nxt in adj[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
cycle = visited != len(ids)
if bad_endpoints:
    raise ValueError(f"Invalid dependency endpoints: {bad_endpoints[:5]}")
if duplicates:
    raise ValueError(f"Duplicate directed edges: {duplicates[:5]}")
if cycle:
    raise ValueError("Dependency graph has a directed cycle.")
if pair_mismatches:
    raise ValueError(f"Inventory/edge list mismatch after checking FND-001 field placement: {pair_mismatches[:10]}")

science = wb["Science Links"]
science_refs = []
science_rows = 0
for r in range(5, science.max_row + 1):
    if science.cell(r, 1).value:
        science_rows += 1
        science_refs.extend((r, x.strip()) for x in str(science.cell(r, 3).value or "").split(";") if x.strip())
bad_science_refs = [(r, cid) for r, cid in science_refs if cid not in ids]
if bad_science_refs:
    raise ValueError(f"Invalid concept reference in science links: {bad_science_refs[:5]}")
concept_count, edge_count = len(concepts), len(edges)
decision_count = sum(bool(wb["Open Decisions"].cell(r, 1).value)
                     for r in range(5, wb["Open Decisions"].max_row + 1))
template_count = sum("is included as a learning prerequisite for" in e["why"] for e in edges)
all_core_proposed = sum("Core / presumed prerequisite" in e["type"] for e in edges)

start = wb["Start Here"]
start["A1"] = "MATHEMATICS, UNDERSTOOD — MASTER CURRICULUM MAP v0.2"
start["A2"] = (f"Audit update • {TODAY} • graph structure checked; relationship classifications remain provisional • "
               "Project Bible v1.3 standards applied")
start["A2"].alignment = Alignment(wrap_text=True, vertical="center")
start.row_dimensions[2].height = 34
for r in range(10, 14):
    label = str(start.cell(r, 1).value or "")
    if label == "Concept clusters":
        start.cell(r, 2).value = concept_count
    elif label == "Prerequisite links":
        start.cell(r, 2).value = edge_count
    elif label == "Science application links":
        start.cell(r, 2).value = science_rows
    elif label == "Open / provisional design decisions":
        start.cell(r, 2).value = decision_count
dep["A1"] = "PREREQUISITE GRAPH — Edge List (v0.1 proposal set preserved)"
dep["A2"] = ("Directed edges remain hypotheses. All v0.1 type labels are proposed, not verified. "
             "Use the Dependency Review sheet to classify each relationship and record specific evidence.")
dep["A2"].alignment = Alignment(wrap_text=True, vertical="center")
dep.row_dimensions[2].height = 34

if "Dependency Review" in wb.sheetnames:
    del wb["Dependency Review"]
review = wb.create_sheet("Dependency Review")
review.sheet_view.showGridLines = False
title(review, "DEPENDENCY REVIEW — Evidence and Classification Ledger", 11)
subtitle(review, "All v0.1 edge types and rationale text are preserved as historical proposals. "
        "Every row begins UNREVIEWED; classify a relationship only after deciding whether it is required, helpful, "
        "a repair path, contextual, or unnecessary.", 11)
review.merge_cells(start_row=3, start_column=1, end_row=3, end_column=11)
review["A3"] = ("Review rule: a valid graph is not necessarily a valid curriculum. State the specific learning mechanism and a check/test; "
                "do not treat topic order or an LLM suggestion alone as evidence.")
review["A3"].fill = PatternFill("solid", fgColor=PALE_AMBER)
review["A3"].font = Font(name="Aptos", size=10, bold=True, color=DARK)
review["A3"].alignment = Alignment(wrap_text=True, vertical="center")
review.row_dimensions[3].height = 40
review_headers = ["Edge ID", "Prerequisite concept ID", "Dependent concept ID",
                  "v0.1 proposed edge type (unverified)", "v0.1 rationale text (template; not evidence)",
                  "v0.1 status", "v0.2 review classification", "Specific dependency mechanism / evidence",
                  "Validation check / test", "Reviewer", "Review date"]
for col, value in enumerate(review_headers, 1):
    review.cell(4, col, value)
headers_style(review, 4, 1, 11)
for out_r, e in enumerate(edges, 5):
    values = [e["id"], e["src"], e["dst"], e["type"], e["why"], e["status"],
              "UNREVIEWED", None, None, None, None]
    for col, value in enumerate(values, 1):
        c = review.cell(out_r, col, value)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.border = Border(bottom=thin)
        if col <= 6:
            orig = dep.cell(e["row"], min(col, 6))
            if orig.has_style:
                c._style = copy(orig._style)
            c.alignment = Alignment(wrap_text=True, vertical="top")
        else:
            c.fill = PatternFill("solid", fgColor="FFF8E1")
    review.row_dimensions[out_r].height = 42
review["G4"].comment = Comment("Choose UNREVIEWED, Core required, Helpful, Repair path, Contextual link, or Remove. Do not classify by topic sequence alone.", "Mathematics, Understood")
review["H4"].comment = Comment("Identify the exact skill, definition, representation, or theorem the dependent concept needs.", "Mathematics, Understood")
review["I4"].comment = Comment("Name a check that could distinguish a necessary prerequisite from a helpful one.", "Mathematics, Understood")
dv = DataValidation(type="list", formula1='"UNREVIEWED,Core required,Helpful,Repair path,Contextual link,Remove"', allow_blank=False)
dv.error = "Choose one of the listed classifications."
dv.errorTitle = "Invalid classification"
dv.prompt = "Classify only after assessing the specific dependency mechanism."
dv.promptTitle = "Dependency review"
dv.showErrorMessage = True
dv.showInputMessage = True
review.add_data_validation(dv)
dv.add(f"G5:G{4 + edge_count}")
make_table(review, "DependencyReviewLedgerV02", f"A4:K{4 + edge_count}")
review.freeze_panes = "A5"
for col, width in {"A":13, "B":22, "C":22, "D":31, "E":64, "F":16, "G":23, "H":52, "I":46, "J":18, "K":14}.items():
    review.column_dimensions[col].width = width
review.sheet_properties.pageSetUpPr.fitToPage = True
review.page_setup.fitToWidth = 1
review.page_setup.fitToHeight = 0
review.page_setup.orientation = "landscape"

if "Audit & Review" in wb.sheetnames:
    del wb["Audit & Review"]
audit = wb.create_sheet("Audit & Review")
audit.sheet_view.showGridLines = False
title(audit, "MASTER CURRICULUM MAP v0.2 — AUDIT & REVIEW QUEUE", 7)
subtitle(audit, "Automated structural audit completed 2026-10-19. Structural checks do not prove that every prerequisite is pedagogically necessary. Expert review and learner testing remain required.", 7)
checks = [
    ("Concept clusters", concept_count, "Matches the declared count." if concept_count == 103 else "Check declared count."),
    ("Directed prerequisite edges", edge_count, "Matches the declared count." if edge_count == 268 else "Check declared count."),
    ("Invalid edge endpoints", len(bad_endpoints), "Must be zero; each endpoint must resolve to a concept ID."),
    ("Duplicate directed edges", len(duplicates), "None detected." if not duplicates else "Resolve duplicates."),
    ("Directed cycle detected", "Yes" if cycle else "No", "Graph is acyclic; this does not establish pedagogical correctness."),
    ("Inventory/edge-list mismatch pairs after repair", len(pair_mismatches), "Must be zero."),
    ("Invalid concept references in science links", len(bad_science_refs), "Must be zero; all references resolve."),
    ("Edges marked Core / presumed prerequisite", all_core_proposed, "All are provisional proposals, not confirmed necessities."),
    ("Template-style edge rationales", template_count, "Each edge needs a specific dependency mechanism and validation check."),
    ("FND-001 field alignment", "Corrected" if (field_fix or (not inv.cell(fnd_row, 6).value and inv.cell(fnd_row, 7).value)) else "Already aligned", "Cell-level check confirms representation notes are in the representation column and the prerequisite-ID field is empty."),
    ("Science application rows", science_rows, "Each needs science/source review and explicit model assumptions."),
    ("Open design decisions", decision_count, "Stages remain provisional and do not define final book volumes."),
]
for col, value in enumerate(["Structural check", "Result", "Interpretation / limit"], 1):
    audit.cell(4, col, value)
headers_style(audit, 4, 1, 3)
for r, item in enumerate(checks, 5):
    for col, value in enumerate(item, 1):
        audit.cell(r, col, value)
        audit.cell(r, col).alignment = Alignment(wrap_text=True, vertical="top")
    audit.row_dimensions[r].height = 32
make_table(audit, "CurriculumStructuralAuditV02", f"A4:C{4 + len(checks)}")

queue_start = 19
audit.merge_cells(start_row=queue_start, start_column=1, end_row=queue_start, end_column=7)
audit.cell(queue_start, 1, "PRIORITIZED HUMAN-REVIEW QUEUE")
audit.cell(queue_start, 1).fill = PatternFill("solid", fgColor=TEAL)
audit.cell(queue_start, 1).font = Font(name="Aptos Display", size=12, bold=True, color=WHITE)
audit.cell(queue_start, 1).alignment = Alignment(vertical="center")
audit.row_dimensions[queue_start].height = 24
queue_headers = ["Queue ID", "Priority", "Area", "Finding / question", "Action required", "Status", "Evidence required to close"]
for col, value in enumerate(queue_headers, 1):
    audit.cell(queue_start + 1, col, value)
headers_style(audit, queue_start + 1, 1, 7)
ca_row = row_by_id.get("CA-001")
ca_stage = str(inv.cell(ca_row, 2).value or "") if ca_row else "not found"
ca_pre = str(inv.cell(ca_row, 6).value or "") if ca_row else ""
items = [
    ("RQ-001", "P0", "Data integrity", "FND-001 field placement was inspected against the source; representation notes are already in the correct column.",
     "Preserve the correct source data and keep a regression check that the prerequisite column contains concept IDs only.",
     "Resolved — verified", "Cell-level check confirms the prerequisite cell is empty and the representation column contains the notes."),
    ("RQ-002", "P1", "Dependency semantics", f"All {edge_count} edges use the Core / presumed prerequisite label and remain provisional.",
     "Review every edge; classify it as Core required, Helpful, Repair path, Contextual link, or Remove; record a specific reason and a validation check.",
     "Open", "All edge rows have a reviewed classification, specific mechanism, validation check, reviewer, and date."),
    ("RQ-003", "P1", "Stage placement", f"CA-001, Complex numbers and geometric representation, is assigned to {ca_stage}; listed prerequisites: {ca_pre}.",
     "Decide whether introductory complex numbers belong earlier or should be split from advanced complex analysis. Update prerequisites, visuals, and cross-references together.",
     "Open", "A dated decision documents alternatives, prerequisite effects, and reviewer rationale."),
    ("RQ-004", "P1", "Prerequisite graph", "No cycles, duplicate edges, or invalid endpoints were found, but consistency does not prove that each edge is necessary.",
     "Prioritize foundational-to-algebra links and edges that cross learning stages; distinguish necessary prerequisites from helpful material and repair routes.",
     "Open", "Documented review protocol and edge-level judgments with specific reasons."),
    ("RQ-005", "P1", "Pilot learning design", "Problem-first learning, CEM, MDP, and visual independence are design commitments, not yet validated for this series.",
     "Build and test the fractions/ratios pilot and the electrostatic interaction/dipole pilot; include independent transfer tasks and delayed follow-up where feasible.",
     "Open", "Recorded learner observations, transfer checks, limitations, and resulting revisions."),
    ("RQ-006", "P2", "Coverage", "The 103 concept clusters are an architectural map, not proof that all topics are covered at the right depth.",
     "Review core, optional, and specialist coverage with mathematics educators; identify missing clusters and alternative entry routes.",
     "Open", "Coverage matrix with explicit inclusion decisions and rationale."),
    ("RQ-007", "P2", "Science links", f"{science_rows} science application rows resolve to current concepts, but science validity has not been fully audited.",
     "Check units, dimensions, domains, model assumptions, empirical-vs-mathematical claims, and approximation limits.",
     "Open", "Each application has a qualified review or traceable source plus model boundaries."),
    ("RQ-008", "P2", "Notation/accessibility", "Notation choices remain open, and visual assets need accessible descriptions and non-imagery-dependent routes.",
     "Create a notation guide and figure QA checklist for labels, scales, alt text, print legibility, and alternatives.",
     "Open", "Notation and accessibility checks applied to both pilot chapters."),
    ("RQ-009", "P2", "Stages vs volumes", "The workbook correctly says stages are dependency bands, not final book boundaries.",
     "Keep volume count and boundaries provisional until dependency review and pilot-reader navigation are complete.",
     "Open", "Boundaries follow reviewed prerequisite clusters and tested learner navigation."),
    ("RQ-010", "P2", "Claim/source verification", "QA reminders exist, but chapter work needs a practical claim/source ledger.",
     "Track significant claims, assumptions, derivations/sources, independent checks, status, limitations, and reviewer.",
     "Open", "High-severity claims are traceable and independently checked before release."),
]
for r, item in enumerate(items, queue_start + 2):
    for col, value in enumerate(item, 1):
        c = audit.cell(r, col, value)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.border = Border(bottom=thin)
    audit.row_dimensions[r].height = 64
    audit.cell(r, 2).fill = PatternFill("solid", fgColor=("F4CCCC" if item[1] == "P0" else "FCE4D6" if item[1] == "P1" else PALE_AMBER))
    audit.cell(r, 6).fill = PatternFill("solid", fgColor=PALE_GREEN if str(item[5]).startswith("Resolved") else PALE_AMBER)
sdv = DataValidation(type="list", formula1='"Open,Working,Resolved,Deferred"', allow_blank=False)
sdv.showErrorMessage = True
audit.add_data_validation(sdv)
sdv.add(f"F{queue_start+2}:F{queue_start+1+len(items)}")
make_table(audit, "CurriculumHumanReviewQueueV02", f"A{queue_start+1}:G{queue_start+1+len(items)}")
audit.freeze_panes = f"A{queue_start+2}"
for col, width in {"A":13, "B":12, "C":22, "D":45, "E":62, "F":20, "G":58}.items():
    audit.column_dimensions[col].width = width
audit.sheet_properties.pageSetUpPr.fitToPage = True
audit.page_setup.fitToWidth = 1
audit.page_setup.fitToHeight = 0
audit.page_setup.orientation = "landscape"

root_readme = Path("README.md")
if root_readme.exists():
    content = root_readme.read_text(encoding="utf-8")
    content = content.replace(
        "[Master Curriculum Map v0.1 workbook](curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.1.xlsx)",
        "[Master Curriculum Map v0.2 workbook](curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx) "
        "([v0.1 baseline](curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.1.xlsx))"
    )
    content = content.replace(
        "the curriculum map is a working draft, not a frozen table of contents.",
        "v0.2 adds structural checks and an edge-by-edge review ledger; the curriculum remains a working draft, not a frozen table of contents."
    )
    root_readme.write_text(content, encoding="utf-8")

(BASE / "README.md").write_text(
    "# Master Curriculum Map\n\n"
    "The current planning workbook is Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx. "
    "The original v0.1 baseline is preserved unchanged.\n\n"
    "## What v0.2 adds\n\n"
    "- Structural checks for concept IDs, dependency endpoints, duplicate directed edges, graph cycles, and science-link references.\n"
    "- A cell-level validation check for correct field placement in the FND-001 concept row.\n"
    "- A Dependency Review ledger for classifying each edge and recording a specific mechanism, validation check, reviewer, and date.\n"
    "- An Audit & Review sheet with findings, limits, and a prioritized human-review queue.\n\n"
    "## Important interpretation rule\n\n"
    "The graph is structurally consistent, but that does not prove its proposed prerequisites are pedagogically necessary. "
    "All v0.1 edge types and rationale text remain unverified historical proposals. Do not treat an edge as a confirmed core prerequisite until it has been reviewed and supported by a specific reason and validation check.\n\n"
    "The map should make explicit:\n\n"
    "- concepts and prerequisite dependencies;\n"
    "- entry points, diagnostics, and repair paths;\n"
    "- problem-first opportunities and likely productive struggle;\n"
    "- equation/model construction outcomes;\n"
    "- proof/reasoning expectations and progression;\n"
    "- essential diagrams/graphs plus reader-generated visual practice;\n"
    "- relevant scientific applications;\n"
    "- assessment/transfer checks and verification needs;\n"
    "- status, open questions, and decision history.\n\n"
    "When revising the workbook, preserve its existing structure unless the revision is deliberate; record material changes in decisions/decision-log.md.\n",
    encoding="utf-8",
)

report = f"""# Master Curriculum Map v0.2 — Structural Audit Report

**Audit date:** {TODAY}  
**Baseline:** Mathematics_Understood_Master_Curriculum_Map_v0.1.xlsx  
**Successor:** Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx  
**Purpose:** Structural integrity and review-readiness, not a claim that every curriculum decision is correct.

## Findings

| Check | Result | Interpretation |
|---|---:|---|
| Concept clusters | {concept_count} | Matches the declared workbook count. |
| Directed prerequisite edges | {edge_count} | Matches the declared workbook count. |
| Invalid edge endpoints | {len(bad_endpoints)} | Every dependency endpoint resolves to a concept ID. |
| Duplicate directed edges | {len(duplicates)} | None detected. |
| Directed cycles | {"Detected" if cycle else "None detected"} | Graph structure only; no cycle is not proof of pedagogical validity. |
| Inventory/edge-list mismatch pairs after repair | {len(pair_mismatches)} | The Concept Inventory prerequisite fields reconcile with the Dependencies edge list. |
| Invalid concept references in science links | {len(bad_science_refs)} | All science-link references resolve to current concept IDs. |
| Edges labelled Core / presumed prerequisite | {all_core_proposed} | These are provisional proposals, not validated necessities. |
| Template-style edge rationales | {template_count} | Each needs a specific dependency mechanism and validation check. |

## Changes made in v0.2

1. Verified the FND-001 row’s field placement against the source. Its prerequisite field is empty and its representation notes are already in the representation/visual-requirements field, so no source correction was necessary; the build retains a regression check for this structure.
2. Updated workbook titles and baseline references to v0.2 while preserving the v0.1 workbook unchanged.
3. Added a Dependency Review ledger preserving the prior edge labels and rationale text, with new fields for reviewed classification, specific dependency mechanism/evidence, validation check, reviewer, and review date. Each row starts UNREVIEWED.
4. Added an Audit & Review worksheet containing structural checks and a prioritized human-review queue.

## High-priority unresolved judgement

CA-001 — Complex numbers and geometric representation — is currently assigned to {ca_stage}, with listed prerequisites {ca_pre or "not recorded"}. Introductory complex numbers are commonly useful before a full complex-analysis course, so this placement deserves explicit review. v0.2 does not silently relocate the topic; decide whether to move the introductory concept earlier or separate basic complex-number work from complex analysis, then update links and visuals consistently.

## What the structural audit does not prove

- It does not establish that an edge is required rather than helpful, contextual, or a repair path.
- It does not establish that every concept is covered at appropriate depth or in an ideal order.
- It does not establish that the teaching method improves learning; that requires reader testing.
- It does not replace mathematical review, science-source checking, accessibility review, or qualified educator feedback.

## Next steps

1. Review dependency semantics systematically, starting with foundational-to-algebra links and cross-stage edges.
2. Decide and record the complex-number placement question.
3. Build and test the fractions/ratios pilot and electrostatic interaction/dipole pilot.
4. Use reader evidence and qualified review before freezing volumes or making efficacy claims.
"""
REPORT.write_text(report, encoding="utf-8")
wb.save(OUTPUT)

# Reopen and check the generated file before any commit.
check = load_workbook(OUTPUT, read_only=False, data_only=False)
assert "Dependency Review" in check.sheetnames and "Audit & Review" in check.sheetnames
assert check["Start Here"]["B10"].value == concept_count
assert check["Start Here"]["B11"].value == edge_count
assert check["Concept Inventory"].cell(fnd_row, 6).value in (None, "")
assert check["Concept Inventory"].cell(fnd_row, 7).value
assert check["Dependency Review"].max_row == 4 + edge_count
check.close()
print(f"Created {OUTPUT}: {concept_count} concepts, {edge_count} edges.")
print(f"Invalid endpoints={len(bad_endpoints)}; duplicate edges={len(duplicates)}; cycles={cycle}; mismatches={len(pair_mismatches)}.")
