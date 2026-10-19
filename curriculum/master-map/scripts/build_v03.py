from collections import Counter, defaultdict, deque
from copy import copy
from pathlib import Path
import re
import json

from openpyxl import load_workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.table import Table, TableStyleInfo

BASE = Path("curriculum/master-map")
SOURCE = BASE / "Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx"
OUTPUT = BASE / "Mathematics_Understood_Master_Curriculum_Map_v0.3.xlsx"
REPORT = BASE / "AUDIT_REPORT_v0.3.md"
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


# Apply the D-11 complex-number scope split to a new v0.3 successor.
# The v0.2 source remains untouched. This is a provisional implementation awaiting educator review.
concept_ws = wb["Concept Inventory"]
def _locate_row(ws, id_col, target, start=5):
    for rr in range(start, ws.max_row + 1):
        if str(ws.cell(rr, id_col).value or "").strip() == target:
            return rr
    return None

ca001_row_pre = _locate_row(concept_ws, 1, "CA-001")
ca002_row_pre = _locate_row(concept_ws, 1, "CA-002")
ca003_row_pre = _locate_row(concept_ws, 1, "CA-003")
if ca001_row_pre is None or ca002_row_pre is None:
    raise ValueError("Expected CA-001 and CA-002 concept rows were not found.")
if ca003_row_pre is not None:
    raise ValueError("CA-003 already exists in the v0.2 baseline; stop rather than duplicate it.")
if str(concept_ws.cell(ca001_row_pre, 4).value).strip() != "Complex numbers and geometric representation":
    raise ValueError("CA-001 title differs from the inspected v0.2 baseline; review the patch before proceeding.")
if str(concept_ws.cell(ca002_row_pre, 4).value).strip() != "Complex functions and complex differentiation":
    raise ValueError("CA-002 title differs from the inspected v0.2 baseline; review the patch before proceeding.")

ca001_values = {
    2: "1 — Algebra & functions",
    3: "Complex numbers",
    4: "Complex numbers: algebraic meaning and operations",
    5: "Interpret the imaginary unit i; express numbers in a + bi form; identify real and imaginary parts; add, subtract and multiply complex numbers; divide by a nonzero complex number using conjugates; verify basic identities.",
    6: "FND-015;ALG-002",
    7: "Paired real/imaginary components; a + bi cards; component-wise addition and multiplication; conjugate/product examples; optional point representation as a bridge to Stage 2. Do not require polar form here.",
    8: "Construct a complex expression from real and imaginary parts; carry out operations and verify by component-wise expansion.",
    9: "Justify basic operations using i² = −1; verify conjugate identities by expansion; distinguish worked examples from general identities.",
    10: "Quadratic equations and non-real roots (contextual extension); complex plane and polar form; complex analysis; signals/phasors; quantum mechanics.",
    11: "Oscillations, phasors, quantum mechanics.",
    12: "Keep rectangular algebra separate from polar form; state that the divisor is nonzero for division; introduce i² = −1 explicitly and locally.",
    13: "Provisional — v0.3 scope split; educator review pending"
}
for col, value in ca001_values.items():
    concept_ws.cell(ca001_row_pre, col, value)

ca002_values = {
    5: "Analyze complex-valued functions and complex differentiability; explain why complex differentiability imposes strong constraints; use geometric/polar interpretations where useful.",
    6: "CA-001;CAL-004;ADV-001",
    7: "Domain/color plots, mapped grids, contour sketches; use polar views when they serve the chosen theorem or application.",
    10: "Advanced analysis, contour integration, applied transforms; complex-plane/polar representation is a useful connection rather than a universal entry gate.",
    12: "Visualizations need a key and scale; state domain, differentiability assumptions, and connectedness conditions where relevant.",
    13: "Provisional — v0.3 scope split; educator review pending"
}
for col, value in ca002_values.items():
    concept_ws.cell(ca002_row_pre, col, value)

# Add a distinct Stage 2 cluster so polar/geometric prerequisites do not delay algebraic complex arithmetic.
concept_rows = [rr for rr in range(5, concept_ws.max_row + 1) if concept_ws.cell(rr, 1).value]
last_concept_row = max(concept_rows)
new_concept_row = last_concept_row + 1
for col in range(1, 14):
    source_cell = concept_ws.cell(last_concept_row, col)
    dest_cell = concept_ws.cell(new_concept_row, col)
    if source_cell.has_style:
        dest_cell._style = copy(source_cell._style)
    if source_cell.number_format:
        dest_cell.number_format = source_cell.number_format
    if source_cell.alignment:
        dest_cell.alignment = copy(source_cell.alignment)
    if source_cell.protection:
        dest_cell.protection = copy(source_cell.protection)
