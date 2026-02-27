# Configuration file for the Sphinx documentation builder.
#
# ---------------------------------------------------------------------------
# TUTORIAL OVERVIEW (for colleagues reading this demo repository)
# ---------------------------------------------------------------------------
#
# This file (conf.py) is both:
#
#   1) The build configuration for Sphinx (how documentation is generated)
#   2) The "domain model" definition for Sphinx-Needs (safety artifact model)
#
# In this demo, we model a minimal IEC 61508 SIL 2 lifecycle thread
# for an Emergency Stop function. The lifecycle artifacts (hazard, risk,
# SIL allocation, requirements, architecture, verification, evidence, etc.)
# are represented as structured "needs".
#
# The configuration below therefore has two conceptual layers:
#
# ---------------------------------------------------------------------------
# 1. Sphinx Basics (Required)
# ---------------------------------------------------------------------------
#
# - Project information (project, author, release):
#     Metadata shown in the generated documentation.
#
# - extensions:
#     Enables functionality. In this demo we use:
#
#     sphinx_needs
#         Enables structured artifacts such as:
#             .. hazard::
#             .. risk::
#             .. fsr::
#             .. needflow::
#         and provides trace tables and lifecycle views.
#
#     sphinxcontrib.plantuml
#         Allows rendering of PlantUML diagrams (optional but useful
#         for architecture and metamodel visualization).
#
# - html_theme, html_static_path:
#     Define how the site looks and where static assets (SVG, CSS, etc.) live.
#
# ---------------------------------------------------------------------------
# 2. Sphinx-Needs Configuration (Lifecycle Domain Model)
# ---------------------------------------------------------------------------
#
# This is where we define the safety engineering "meta-model" used
# throughout the demo.
#
# - needs_id_required = True
#     Forces every artifact to have a stable :id:
#     (important for traceability and lifecycle linking).
#
# - needs_title_optional = False
#     Forces each artifact to have a meaningful title.
#
# - needs_types
#     Defines the artifact types (directives) used in this demo.
#     For the SIL 2 example we define:
#
#         hazard   → Hazard identification
#         risk     → Risk assessment result
#         sil      → SIL allocation decision
#         fsr      → Functional Safety Requirement
#         tsr      → Technical Safety Requirement
#         arch     → Safety architecture element
#         verif    → Verification activity
#         confirm  → Confirmation measure
#         evidence → Evidence artifact
#
#     Each type has:
#         - a directive name (used in .rst files)
#         - a human-readable title (used in tables and views)
#
# - needs_fields
#     Defines additional structured attributes that any artifact may have.
#     Examples:
#
#         phase         → IEC 61508 lifecycle phase
#         sil_level     → SIL classification (e.g., SIL2)
#         owner_role    → Responsible engineering role
#         part_ref      → IEC 61508 clause reference
#         artifact_kind → Optional classification
#         tool_ref      → Tool or report reference
#
#     These fields allow filtering, reporting, and lifecycle analysis.
#
# - needs_links
#     Defines allowed relationships between artifacts.
#     Example lifecycle relationships:
#
#         addresses  → Risk addresses Hazard
#         allocates  → SIL allocation applies to Risk
#         refines    → Requirement refines SIL decision
#         realizes   → Architecture realizes Requirement
#         verifies   → Verification verifies Requirement
#         evidences  → Evidence documents Verification result
#         reviews    → Independent review of lifecycle artifact
#
#     Without declaring link types here, they cannot be used
#     in the .rst files.
#
# ---------------------------------------------------------------------------
# End of tutorial section.
# ---------------------------------------------------------------------------

# -- Project information -----------------------------------------------------

project = "IEC 61508 Assurance-as-Code Demo"
copyright = "2026, Dr. Padma Iyenghar"
author = "Dr. Padma Iyenghar"
release = "1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx_needs",
    "sphinxcontrib.plantuml",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]

# -- PlantUML ---------------------------------------------------------------

