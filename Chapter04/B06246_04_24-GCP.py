# Georeferencing a Raster from Ground Control Points

# https://github.com/GeospatialPython/Learn/raw/master/georef.zip

from processing.algs.gdal.GdalUtils import GdalUtils

src = "/qgis_data/rasters/georef/1853survey.jpg"
points = "/qgis_data/rasters/georef/1853survey.points"
trans = "/qgis_data/rasters/georef/1835survey_trans.tif"
final = "/qgis_data/rasters/georef/1835survey_georef.tif"

gcp = open(points, "rb")
hdr = gcp.readline()
command = ["gdal_translate"]
for line in gcp:
  x,y,col,row,e = line.split(",")
  command.append("-gcp")
  command.append("%s" % col)
  command.append("%s" % abs(float(row)))
  command.append("%s" % x)
  command.append("%s" % y)    

command.append(src)
command.append(trans) 

GdalUtils.runGdal(command, None)

command = ["gdalwarp"]
command.extend(["-r", "near", "-order", "3", "-co", "COMPRESS=NONE", "-dstalpha"])

command.append(trans) 
command.append(final)

GdalUtils.runGdal(command, None)