ca003_values = [
    "CA-003",
    "2 — Geometry, trig & spatial",
    "Complex numbers / coordinate geometry",
    "Complex plane, modulus/argument and polar form",
    "Represent z = a + bi as a point/vector in the complex plane; calculate its modulus and argument; convert between rectangular and polar forms; interpret multiplication as rotation/scaling; use polar form for powers and roots with explicit argument conventions.",
    "CA-001;ALG-006;GEO-005;TRI-002",
    "Complex plane with real/imaginary axes; vectors from the origin; right-triangle modulus; argument angle; unit-circle and radians cues; rectangular/polar overlays; worked rotation/scaling examples; branch/argument callouts.",
    "Construct a complex-plane or polar representation from components, magnitude/angle, or a rotation context; state angle units and the argument convention.",
    "Derive rectangular/polar conversion from coordinates and trigonometry; justify the modulus formula and multiplication-as-rotation/scaling; identify argument non-uniqueness.",
    "Complex analysis; eigenvalues; differential equations; oscillation/phasors; quantum mechanics.",
    "Oscillations, phasors, quantum mechanics.",
    "Label axes, units and angle conventions; state that arg(z) is undefined at z = 0 and that arguments differ by multiples of 2π; separate algebraic fluency from polar-geometry fluency.",
    "Provisional — v0.3 scope split; educator review pending"
]
for col, value in enumerate(ca003_values, 1):
    concept_ws.cell(new_concept_row, col, value)
concept_ws.row_dimensions[new_concept_row].height = 62
for table in concept_ws.tables.values():
    if table.ref.startswith("A4:M"):
        table.ref = f"A4:M{new_concept_row}"

# Revise the affected edge set by stable ID, preserving unchanged links and adding new IDs only.
dep_ws = wb["Dependencies"]
edge_row_by_id = {}
for rr in range(5, dep_ws.max_row + 1):
    edge_id = str(dep_ws.cell(rr, 1).value or "").strip()
    if edge_id:
        edge_row_by_id[edge_id] = rr
def _set_edge(edge_id, source_id, target_id, edge_type, rationale, status="Provisional"):
    rr = edge_row_by_id.get(edge_id)
    if rr is None:
        raise ValueError(f"Required baseline edge missing: {edge_id}")
    for col, value in enumerate([edge_id, source_id, target_id, edge_type, rationale, status], 1):
        dep_ws.cell(rr, col, value)

_set_edge("EDGE-255", "FND-015", "CA-001", "Core / presumed prerequisite",
          "Signed/rational real-component arithmetic supports the full basic complex-arithmetic outcome; offer a short local arithmetic bridge when needed.")
_set_edge("EDGE-256", "FND-014", "CA-001", "Helpful / just-in-time link",
          "The identity i² = −1 uses integer-exponent notation, but it can be introduced inside the first complex-number lesson; full exponent-strand mastery is not an entry gate.")
_set_edge("EDGE-257", "ALG-002", "CA-001", "Core / presumed prerequisite",
          "Expression reading and equivalence support expansion and simplification of a + bi operations and conjugate identities; refresh the minimum locally if needed.")
_set_edge("EDGE-258", "TRI-002", "CA-003", "Core / presumed prerequisite",
          "The full polar-form outcome needs unit-circle/trigonometric relationships for angle, quadrant, and rectangular-to-polar conversion.")
_set_edge("EDGE-259", "CA-001", "CA-002", "Core / presumed prerequisite",
          "Complex functions and differentiation operate on complex inputs/outputs; basic complex-number meaning and arithmetic are foundational.")
_set_edge("EDGE-260", "CAL-004", "CA-002", "Core / presumed prerequisite",
          "The mapped complex-differentiation outcome uses derivative language and rule fluency; a limit-based bridge is available for learners who need it.")
_set_edge("EDGE-261", "ADV-001", "CA-002", "Core / presumed prerequisite",
          "The advanced complex-analysis outcome requires proof-based work with definitions, assumptions, lemmas, and conditions.")

last_edge_row = max(edge_row_by_id.values())
if any(f"EDGE-{n:03d}" in edge_row_by_id for n in range(269, 274)):
    raise ValueError("One or more v0.3 edge IDs already exist; reconcile instead of duplicating.")
new_edges = [
    ("EDGE-269", "ALG-014", "CA-001", "Contextual link (non-prerequisite)",
     "Quadratics motivate non-real roots and the usefulness of complex numbers, but that application is not required to learn basic complex arithmetic.", "Provisional"),
    ("EDGE-270", "ALG-006", "CA-003", "Core / presumed prerequisite",
     "Ordered pairs, axes, and coordinate conventions support representing a + bi as a point with real and imaginary coordinates.", "Provisional"),
    ("EDGE-271", "GEO-005", "CA-003", "Core / presumed prerequisite",
     "The modulus is the distance from the origin and uses the Pythagorean theorem for the full geometric/polar outcome.", "Provisional"),
    ("EDGE-272", "CA-001", "CA-003", "Core / presumed prerequisite",
     "The geometric/polar cluster builds on algebraic complex-number meaning and operations, then links them to coordinate and transformation interpretations.", "Provisional"),
    ("EDGE-273", "CA-003", "CA-002", "Helpful / enrichment link",
     "Polar/geometric interpretation is valuable in complex analysis but is not a universal prerequisite for defining complex differentiability or starting with a difference quotient.", "Provisional")
]
for edge_id, source_id, target_id, edge_type, rationale, status in new_edges:
    rr = last_edge_row + 1
    last_edge_row = rr
    for col, value in enumerate([edge_id, source_id, target_id, edge_type, rationale, status], 1):
        c = dep_ws.cell(rr, col, value)
        prev = dep_ws.cell(rr - 1, col)
        if prev.has_style:
            c._style = copy(prev._style)
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.border = Border(bottom=thin)
    dep_ws.row_dimensions[rr].height = 48
    edge_row_by_id[edge_id] = rr
