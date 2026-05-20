# This document is intneded as support for the curators of the repository #

## Documentation setup ##

The `ontokit` tool avilable from EMMOntoPy was used to generate the standard documentation and workflows.
Note that the documentation and workflows are further refined according to the needs of the SSbD Core Ontology.


To generate the documentation locally please write the command
```bash
ontokit docs --imported --recursive --ontology-file=core.ttl --docs-dir=docs .
```

Note that it was chosen to include imported ontologies recursively since the ontology does not explicitly import ontologies from
outside. Rather we are explicitly including all terms from other ontologies that we are including.
This might change in the future.

Also note that not all links in the locally generated documentation will work since they are intended to be published on GitHub pages
as part of the .github/workflows/cd_ghpages.yml workflow.
