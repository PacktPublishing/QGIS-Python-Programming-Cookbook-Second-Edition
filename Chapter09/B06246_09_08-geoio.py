# Using the __geo_interface__ Protocol

# Based on code by Nathan Woodrow and modified by Martin Laloux
# http://nathanw.net/2013/06/25/adding-__geo_interface__-to-qgis-geometry-and-feature/
# https://github.com/mlaloux/Python-geo_interface-applications/blob/master/QGIS_add_geo_interface.py

import json

def mapping_feature(feature):
    geom = feature.geometry()
    properties = {}
    fields = [field.name() for field in feature.fields()]
    properties = dict(zip(fields, feature.attributes()))
    return { 'type' : 'Feature',
             'properties' : properties,
             'geometry' : geom.__geo_interface__}

def mapping_geometry(geometry):
    geo = geometry.exportToGeoJSON()
    return json.loads(geo)

QgsFeature.__geo_interface__ = property(lambda self: mapping_feature(self))
QgsGeometry.__geo_interface__ = property(lambda self: mapping_geometry(self))

# f.__geo_interface__