for table in dep_ws.tables.values():
    if table.ref.startswith("A4:F"):
        table.ref = f"A4:F{last_edge_row}"

# Update stage-level coverage to match the new, distinct learning milestones.
stage_ws = wb["Stage Map"]
stage_rows_by_name = {str(stage_ws.cell(rr, 1).value or "").strip(): rr
                      for rr in range(5, stage_ws.max_row + 1)
                      if stage_ws.cell(rr, 1).value}
stage1_row = stage_rows_by_name.get("1 — Algebra & functions")
stage2_row = stage_rows_by_name.get("2 — Geometry, trig & spatial")
if stage1_row is None or stage2_row is None:
    raise ValueError("Expected Stage 1 and Stage 2 rows were not found.")
stage_ws.cell(stage1_row, 3, "Variables, expressions, equations, inequalities, coordinate plane, graph literacy, linear/nonlinear functions, systems, sequences, and algebraic complex numbers in rectangular form.")
stage_ws.cell(stage1_row, 4, "Construct equations/functions from situations; interpret/create graphs; choose solving strategies; perform basic complex arithmetic in a + bi form.")
stage_ws.cell(stage1_row, 5, "Balance models, tables, coordinate graphs, transformation overlays, domain/range sketches; paired real/imaginary components and conjugate examples.")
stage_ws.cell(stage1_row, 7, "Elementary complex arithmetic follows the minimum required expression/arithmetic skills. Polar form and modulus/argument wait until the geometry/trigonometry stage.")
stage_ws.cell(stage2_row, 3, "Geometric definitions, polygons, area/volume, similarity, Pythagorean theorem, circles, vectors, trigonometry, and complex-plane/polar representation.")
stage_ws.cell(stage2_row, 4, "Translate diagrams to statements; formulate geometric relations/periodic models; interpret complex modulus, argument, polar form, and multiplication as rotation/scaling.")
stage_ws.cell(stage2_row, 5, "Accurate labelled diagrams, constructions, scale models, vector arrows, unit-circle/function graphs, and complex-plane/polar overlays.")
stage_ws.cell(stage2_row, 7, "Sequence polar complex numbers after algebraic complex numbers, coordinate geometry, distance reasoning, and the unit circle. Keep complex analysis in Stage 6.")
for rr in (stage1_row, stage2_row):
    for col in range(1, 8):
        stage_ws.cell(rr, col).alignment = Alignment(wrap_text=True, vertical="top")
    stage_ws.row_dimensions[rr].height = 80

# Split the one visual family into distinct algebraic and geometric/polar visual requirements.
visual_ws = wb["Visual Catalogue"]
v15_row = _locate_row(visual_ws, 1, "V-15")
if v15_row is None:
    raise ValueError("Expected Visual Catalogue entry V-15 was not found.")
v15 = [
    "V-15",
    "Elementary complex numbers / algebra",
    "CA-001",
    "Make the real/imaginary parts and algebraic operations in a + bi form legible; connect symbolic operations to component-wise reasoning.",
    "Paired-component cards; color-neutral real/imaginary alignment; expansion and conjugate examples; optional coordinate point as a bridge.",
    "Translate between verbal description and a + bi; expand products; predict and verify conjugate identities; separate arithmetic from representation errors.",
    "Keep signs and i² = −1 explicit; avoid color-only encoding; show complete algebraic steps; do not imply polar form is required at this stage."
]
for col, value in enumerate(v15, 1):
    visual_ws.cell(v15_row, col, value)
v16_row = _locate_row(visual_ws, 1, "V-17")
if v16_row is not None:
    raise ValueError("V-17 already exists in the v0.2 baseline; check before adding.")
visual_rows = [rr for rr in range(5, visual_ws.max_row + 1) if visual_ws.cell(rr, 1).value]
last_visual_row = max(visual_rows)
v16_row = last_visual_row + 1
for col in range(1, 8):
    src = visual_ws.cell(last_visual_row, col)
    dst = visual_ws.cell(v16_row, col)
    if src.has_style:
        dst._style = copy(src._style)
    if src.alignment:
        dst.alignment = copy(src.alignment)
v16 = [
    "V-17",
    "Complex plane, modulus/argument and polar form",
    "CA-001;CA-003;ALG-006;GEO-005;TRI-002",
    "Connect the algebraic number a + bi to coordinates, distance from the origin, direction, polar representation, and multiplication as rotation/scaling.",
    "Complex plane with labelled axes; vectors and right triangles for modulus; angle/radian callouts; rectangular/polar conversions; rotation/scaling overlays; examples showing argument non-uniqueness.",
    "Plot and reconstruct a + bi; calculate modulus/argument; convert forms; predict products geometrically and verify algebraically; identify when argument conventions matter.",
    "Label real/imaginary axes, scale, units and angle convention; note arg(z) is undefined at zero and arguments differ by multiples of 2π; include text descriptions and print-legible labels."
]
for col, value in enumerate(v16, 1):
    visual_ws.cell(v16_row, col, value)
