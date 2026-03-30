# SSbD Core Ontology

Welcome to the **SSbD Core Ontology**, a semantic resource with essential terms and relationships to describe resources and provenance in Safe and Sustainable by Design.

## Quick example

````{tab-set}

```{tab-item} JSON-LD
```json
{
	"@context": "https://ssbd-ontology.github.io/core/context/core.jsonld",
	"@id": "https://example.org/dataset/tox-001",
	"@type": "ssbd:Dataset",
	"dcterms:title": "My toxicity dataset",
	"dcterms:description": "Measurements from in vitro assay campaign.",
	"dcterms:publisher": "https://orcid.org/0000-0000-0000-0001"
}
```
```

```{tab-item} Context link
Use the published JSON-LD context directly:

[https://ssbd-ontology.github.io/core/context/core.jsonld](https://ssbd-ontology.github.io/core/context/core.jsonld)
```

````

## Check out these resources to get started

````{grid} 1 1 2 2
:gutter: 3

```{grid-item-card} User guide
:link: document-your-data.html
:link-type: url

Start with a practical workflow for documenting your resources with table-based templates.
```

```{grid-item-card} Project overview
:link: overview.html
:link-type: url

Read the complete project overview, documentation map, and reference links.
```

```{grid-item-card} Background
:link: background.html
:link-type: url

Read the conceptual foundations, including provenance and relation patterns used in the ontology.
```

```{grid-item-card} Module pages
:link: models.html
:link-type: url

Explore domain branches such as Models, Matter, and Assessments.
```

```{grid-item-card} Reference index
:link: https://ssbd-ontology.github.io/core/core.html
:link-type: url

Browse all ontology terms, properties, and formal definitions.
```

````

## Documentation pages

```{toctree}
:maxdepth: 1
:caption: Contents

overview
background
guiding-principles
matter
models
assessments
classes
taxonomy
tools
repository_guide
document-your-data
```

## Additional links

- [Main reference documentation](https://ssbd-ontology.github.io/core/core.html)
- [Property reference index](https://ssbd-ontology.github.io/core/properties.html)
- [WIDOCO core module terms](https://ssbd-ontology.github.io/core/widoco/index-en.html)