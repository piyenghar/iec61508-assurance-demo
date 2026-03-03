# IEC 61508 Assurance-as-Code Demo

This repository demonstrates a minimal IEC 61508 safety lifecycle thread for a SIL 2 Emergency Stop, encoded as structured, typed engineering artifacts using Sphinx and Sphinx-Needs.

The demo illustrates how lifecycle artifacts (hazard, risk, SIL allocation, requirements, architecture, verification, evidence, confirmation) can be represented as executable objects with constrained link semantics. Traceability graphs and lifecycle completeness checks are computed at build time.

---

## Quick Overview

For a quick overview without building the project, see:

`docs/source/IEC_61508_Assurance_Demo.pdf`

This PDF provides a static snapshot of the complete lifecycle thread. Please note that, this file is provided here to give a quick overview and is extracted from the generated html pages. 

---

## Repository Structure

```
docs/
├── source/
│   ├── 01_overview.rst
│   ├── 02_artifacts.rst
│   ├── 03_traceability.rst
│   ├── 04_checks.rst
│   ├── conf.py
│   └── IEC_61508_Assurance_Demo.pdf
└── build/  (generated output, not committed)
```


---

## Requirements

- Python 3.10+
- Sphinx
- sphinx-needs
- sphinx-book-theme
- sphinxcontrib-plantuml

For example, install dependencies inside a virtual environment:

```bash
pip install sphinx sphinx-needs sphinx-book-theme sphinxcontrib-plantuml
```
---
## Build HTML Documentation

From the docs directory:

```bash

sphinx-build -b html ./source ./build/html -E -a
```
Then open:

```
docs/build/html/index.html
```

in your browser.


## Scope of the Demonstration

This demo focuses strictly on structural lifecycle consistency.

It does not evaluate:

Semantic correctness of hazard analysis

Quantitative SIL determination

Architectural metrics (e.g., HFT, SFF)

Probabilistic calculations

Full safety case argumentation

The purpose is to demonstrate executable lifecycle structure and automated traceability enforcement for a single SIL 2 thread.

---
© 2026 Dr. Padma Iyenghar / innotec GmbH – TÜV Austria Group