visual_ws.row_dimensions[v16_row].height = 62
for rr in range(5, v16_row + 1):
    for col in range(1, 8):
        visual_ws.cell(rr, col).alignment = Alignment(wrap_text=True, vertical="top")
for table in visual_ws.tables.values():
    if table.ref.startswith("A4:G"):
        table.ref = f"A4:G{v16_row}"

# D-11 is implemented as a proposal in v0.3 but remains open pending educator review.
decisions_ws = wb["Open Decisions"]
d11_row = _locate_row(decisions_ws, 1, "D-11")
if d11_row is None:
    raise ValueError("D-11 was not found in the Open Decisions register.")
decisions_ws.cell(d11_row, 4, "v0.3 provisional patch applied: CA-001 is algebraic complex numbers in Stage 1; CA-003 is complex-plane/polar work in Stage 2; CA-002 complex analysis remains in Stage 6.")
decisions_ws.cell(d11_row, 5, "Review OpenStax elementary/polar-form sequencing; check all prerequisite endpoints, the directed graph, inventory/edge alignment, and learner entry routes; obtain mathematics-educator feedback before treating the split as final.")
decisions_ws.cell(d11_row, 6, "Proposed implementation — educator review pending")
decisions_ws.cell(d11_row, 7, "After mathematics-educator review and pilot-reader checks; before freezing stages or publication volumes.")
for col in range(1, 8):
    decisions_ws.cell(d11_row, col).alignment = Alignment(wrap_text=True, vertical="top")
