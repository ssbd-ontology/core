# SSbD Core Ontology

Welcome to the **SSbD Core Ontology**, a semantic resource with essential terms and relationships to describe resources and provenance in Safe and Sustainable by Design.

## Quick example

`````{tab-set}

````{tab-item} JSON-LD
```json
{
	"@context": "https://w3id.org/ssbd/context/",
	"@id": "https://example.org/dataset/tox-001",
	"@type": "ssbd:Dataset",
	"dcterms:title": "My toxicity dataset",
	"dcterms:description": "Measurements from in vitro assay campaign.",
	"dcterms:publisher": "https://orcid.org/0000-0000-0000-0001"
}
```
````

````{tab-item} JSON-LD Playground
```{raw} html
<div style="position: relative; padding-top: 56.25%;">
	<iframe src="https://json-ld.org/playground/#startTab=tab-expanded&json-ld=%7B%22%40context%22%3A%22https%3A%2F%2Fw3id.org%2Fssbd%2Fcontext%2F%22%2C%22%40id%22%3A%22https%3A%2F%2Fexample.org%2Fdataset%2Ftox-001%22%2C%22%40type%22%3A%22ssbd%3ADataset%22%2C%22dcterms%3Atitle%22%3A%22My%20toxicity%20dataset%22%2C%22dcterms%3Adescription%22%3A%22Measurements%20from%20in%20vitro%20assay%20campaign.%22%2C%22dcterms%3Apublisher%22%3A%22https%3A%2F%2Forcid.org%2F0000-0000-0000-0001%22%7D" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen>
	</iframe>
</div>

```
````

`````

## Check out these resources to get started

````{grid} 1 1 2 2
:gutter: 3

```{grid-item-card} Theoretical Background
:link: background.html
:link-type: url

Read the conceptual foundations, including provenance and relation patterns used in the ontology.
```

```{grid-item-card} Project overview
:link: overview.html
:link-type: url

Overview of all the resources in documentation.
```

```{grid-item-card} Detailed description of the modules
:link: modules.html
:link-type: url

The starting page for the individual modules, describing their content and interconnections.
```

```{grid-item-card} User guide
:link: document-your-data.html
:link-type: url

Practical introduction to documenting your resources with table-based templates.
```

````
