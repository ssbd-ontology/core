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

```{tab-item} Context link
Use the published JSON-LD context directly:

[https://ssbd-ontology.github.io/core/context/core.jsonld](https://ssbd-ontology.github.io/core/context/core.jsonld)
```

````

## Check out these resources to get started

````{grid} 1 1 2 2
:gutter: 3

```{grid-item-card} Theoretical Background
:link: docs/background.html
:link-type: url

Read the conceptual foundations, including provenance and relation patterns used in the ontology.
```

```{grid-item-card} Project overview
:link: docs/overview.html
:link-type: url

Overview of all the resources in documentation.
```

```{grid-item-card} Detailed description of the modules
:link: docs/modules.html
:link-type: url

The starting page for the individual modules, describing their content and interconnections.
```

```{grid-item-card} User guide
:link: docs/document-your-data.html
:link-type: url

Practical introduction to documenting your resources with table-based templates.
```

````
