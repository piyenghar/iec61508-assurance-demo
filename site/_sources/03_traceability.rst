Traceability Views
==================

This section provides traceability views over the SIL 2 Emergency Stop lifecycle artifacts.

All lifecycle artifacts
-----------------------

.. needtable::
   :types: hazard,risk,sil,fsr,tsr,arch,verif,evidence,confirm
   :columns: id;title;type;phase;sil_level;owner_role
   :sort_by: id

Emergency Stop thread (filtered by ID prefix)
---------------------------------------------

.. needtable::
   :filter: "ESTOP" in id
   :columns: id;title;type;phase;sil_level
   :sort_by: id

Verification coverage (FSR without verification)
------------------------------------------------

The following table lists functional safety requirements that do not yet have a verification activity linked.

.. needtable::
   :types: fsr
   :filter: "'verifies' not in links_back or len(links_back['verifies']) == 0"
   :columns: id;title;phase;sil_level;owner_role
   :sort_by: id

Evidence coverage (verification without evidence)
-------------------------------------------------

The following table lists verification activities that do not yet have evidence linked.

.. needtable::
   :types: verif
   :filter: "'evidences' not in links_back or len(links_back['evidences']) == 0"
   :columns: id;title;phase;owner_role
   :sort_by: id

SIL allocation coverage (risk without SIL allocation)
-----------------------------------------------------

The following table lists risk assessment items that do not yet have a SIL allocation linked.

.. needtable::
   :types: risk
   :filter: "'allocates' not in links_back or len(links_back['allocates']) == 0"
   :columns: id;title;phase;owner_role
   :sort_by: id