# Keep enabled for later diagrams. Configure ONE of the following when ready:
# Option A: PlantUML jar (local)
#plantuml = "java -jar ./tools/plantuml.jar"


import os
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent  # docs/source -> repo root
_PLANTUML_JAR = _REPO_ROOT / "tools" / "plantuml" / "plantuml.jar"

plantuml = f'java -jar "{_PLANTUML_JAR}"'
plantuml_output_format = "png"
#
# Option B: PlantUML server
# plantuml = "http://www.plantuml.com/plantuml"
#
#plantuml = "http://www.plantuml.com/plantuml"
#plantuml_output_format = "png"

# -- Sphinx-Needs core behavior ---------------------------------------------

needs_id_required = True
needs_title_optional = False
 

# If you want IDs with hyphens like EVID-PLAN-01, enable this:
needs_id_regex = r"^[A-Z][A-Z0-9_-]{2,}$"

needs_types = [
    {"directive": "hazard",   "title": "Hazard",                     "prefix": "HAZ_"},
    {"directive": "risk",     "title": "Risk Assessment",            "prefix": "RISK_"},
    {"directive": "sil",      "title": "SIL Allocation",             "prefix": "SIL_"},
    {"directive": "fsr",      "title": "Functional Safety Requirement","prefix": "FSR_"},
    {"directive": "tsr",      "title": "Technical Safety Requirement","prefix": "TSR_"},
    {"directive": "arch",     "title": "Safety Architecture",        "prefix": "ARCH_"},
    {"directive": "verif",    "title": "Verification Activity",      "prefix": "VERIF_"},
    {"directive": "confirm",  "title": "Confirmation Measure",       "prefix": "CONF_"},
    {"directive": "evidence", "title": "Evidence Artifact",          "prefix": "EVID_"},
]

# Custom fields available for all needs
# Add schema/nullable/default to avoid needs.config warnings in newer sphinx-needs.
needs_fields = {
    "phase": {
        "name": "Lifecycle phase",
        "schema": {"type": "string"},
        "nullable": True,
        "default": "",
    },
    "sil_level": {
        "name": "SIL Level",
        "schema": {"type": "string"},
        "nullable": True,
        "default": "",
    },
    "owner_role": {
        "name": "Owner role",
        "schema": {"type": "string"},
        "nullable": True,
        "default": "",
    },
    "part_ref": {
        "name": "IEC 61508 part ref",
        "schema": {"type": "string"},
        "nullable": True,
        "default": "",
    },
    "artifact_kind": {
        "name": "Artifact kind",
        "schema": {"type": "string"},
        "nullable": True,
        "default": "",
    },
    "tool_ref": {
        "name": "Tool reference",
        "schema": {"type": "string"},
        "nullable": True,
        "default": "",
    },
}

needs_links = {
    "addresses": {"incoming": "addressed_by", "outgoing": "addresses"},
    "allocates": {"incoming": "allocated_by", "outgoing": "allocates"},
    "refines": {"incoming": "refined_by", "outgoing": "refines"},
    "realizes": {"incoming": "realized_by", "outgoing": "realizes"},
    "verifies": {"incoming": "verified_by", "outgoing": "verifies"},
    "evidences": {"incoming": "evidenced_by", "outgoing": "evidences"},
    "reviews": {"incoming": "reviewed_by", "outgoing": "reviews"},
    "produces": {"incoming": "produced_by", "outgoing": "produces"},
}

# Quality-of-life settings (optional)
needs_table_style = "datatables"
needs_show_link_type = True


needs_flow_engine = "graphviz"

needs_graphviz_styles = {
    "assurance_light": {
        "graph": {
            "bgcolor": "white",
        },
        "node": {
            "style": "filled,rounded",
            "fillcolor": "#FFFFFF",
            "color": "#555555",
            "fontcolor": "#222222",
        },
        "edge": {
            "color": "#777777",
            "fontcolor": "#777777",
        },
    },
}






