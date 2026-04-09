# SSbD Assessments Ontology

This page introduces how the SSbD assessments branch of the SSbD ontology is built and how the main classes are connected.
The choice to cateogrize SSbD primarily as an assessment process rather than a product property is based on the following considerations:
- SSbD is fundamentally about evaluating the safety and sustainability of chemicals and materials, which is an active process rather than a static property.


The diagram below summarizes the upper structure of the SSbD assessments branch:

[![SSbD assessments model](https://ssbd-ontology.github.io/core/docs/figs/ssbd-assessments.png)](https://ssbd-ontology.github.io/core/docs/figs/ssbd-assessments.png)

The `ssbd:SSbDAssessment` class represents the overall assessment process, which can be broken down into specific dimensions of assessment (e.g., hazard, exposure, lifecycle) using the `ssbd:hasPart` relation.
This means that an `ssbd:SSbDAssessment` can have multiple parts, targeting different dimensions of SSbD.
The various dimensions of SSbD are then considered by `ssbd:SpecifiedAssessment` subclasses.
It is important to make this distinction in the ontology because one such specified assessment is not by itself an `ssbd:SSbDAssessment`.
For instance, assessing the functionality is not a full `ssbd:SSbDAssessment`, but a part of it.
Introducing the `ssbd:SpecifiedAssessment` class allows for easy expansion of types of assessments that are
relevant for SSbD.

