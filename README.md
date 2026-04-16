# The SSbD Core Ontology

SSbD Core Ontology provides semantic annotations for the [Safe and Sustainable by Design](https://research-and-innovation.ec.europa.eu/research-area/industrial-research-and-innovation/chemicals-and-advanced-materials/safe-and-sustainable-design_en) (SSbD) approach to guide the innovation process for chemicals and materials. It adheres to the recommendations specified by DCAT-AP 3.0.1 as implemented in Tripper, and builds on PROV-O for provenance. It is constructed to be easily aligned with EMMO.

## Documentation

Documentation is available at the project website (https://ssbd-ontology.github.io/core), including:

- [Home page](https://ssbd-ontology.github.io/core/)
- [Project overview](https://ssbd-ontology.github.io/core/docs/overview.html)
- [Theoretical background](https://ssbd-ontology.github.io/core/docs/background.html)
- [User guide](https://ssbd-ontology.github.io/core/docs/document-your-data.html)
- [Modules and imports](https://ssbd-ontology.github.io/core/docs/modules.html)

Reference documentation:

- [Reference Index](https://ssbd-ontology.github.io/core/core.html)
- [Properties Index](https://ssbd-ontology.github.io/core/properties.html)
- [SSbDAssessments Index](https://ssbd-ontology.github.io/core/ssbdtaxonomy.html)
- [Models Index](https://ssbd-ontology.github.io/core/models.html)
- [Matter Index](https://ssbd-ontology.github.io/core/matter.html)
- [CHEMINF descriptors Index](https://ssbd-ontology.github.io/core/cheminf.html)

## Repository structure

- `core.ttl` is the main ontology module. The other top-level Turtle files provide companion modules and alignments, including the matter, models, taxonomy, CHEMINF, DCAT, ChEBI, contributor, and reused-term definitions used by the project.
- `docs/` contains the project documentation source for GitHub Pages, including background material, usage guidance, module descriptions, and supporting figures.
- `sources/` stores the tabular source files used to derive SSbD taxonomy content.
- `validation/` contains SHACL generation and validation tooling. See [validation/README.md](validation/README.md) for more information on approach and usage.
- `scripts/` contains utility scripts used to extract data, generate documentation artifacts, and build taxonomy resources from source material.
- `catalog-v001.xml` maps the project's ontology IRIs to local Turtle files, allowing ontology tools to resolve them locally.

## Contact

For questions, suggestions, or contributions, please contact [Thomas Exner](mailto:thomas.exner@sevenpastnine.com).
