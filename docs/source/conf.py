# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'IEC 61508 Assurance-as-Code Demo'
copyright = '2026, Dr. Padma Iyenghar'
author = 'Dr. Padma Iyenghar'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

extensions = [
    "sphinx_needs",
    "sphinxcontrib.plantuml",
]

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]

plantuml_output_format = "svg"

needs_id_required = True
needs_title_optional = False

needs_types = [
    {"directive": "hazard",   "title": "Hazard"},
    {"directive": "risk",     "title": "Risk Assessment"},
    {"directive": "sil",      "title": "SIL Allocation"},
    {"directive": "fsr",      "title": "Functional Safety Requirement"},
    {"directive": "tsr",      "title": "Technical Safety Requirement"},
    {"directive": "arch",     "title": "Safety Architecture"},
    {"directive": "verif",    "title": "Verification Activity"},
    {"directive": "confirm",  "title": "Confirmation Measure"},
    {"directive": "evidence", "title": "Evidence Artifact"},
]

needs_fields= [
    "phase",
    "sil_level",
    "owner_role",
    "part_ref",
    "artifact_kind",
]

needs_links = [
    {"option": "addresses", "incoming": "addressed by", "outgoing": "addresses"},
    {"option": "allocates", "incoming": "allocated by", "outgoing": "allocates"},
    {"option": "mitigates", "incoming": "mitigated by", "outgoing": "mitigates"},
    {"option": "refines",   "incoming": "refined by", "outgoing": "refines"},
    {"option": "realizes",  "incoming": "realized by", "outgoing": "realizes"},
    {"option": "verifies",  "incoming": "verified by", "outgoing": "verifies"},
    {"option": "produces",  "incoming": "produced by", "outgoing": "produces"},
    {"option": "reviews",   "incoming": "reviewed by", "outgoing": "reviews"},
]