decisions_ws.row_dimensions[d11_row].height = 86
for table in decisions_ws.tables.values():
    if table.ref.startswith("A4:G"):
        table.ref = f"A4:G{max(int(table.ref.split(':')[1][1:]), decisions_ws.max_row)}"

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
inv["A1"] = "MASTER CURRICULUM MAP v0.3 — Concept Inventory"
inv["A2"] = ("v0.3 successor to v0.2. Complex-number outcomes are split provisionally across Stages 1, 2 and 6; educator review remains pending. "
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
edge_set = {(e["src"], e["dst"]) for e in edges if e["type"] == "Core / presumed prerequisite"}
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

# Keep the complex-number scope question visible in the workbook's open-decision register.
open_decisions_ws = wb["Open Decisions"]
existing_decision_ids = {
    str(open_decisions_ws.cell(r, 1).value).strip()
    for r in range(5, open_decisions_ws.max_row + 1)
    if open_decisions_ws.cell(r, 1).value
}
if "D-11" not in existing_decision_ids:
    decision_row = max(open_decisions_ws.max_row + 1, 15)
    decision_values = [
        "D-11",
        "Complex-number scope and stage split",
        "Elementary algebraic complex numbers, polar/geometric representation, and complex analysis use different prerequisite sets; one combined cluster may delay introductory content or force trigonometry too early.",
        "Open proposal: re-scope CA-001 as algebraic complex numbers in Stage 1; create CA-003 for complex plane/polar/geometric representation in Stage 2; keep CA-002 complex analysis in Stage 6.",
        "Review OpenStax's elementary/polar-form sequencing, check the full dependency graph, and obtain mathematics-educator feedback before implementing the split.",
        "Open",
        "Before producing a new workbook version or drafting the complex-number chapters."
    ]
    for col, value in enumerate(decision_values, 1):
        cell = open_decisions_ws.cell(decision_row, col, value)
        source_cell = open_decisions_ws.cell(decision_row - 1, col)
        if source_cell.has_style:
            cell._style = copy(source_cell._style)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.border = Border(bottom=thin)
    open_decisions_ws.row_dimensions[decision_row].height = 72
    for table in open_decisions_ws.tables.values():
        if re.fullmatch(r"A4:G\d+", table.ref):
            table.ref = f"A4:G{decision_row}"

concept_count, edge_count = len(concepts), len(edges)
decision_count = sum(bool(open_decisions_ws.cell(r, 1).value)
                     for r in range(5, open_decisions_ws.max_row + 1))
template_count = sum("is included as a learning prerequisite for" in e["why"] for e in edges)
all_core_proposed = sum("Core / presumed prerequisite" in e["type"] for e in edges)

# Combine numbered, versioned review batches and retain provenance per edge.
REVIEW_DIR = BASE / "reviews"
review_batch_files = sorted(REVIEW_DIR.glob("dependency-review-batch-*.json")) + sorted(REVIEW_DIR.glob("complex-number-split-review-v03.json"))
if not review_batch_files:
    raise FileNotFoundError(f"No dependency review batch files found in: {REVIEW_DIR}")
review_documents = [json.loads(path.read_text(encoding="utf-8")) for path in review_batch_files]
preliminary_reviews = {}
reviewer_by_edge = {}
review_date_by_edge = {}
review_batch_by_edge = {}
for document in review_documents:
    batch_edges = document.get("edges", {})
    if document.get("review_count") != len(batch_edges):
        raise ValueError(f"Review count mismatch in batch {document.get('batch_id')}.")
    for edge_id, item in batch_edges.items():
        if edge_id in preliminary_reviews:
            raise ValueError(f"Duplicate edge review across batches: {edge_id}")
        preliminary_reviews[edge_id] = item
        reviewer_by_edge[edge_id] = document["status"]
        review_date_by_edge[edge_id] = document["prepared_on"]
        review_batch_by_edge[edge_id] = document["batch_id"]
edge_by_id = {e["id"]: e for e in edges}
if not set(preliminary_reviews).issubset(edge_by_id):
    raise ValueError("Review batch contains an edge ID not present in the dependency list.")
allowed_classifications = {"Core required", "Helpful", "Repair path", "Contextual link", "Remove"}
if any(item[0] not in allowed_classifications for item in preliminary_reviews.values()):
    raise ValueError("Review batch contains an unsupported classification.")
if any(len(item) != 3 or not all(str(x).strip() for x in item) for item in preliminary_reviews.values()):
    raise ValueError("Every reviewed edge must include a classification, mechanism, and proposed validation check.")
review_counts = Counter(item[0] for item in preliminary_reviews.values())
concept_title_by_id = {c["id"]: c["title"] for c in concepts}
review_batch_summaries = []
for document in review_documents:
    batch_class_counts = Counter(item[0] for item in document["edges"].values())
    counts = ", ".join(f"{classification}: {count}" for classification, count in sorted(batch_class_counts.items()))
    review_batch_summaries.append(f"- {document['batch_id']}: {document['title']} — {len(document['edges'])} edges ({counts}); {document['status']}.")
review_batch_summary_text = "\n".join(review_batch_summaries)
review_batch_table = "\n".join(
    f"| {edge_id} | {edge_by_id[edge_id]['src']} — {concept_title_by_id[edge_by_id[edge_id]['src']]} → "
    f"{edge_by_id[edge_id]['dst']} — {concept_title_by_id[edge_by_id[edge_id]['dst']]} | {item[0]} | {review_batch_by_edge[edge_id]} |"
    for edge_id, item in preliminary_reviews.items()
)

start = wb["Start Here"]
start["A1"] = "MATHEMATICS, UNDERSTOOD — MASTER CURRICULUM MAP v0.3"
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
start["A14"] = "AI-assisted preliminary edge reviews"
start["B14"] = len(preliminary_reviews)
start["A15"] = "Edges still unreviewed"
start["B15"] = edge_count - len(preliminary_reviews)
for col in (1, 2):
    if start.cell(13, col).has_style:
        start.cell(14, col)._style = copy(start.cell(13, col)._style)
        start.cell(15, col)._style = copy(start.cell(13, col)._style)

dep["A1"] = "PREREQUISITE GRAPH — v0.3 complex-number scope patch (v0.2 baseline preserved)"
dep["A2"] = ("Directed edges remain proposals. v0.3 splits algebraic complex numbers from polar/geometric representation and preserves non-core contextual/helpful links separately. "
             "Use the Dependency Review sheet to classify each relationship and record specific evidence.")
dep["A2"].alignment = Alignment(wrap_text=True, vertical="center")
dep.row_dimensions[2].height = 34

if "Dependency Review" in wb.sheetnames:
    del wb["Dependency Review"]
review = wb.create_sheet("Dependency Review")
review.sheet_view.showGridLines = False
title(review, "DEPENDENCY REVIEW — Evidence and Classification Ledger", 11)
subtitle(review, "Baseline edge types and rationales remain provisional where unchanged. "
        f"{len(preliminary_reviews)} edges have AI-assisted preliminary desk reviews across the current batches; educator confirmation is pending. "
        f"{edge_count - len(preliminary_reviews)} rows remain UNREVIEWED. A preliminary classification is not a final pedagogical sign-off.", 11)
review.merge_cells(start_row=3, start_column=1, end_row=3, end_column=11)
review["A3"] = ("Review rule: a valid graph is not necessarily a valid curriculum. State the specific learning mechanism and a check/test; "
                "do not treat topic order or an LLM suggestion alone as evidence.")
review["A3"].fill = PatternFill("solid", fgColor=PALE_AMBER)
review["A3"].font = Font(name="Aptos", size=10, bold=True, color=DARK)
review["A3"].alignment = Alignment(wrap_text=True, vertical="center")
review.row_dimensions[3].height = 40
review_headers = ["Edge ID", "Prerequisite concept ID", "Dependent concept ID",
                  "Baseline edge type (provisional)", "Baseline rationale / review note",
                  "Baseline status", "v0.3 preliminary review classification", "Specific dependency mechanism / evidence",
                  "Proposed validation check / test", "Reviewer", "Review date"]
for col, value in enumerate(review_headers, 1):
    review.cell(4, col, value)
headers_style(review, 4, 1, 11)
for out_r, e in enumerate(edges, 5):
    review_item = preliminary_reviews.get(e["id"])
    if review_item:
        classification, mechanism, proposed_check = review_item
        review_fields = [classification, mechanism, proposed_check, reviewer_by_edge[e["id"]], review_date_by_edge[e["id"]]]
    else:
        review_fields = ["UNREVIEWED", None, None, None, None]
    values = [e["id"], e["src"], e["dst"], e["type"], e["why"], e["status"]] + review_fields
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
title(audit, "MASTER CURRICULUM MAP v0.3 — AUDIT & REVIEW QUEUE", 7)
subtitle(audit, "Automated structural audit completed 2026-10-19. Structural checks do not prove that every prerequisite is pedagogically necessary. Expert review and learner testing remain required.", 7)
checks = [
    ("Concept clusters", concept_count, "Matches the declared count." if concept_count == 104 else "Check declared count."),
    ("Directed prerequisite edges", edge_count, "Matches the declared count." if edge_count == 273 else "Check declared count."),
    ("Invalid edge endpoints", len(bad_endpoints), "Must be zero; each endpoint must resolve to a concept ID."),
    ("Duplicate directed edges", len(duplicates), "None detected." if not duplicates else "Resolve duplicates."),
    ("Directed cycle detected", "Yes" if cycle else "No", "Graph is acyclic; this does not establish pedagogical correctness."),
    ("Inventory/edge-list mismatch pairs after field validation", len(pair_mismatches), "Must be zero."),
    ("Invalid concept references in science links", len(bad_science_refs), "Must be zero; all references resolve."),
    ("Edges marked Core / presumed prerequisite", all_core_proposed, "All are provisional proposals, not confirmed necessities."),
    ("Template-style edge rationales", template_count, "Each edge needs a specific dependency mechanism and validation check."),
    ("Edges with AI-assisted preliminary desk review", len(preliminary_reviews), "Draft classifications only; educator confirmation and learner evidence remain pending."),
    ("Edges remaining unreviewed", edge_count - len(preliminary_reviews), "Do not infer a classification from the edge's position or old v0.1 label."),
    ("FND-001 field alignment", "Corrected during build" if field_fix else "Already aligned", "Cell-level check confirms representation notes are in the representation column and the prerequisite-ID field is empty."),
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
    ("RQ-002", "P1", "Dependency semantics", f"{len(preliminary_reviews)} of {edge_count} edges have AI-assisted preliminary desk classifications; {edge_count - len(preliminary_reviews)} remain unreviewed.",
     "Continue reviewing in focused tranches. Treat prefilled classifications as draft hypotheses until a mathematics educator checks them and learner diagnostics/transfer tasks support the intended pathway.",
     "Working", "Each edge has an explicit classification, specific mechanism, proposed validation check, reviewer, and date; educator sign-off is distinguished from AI-assisted desk review."),
    ("RQ-003", "P1", "Complex-number scope", "v0.3 provisionally splits CA-001 (algebraic complex numbers, Stage 1), CA-003 (complex plane/polar form, Stage 2), and CA-002 (complex analysis, Stage 6).",
     "Obtain mathematics-educator review of the three outcome scopes and edge classifications; run diagnostic/transfer checks before treating the split as final.",
     "Working — educator review pending", "A dated educator review and pilot-reader evidence support or revise each outcome and its prerequisites."),
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
        "[Master Curriculum Map v0.2 workbook](curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx) ([v0.1 baseline](curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.1.xlsx))",
        "[Master Curriculum Map v0.3 workbook](curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.3.xlsx) ([v0.2 baseline](curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx); [v0.1 historical baseline](curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.1.xlsx))"
    )
    content = content.replace(
        "early design and curriculum architecture; v0.2 includes structural checks and 35 AI-assisted preliminary dependency classifications, pending educator confirmation; 233 edges remain unreviewed. The curriculum remains a working draft, not a frozen table of contents.",
        f"early design and curriculum architecture; v0.3 provisionally splits complex-number outcomes across Stages 1, 2 and 6; {len(preliminary_reviews)} AI-assisted preliminary dependency classifications are recorded, educator confirmation is pending, and {edge_count - len(preliminary_reviews)} edges remain unreviewed. The curriculum remains a working draft, not a frozen table of contents."
    )
    content = content.replace(
        "[curriculum map workbook](curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.1.xlsx)",
        "[curriculum map workbook](curriculum/master-map/Mathematics_Understood_Master_Curriculum_Map_v0.3.xlsx)"
    )
    content = content.replace(
        "- **Dependency review:** [Batch 1](curriculum/master-map/DEPENDENCY_REVIEW_BATCH_01.md) and [Batch 2](curriculum/master-map/DEPENDENCY_REVIEW_BATCH_02.md) document draft classifications and proposed checks; neither is expert sign-off.",
        "- **Dependency review:** [Batch 1](curriculum/master-map/DEPENDENCY_REVIEW_BATCH_01.md), [Batch 2](curriculum/master-map/DEPENDENCY_REVIEW_BATCH_02.md), and [Batch 3](curriculum/master-map/reviews/complex-number-split-review-v03.json) document AI-assisted preliminary classifications and proposed checks; educator confirmation is pending."
    )
    content = content.replace(
        "- **Open curriculum proposal:** [Separate elementary complex numbers from complex analysis](curriculum/master-map/DECISION_PROPOSAL_CA001.md); no stage or dependency changes have been applied yet.",
        "- **Open curriculum decision:** [D-11 — complex-number scope split](curriculum/master-map/DECISION_PROPOSAL_CA001.md) has been implemented provisionally in v0.3; educator review and learner testing remain pending."
    )
    root_readme.write_text(content, encoding="utf-8")

(BASE / "README.md").write_text(
    "# Master Curriculum Map v0.3\n\n"
    "The current planning workbook is [Mathematics_Understood_Master_Curriculum_Map_v0.3.xlsx](Mathematics_Understood_Master_Curriculum_Map_v0.3.xlsx). "
    "The v0.2 [baseline](Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx) and v0.1 historical baseline are preserved unchanged.\n\n"
    "## What v0.3 adds\n\n"
    "- A provisional scope split: CA-001 algebraic complex numbers in Stage 1, CA-003 complex-plane/polar representation in Stage 2, and CA-002 complex analysis in Stage 6.\n"
    "- Coordinated updates to the Concept Inventory, prerequisite graph, Stage Map, Visual Catalogue, and D-11 open-decision record.\n"
    f"- {len(preliminary_reviews)} AI-assisted preliminary edge classifications across review batches 1–3; educator confirmation is pending and {edge_count - len(preliminary_reviews)} edges remain unreviewed.\n"
    "- Graph validation compares the Concept Inventory against core prerequisite edges only; helpful/contextual links are explicitly separate and are not treated as hard prerequisites.\n"
    "- Proposed validation checks are test plans, not reported learning results.\n\n"
    "## Dependency review documents\n\n"
    "- [Batch 1: Foundations into algebra and early functions](DEPENDENCY_REVIEW_BATCH_01.md) ([structured register](reviews/dependency-review-batch-01.json)).\n"
    "- [Batch 2: Polynomials, radicals, exponentials, and sequences](DEPENDENCY_REVIEW_BATCH_02.md) ([structured register](reviews/dependency-review-batch-02.json)).\n"
    "- [Batch 3: Complex-number scope split](reviews/complex-number-split-review-v03.json).\n\n"
    "## Open design record\n\n"
    "- [D-11: Complex-number scope split](DECISION_PROPOSAL_CA001.md). The split is implemented provisionally in v0.3; educator confirmation and learner testing remain pending.\n\n"
    "## Important interpretation rule\n\n"
    "A structurally consistent graph does not prove that every proposed prerequisite is pedagogically necessary. The 47 current classifications are AI-assisted preliminary judgments, not expert-approved decisions or empirical results. Keep mapped outcomes, entry diagnostics, bridge pathways, and learner evidence visible when refining the course order.\n\n"
    "When revising this workbook, preserve prior versioned baselines and record material changes in decisions/decision-log.md.\n",
    encoding="utf-8",
)

report = f"""# Master Curriculum Map v0.3 — Structural Audit Report

**Audit date:** {TODAY}  
**Baseline:** Mathematics_Understood_Master_Curriculum_Map_v0.2.xlsx  
**Successor:** Mathematics_Understood_Master_Curriculum_Map_v0.3.xlsx  
**Purpose:** Structural integrity and review-readiness, not a claim that every curriculum decision is correct.

## Findings

| Check | Result | Interpretation |
|---|---:|---|
| Concept clusters | {concept_count} | Matches the declared workbook count. |
| Directed prerequisite edges | {edge_count} | Matches the declared workbook count. |
| Invalid edge endpoints | {len(bad_endpoints)} | Every dependency endpoint resolves to a concept ID. |
| Duplicate directed edges | {len(duplicates)} | None detected. |
| Directed cycles | {"Detected" if cycle else "None detected"} | Graph structure only; no cycle is not proof of pedagogical validity. |
| Inventory/edge-list mismatch pairs after field validation | {len(pair_mismatches)} | The Concept Inventory prerequisite fields reconcile with the Dependencies edge list. |
| Invalid concept references in science links | {len(bad_science_refs)} | All science-link references resolve to current concept IDs. |
| Open design decisions | {decision_count} | D-11 has a provisional v0.3 implementation; educator review and learner validation remain pending. |
| Edges labelled Core / presumed prerequisite | {all_core_proposed} | These are provisional proposals, not validated necessities. |
| Template-style edge rationales | {template_count} | Each needs a specific dependency mechanism and validation check. |

## Changes made in v0.3

1. Preserved the v0.2 workbook unchanged and created v0.3 as a versioned successor.
2. Split CA-001 into Stage 1 algebraic complex numbers; added CA-003 for Stage 2 complex-plane/polar representation; retained CA-002 complex analysis in Stage 6.
3. Updated CA-001/CA-002 prerequisite IDs, reclassified affected edges, added EDGE-269 through EDGE-273, and synchronized the Stage Map and Visual Catalogue.
4. Updated D-11 to record the provisional implementation while leaving educator review and learner testing open.
5. Rebuilt the Dependency Review ledger from the structured registers and reran ID, endpoint, duplicate, cycle, and core-prerequisite reconciliation checks. The current batches contain {len(preliminary_reviews)} AI-assisted preliminary classifications; {edge_count - len(preliminary_reviews)} edges remain unreviewed.

## Complex-number scope split (v0.3 provisional implementation)

CA-001 now covers algebraic complex-number meaning and operations in Stage 1. CA-003 covers complex-plane representation, modulus/argument and polar form in Stage 2. CA-002 remains complex functions and complex differentiation in Stage 6. This split is supported as a plausible design by OpenStax’s [elementary complex numbers section](https://openstax.org/books/precalculus/pages/3-1-complex-numbers), its separate [polar-form section](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-5-polar-form-of-complex-numbers), and MIT OCW’s [Complex Variables with Applications syllabus](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/pages/syllabus/). These sources inform the design; they do not prove a unique best order or replace educator review. The patch remains provisional, and diagnostics/pilot-reader checks have not yet been conducted.

## Preliminary dependency-review batches

**Scope:** foundational/algebra review batches plus the complex-number scope split.  
**Preliminary desk-reviewed:** {len(preliminary_reviews)} of {edge_count}.  
**Still unreviewed:** {edge_count - len(preliminary_reviews)}.  
**Review status:** AI-assisted curriculum-design judgement; educator confirmation and learner evidence are pending. This is not an expert sign-off. Proposed validation checks are future checks, not completed experiments.

| Classification | Count |
|---|---:|
| Core required for the mapped outcome (with diagnostic/bridge pathways) | {review_counts.get("Core required", 0)} |
| Helpful but not a hard gate for the whole concept cluster | {review_counts.get("Helpful", 0)} |
| Contextual link | {review_counts.get("Contextual link", 0)} |

The review distinguishes a prerequisite for one sub-outcome (such as graphing a function) from a prerequisite for the entire concept cluster (such as defining a function as a mapping). “Core required” means required for the stated outcome as currently scoped, not that a learner should be excluded: diagnostics and short prerequisite instruction may be integrated into the dependent lesson.

| Edge ID | Connection | Draft classification | Batch |
|---|---|---|---|
{review_batch_table}

## What the structural audit does not prove

- It does not establish that an edge is required rather than helpful, contextual, or a repair path.
- It does not establish that every concept is covered at appropriate depth or in an ideal order.
- It does not establish that the teaching method improves learning; that requires reader testing.
- It does not replace mathematical review, science-source checking, accessibility review, or qualified educator feedback.

## Next steps

1. Obtain mathematics-educator review of the provisional complex-number split and its core/helpful/contextual links.
2. Validate the highest-leverage core prerequisites through diagnostics and the first reader pilots.
3. Continue focused review of the remaining 226 unreviewed edges.
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
assert check["Open Decisions"].cell(15, 1).value == "D-11"
assert check["Start Here"]["B13"].value == decision_count
assert any(table.ref == "A4:G15" for table in check["Open Decisions"].tables.values())
assert check["Dependency Review"].max_row == 4 + edge_count
assert check["Concept Inventory"].max_row >= new_concept_row
assert any(str(check["Concept Inventory"].cell(r, 1).value) == "CA-003" for r in range(5, check["Concept Inventory"].max_row + 1))
assert check["Concept Inventory"].cell(ca001_row_pre, 2).value == "1 — Algebra & functions"
assert check["Concept Inventory"].cell(ca002_row_pre, 2).value == "6 — Advanced theory"
assert check["Stage Map"].cell(stage1_row, 3).value.endswith("algebraic complex numbers in rectangular form.")
assert _locate_row(check["Visual Catalogue"], 1, "V-17") is not None
assert _locate_row(check["Open Decisions"], 1, "D-11") is not None
assert len(edges) == 273 and len(concepts) == 104
edge_255_review_row = 5 + next(i for i, edge in enumerate(edges) if edge["id"] == "EDGE-255")
edge_256_review_row = 5 + next(i for i, edge in enumerate(edges) if edge["id"] == "EDGE-256")
edge_269_review_row = 5 + next(i for i, edge in enumerate(edges) if edge["id"] == "EDGE-269")
edge_273_review_row = 5 + next(i for i, edge in enumerate(edges) if edge["id"] == "EDGE-273")
assert check["Dependency Review"].cell(edge_255_review_row, 7).value == "Core required"
assert check["Dependency Review"].cell(edge_256_review_row, 7).value == "Helpful"
assert check["Dependency Review"].cell(edge_269_review_row, 7).value == "Contextual link"
assert check["Dependency Review"].cell(edge_273_review_row, 7).value == "Helpful"
assert check["Dependencies"].cell(edge_row_by_id["EDGE-256"], 4).value == "Helpful / just-in-time link"
assert check["Dependencies"].cell(edge_row_by_id["EDGE-269"], 4).value == "Contextual link (non-prerequisite)"
assert pair_mismatches == [] and not cycle
assert sum(1 for r in range(5, 5 + edge_count) if check["Dependency Review"].cell(r, 7).value != "UNREVIEWED") == len(preliminary_reviews)
edge_029_row = 5 + next(i for i, edge in enumerate(edges) if edge["id"] == "EDGE-029")
assert check["Dependency Review"].cell(edge_029_row, 7).value == "Helpful"
assert "educator confirmation pending" in str(check["Dependency Review"].cell(edge_029_row, 10).value).lower()
edge_030_row = 5 + next(i for i, edge in enumerate(edges) if edge["id"] == "EDGE-030")
assert check["Dependency Review"].cell(edge_030_row, 7).value == "Core required"
assert "educator confirmation" in check["Dependency Review"].cell(edge_030_row, 10).value
check.close()
print(f"Created {OUTPUT}: {concept_count} concepts, {edge_count} edges.")
print(f"Invalid endpoints={len(bad_endpoints)}; duplicate edges={len(duplicates)}; cycles={cycle}; mismatches={len(pair_mismatches)}.")
