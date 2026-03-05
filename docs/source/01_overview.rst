.. what the demo is, how to build, what it shows

Overview
========

This demo encodes a minimal IEC 61508 safety lifecycle thread for a SIL 2
Emergency Stop as structured, typed engineering artifacts using Sphinx and
Sphinx-Needs.

The example spans:

- Hazard and risk assessment
- SIL allocation
- Functional and technical safety requirements
- Safety architecture
- Verification activities
- Evidence artifacts
- Confirmation measures

Unlike conventional document-centric safety documentation, each lifecycle
element is represented as a typed object with explicitly declared relations.
Allowed artifact types and link semantics are constrained by a predefined
meta-model and validated at build time.

Traceability graphs and lifecycle completeness checks are computed directly
from these declared relations. Missing structural links (e.g., requirement
without verification) are automatically detected.

Scope
-----

This demonstration focuses strictly on structural lifecycle consistency.

It does not evaluate:

- Semantic correctness of hazard analysis
- Quantitative SIL determination
- Architectural metrics (e.g., HFT, SFF)
- Probabilistic calculations
- Full safety case argumentation

The purpose is to demonstrate executable lifecycle structure and automated
traceability enforcement for a single SIL 2 thread.

Meta-model
----------

The figure below defines the assurance artifact vocabulary used in the demo.

.. uml:: _static/iec61508_metamodel.puml
   :caption: Assurance artefact meta-model (demo vocabulary). This vocabulary is enforced during build; only these link types are used in computed trace graphs and completeness checks.
   :align: center

Workflow
--------

This section describes the intended IEC 61508 lifecycle flow for the SIL 2 Emergency Stop thread.

The figure below illustrates the workflow, showing the key assurance artifacts and their relationships.

.. uml:: _static/iec61508_workflow.puml
   :caption: IEC 61508 SIL 2 Emergency Stop assurance workflow. Each node corresponds to a Sphinx-Needs artefact ID; each edge label corresponds to a validated link type used to generate traceability views and checks.
   :align: center

1. Hazard
2. Risk assessment
3. SIL allocation
4. Functional safety requirements (FSR)
5. Technical safety requirements (TSR)
6. Safety architecture
7. Verification activities
8. Evidence artifacts
9. Confirmation measures

Each node corresponds to a Sphinx-Needs artefact ID; each edge label corresponds to a validated link type used to generate traceability views and checks.

Assurance Graph
---------------

.. needflow::
   :root_id: HAZ_ESTOP_01
   :root_direction: both
   :link_types: ADDRESSES,ALLOCATES,REFINES,REALIZES,VERIFIES,EVIDENCES,REVIEWS
   :types: hazard,risk,sil,fsr,tsr,arch,verif,evidence,confirm
   :show_link_names:
   :root_depth: 10
