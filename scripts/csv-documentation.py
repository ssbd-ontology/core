#!/usr/bin/env python
# pylint: disable=invalid-name
"""
Generates csv documentation of all SSbD concepts
"""

from pathlib import Path

from tripper import OWL, Namespace, Triplestore
from tripper.datadoc import TableDoc, acquire

thisdir = Path(__file__).resolve().parent
rootdir = thisdir.parent


ts = Triplestore("rdflib")
ts.parse("core.ttl")

# SSBD = ts.namespaces["ssbd"]
SSBD = Namespace("https://w3id.org/ssbd/")

ssbd_concepts = set(s for s in ts.subjects() if s.startswith(str(SSBD)))
dicts = [acquire(ts, iri) for iri in ssbd_concepts]

classes = [d for d in dicts if OWL.Class in d["@type"]]
properties = [d for d in dicts if OWL.Class not in d["@type"]]

td_classes = TableDoc.fromdicts(classes)
td_classes.write_csv("classes.csv")

td_properties = TableDoc.fromdicts(properties)
td_properties.write_csv("properties.csv")


print("")
print("SSbD concepts:")
for c in ssbd_concepts:
    print("  -", c)
