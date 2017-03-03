# Load a NetCDF file

# https://github.com/GeospatialPython/Learn/raw/master/tos_O1_2001-2002.nc

uri='NETCDF:"/qgis_data/rasters/tos_O1_2001-2002.nc":tos'
rlayer = QgsRasterLayer(uri,'Sea Surface Temperature')
rlayer.isValid()
QgsMapLayerRegistry.instance().addMapLayer(rlayer)