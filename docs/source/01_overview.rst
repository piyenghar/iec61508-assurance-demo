.. what the demo is, how to build, what it shows

Overview
========

This demo shows how a minimal IEC 61508 safety lifecycle thread can be represented as structured,
traceable engineering artifacts using Sphinx and Sphinx-Needs. The example thread models a SIL 2
Emergency Stop safety function, from hazard and risk assessment through SIL allocation, requirements,
architecture, verification, and evidence.

Scope of the demo
-----------------

The documentation contains a single, end-to-end lifecycle thread:

- Hazard identification and risk assessment for an Emergency Stop function
- SIL allocation (target: SIL 2)
- Functional and technical safety requirements
- A minimal safety architecture
- Verification activities and linked evidence artifacts
- Traceability views and lifecycle completeness checks

Workflow
-----------------

This section describes the intended IEC 61508 lifecycle flow for the SIL 2 Emergency Stop thread.

The figure below illustrates the workflow, showing the key assurance artifacts and their relationships.

.. uml:: _static/iec61508_workflow.puml
   :caption: IEC 61508 SIL 2 Emergency Stop assurance workflow.  IEC 61508 SIL 2 Emergency Stop assurance workflow. Each node corresponds to a Sphinx-Needs artefact ID; each edge label corresponds to a validated link type used to generate traceability views and checks.
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


.. UML meta-model figure (PlantUML)

Meta-model
-----------------

The figure below defines the assurance artifact vocabulary used in the demo.

.. uml:: _static/iec61508_metamodel.puml
   :caption: Assurance artefact meta-model (demo vocabulary).  This vocabulary is enforced during build; only these link types are used in computed trace graphs and completeness checks.
   :align: center

Assurance Graph
-----------------

.. needflow::
   :root_id: HAZ_ESTOP_01
   :root_direction: outgoing
   :link_types: ADDRESSES,ALLOCATES,REFINES,REALIZES,VERIFIES,EVIDENCES,REVIEWS
   :types: hazard,risk,sil,fsr,tsr,arch,verif,evidence,confirm
   :show_link_names:
   :root_depth: 10
   :alt: Assurance chain rooted at HAZ_ESTOP_01