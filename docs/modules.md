# Modules and imports

This page gives a quick overview of how the SSbD Core Ontology is assembled from modules and where each part is documented.

## Core import structure

The root ontology in `core.ttl` imports the following core modules:

- `reused-terms` (`reused-terms.ttl`)
- `matter` (`matter.ttl`)
- `models` (`models.ttl`)
- `cheminf-mappings` (`cheminf-mappings.ttl`)
- `ssbd-taxonomy` (`ssbd-taxonomy.ttl`)

In simplified form:

```text
core
  -> reused-terms
  -> matter
  -> models
  -> cheminf-mappings
  -> ssbd-taxonomy
```

## Additional alignment and mapping modules

The repository also contains alignment modules that connect SSbD concepts to external vocabularies:

- `chebi-mappings.ttl` links SSbD/EMMO concepts to ChEBI.
- `dcat-mappings.ttl` aligns SSbD terms with DCAT terms.

These mapping modules are useful for interoperability and integration workflows.

## Module documentation pages

Use the pages below for human-readable descriptions of each module area:

- [Background and design principles](background.md)
- [Matter module](matter.md)
- [Models module](models.md)
- [SSbD assessments module](assessments.md)
- [Taxonomy page](taxonomy.md)

## Other documentation resources
- [Classes page](classes.md)
- [Tools page](tools.md)
- [Guiding principles](guiding-principles.md)
- [Project overview](overview.md)
