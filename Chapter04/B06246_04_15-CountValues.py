# Counting the Unique Values in a Raster

# https://github.com/GeospatialPython/Learn/raw/master/SatImage.zip

import gdalnumeric
a = gdalnumeric.LoadFile("/qgis_data/rasters/satimage.tif")
b = a.T.ravel()
c=b.reshape((b.size/3,3))
order = gdalnumeric.numpy.lexsort(c.T)
c = c[order]
diff = gdalnumeric.numpy.diff(c, axis=0)
ui = gdalnumeric.numpy.ones(len(c), 'bool')
ui[1:] = (diff != 0).any(axis=1) 
u = c[ui]
u.size
