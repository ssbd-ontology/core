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

- [Background and design principles](background.html)
- [Matter module](matter.html)
- [Models module](models.html)
- [SSbD assessments module](assessments.html)
- [Taxonomy page](taxonomy.html)

## Other documentation resources
- [Classes page](classes.html)
- [Tools page](tools.html)
- [Guiding principles](guiding-principles.html)
- [Project overview](overview.html)

## Ontology source files

If you want the source-of-truth ontology files directly:

- [core.ttl](../core.ttl)
- [reused-terms.ttl](../reused-terms.ttl)
- [matter.ttl](../matter.ttl)
- [models.ttl](../models.ttl)
- [ssbd-taxonomy.ttl](../ssbd-taxonomy.ttl)
- [cheminf-mappings.ttl](../cheminf-mappings.ttl)
- [chebi-mappings.ttl](../chebi-mappings.ttl)
- [dcat-mappings.ttl](../dcat-mappings.ttl)
