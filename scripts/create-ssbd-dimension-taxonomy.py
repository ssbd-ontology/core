#!/usr/bin/env python
# pylint: disable=invalid-name
"""Generates ssbd-dimensions.ttl"""

from pathlib import Path

from tripper import DCTERMS, OWL, RDF, RDFS, Triplestore
from tripper.datadoc import TableDoc
from tripper.datadoc.keywords import Keywords
from tripper.datadoc.context import get_context
from tripper.utils import en

# Set constants
SSBD = "https://w3id.org/ssbd/core/ssbd-taxonomy"
VER = "0.0.1"

thisdir = Path(__file__).resolve().parent
rootdir = thisdir.parent

ctx = get_context('https://w3id.org/ssbd/context/')
#kw = Keywords(theme=None)
#kw.add(
#    (
#        "https://raw.githubusercontent.com/ssbd-ontology/core"
#        "/refs/heads/gh-pages/context/keywords.yaml"
#    ),
#    "yaml",
#    redefine="allow",
#)


# Create triplestore and load the SSbD taxonomy into it
ts = Triplestore("rdflib")

td = TableDoc.parse_csv(
    rootdir / "sources" / "ssbd_dimension_functionality_taxonomy.csv",
    type=None,
    prefixes={"ssbd": "https://w3id.org/ssbd/"},
    context=ctx,
    #keywords=kw,
    baseiri="https://w3id.org/ssbd/",
)
td.save(ts)

td = TableDoc.parse_csv(
    rootdir / "sources" / "ssbd_dimension_taxonomy.csv",
    type=None,
    prefixes={"ssbd": "https://w3id.org/ssbd/", "pink":"https://w3id.org/ssbd/"},
    context=ctx,
    #keywords=kw,
    baseiri="https://w3id.org/ssbd/",
)
td.save(ts)



# Add Ontology
ts.add_triples(
    [
        (SSBD, RDF.type, OWL.Ontology),
        (SSBD, OWL.versionIRI, f"https://w3id.org/ssbd/{VER}/ssbd-taxonomy"),
        (SSBD, DCTERMS.title, en("SSbD Taxonomy")),
        (
            SSBD,
            DCTERMS.abstract,
            en(
                "Taxonomy useful for categorizing activities and outputs"
                " of activities within the SSbD framework."
            ),
        ),
    ]
)

# Remove subClassOf rdfs:Class relations
ts.remove(predicate=RDFS.subClassOf, object=RDFS.Class)

# Save to file
ts.serialize(rootdir / "ssbd-taxonomy.ttl")
