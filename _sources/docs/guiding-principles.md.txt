Guiding principles
==================
The SSbD Core Ontology strives to follow the guiding principles described in this section.


Never change the semantics of existing terms
--------------------------------------------
The SSbD Core Ontology never changes the semantics of existing terms defined externally (e.g. by W3C or DCAT-AP).
However, the SSbD Core Ontology can:
- Make the documentation of externally defined terms explicit in the Knowledge Base (KB) without importing the whole vocabularies.
- Make an existing term a subclass of a broader concept. This should be understood as broaden the scope of the parent class rather than limiting the scope of the existing term.
- Add SSbD-specific relations that has the existing terms as subject. E.g. SSbD may add a `ssbd:usageNote` to an existing term (but should not add a `vann:usageNote`).
- Add a `ddoc:conformance` relation that specifies whether the relation is "mandatory", "recommended" or "optional" in SSbD.
  The SSbD Core Ontology will never change the conformance described in the DCAT-AP documentation to something weaker.

The basic rule for such additions is that they can live hand-in-hand with similar annotations by other projects without creating confusion or inconsistencies.

For any other additional specifications of an existing term, a SSbD-specific subclass or subproperty will be created.
Such subclasses/subproperties will normally keep the W3C name, but with the `ssbd` namespace (or the `ddoc` namespace if the concept is specific for the tripper data documentation).


Alignment to top-level ontologies
---------------------------------
The SSbD Core Ontology is by itself not a top-level ontology, but is strives to be easy to align with different top-level ontologies, like [EMMO] and [BFO].  However, the goal is only to be able to align with one top-level ontology at the time. Furthermore is the goal not to be able to create a fully consistent ontological framework when aligning to a top-level ontology, but to be able to create interoperability and connect to domain ontologies based on different top-level ontologies.

Since the SSbD Core Ontology is intended to be used within applied sciences and to connect SSbD to materials, it reuses useful parts from the conceptualisation of EMMO, which is an ontology exactly designed for materials and applied sciences. However, the reused parts conceptualisation is simplified as much as possible and limited to the needs of the SSbD Core Ontology.
Examples of such reused conceptualisations include:
* To categorise all relations as either parthood relations (that relates a part or role to a whole), causal relations (to describe causal interactions) and  semiotics (to provide meaning to a sign via an interpreter that connects the sign to an object in the real-world).
* That properties are observables, i.e. signs resulting from a semiotic process where an interpreter connects them to the observed object.
