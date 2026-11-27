# Modules and imports

This page gives a quick overview of how the SSbD Core Ontology is assembled from modules and where each part is documented.

## Core import structure

The root ontology in `core.ttl` imports the following core modules:

- [`Reused terms`](https://w3id.org/ssbd/core/reused-terms)
- [`Matter module`](https://w3id.org/ssbd/core/matter)
- [`Models module`](https://w3id.org/ssbd/core/models)
- [`Cheminf`](https://w3id.org/ssbd/core/cheminf)
- [`SSbD taxonomy`](https://w3id.org/ssbd/core/ssbd-taxonomy)

In simplified form:

```text
core
  -> reused-terms
  -> matter
  -> models
  -> cheminf
  -> ssbd-taxonomy
```

## Additional alignment and mapping modules

The repository also contains alignment modules that connect SSbD concepts to external vocabularies:

- `chebi-mappings.ttl`(https://w3id.org/ssbd/core/chebi-mappings) links SSbD/EMMO concepts to ChEBI.
- `dcat-mappings.ttl`(https://w3id.org/ssbd/core/dcat-mappings) aligns SSbD terms with DCAT terms. 

These mapping modules are useful for interoperability and integration workflows.

## Module documentation pages

Use the pages below for human-readable descriptions of each module area:

- [Background and design principles](background.md)
- [Matter module](matter.md)
- [Models module](models.md)
- [SSbD taxonomy module](assessments.md)

## Other documentation resources
- [Classes page](classes.md)
- [Tools page](tools.md)
- [Guiding principles](guiding-principles.md)
- [Project overview](overview.md)
