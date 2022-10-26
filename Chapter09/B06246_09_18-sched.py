# Running QGIS Scripts as scheduled tasks

# https://github.com/GeospatialPython/Learn/raw/master/Mississippi.zip

import urllib
import datetime
import pytz
import tarfile
import sys
import os
import time
import schedule

# Tell Python where you will get processing from
sys.path.append('/Applications/QGIS.app/Contents/Resources/python')
sys.path.append("/Applications/QGIS.app/Contents/Resources/python/plugins/")

from qgis.core import *
from PyQt4.QtGui import *

def clip():

    # NOAA NEXRAD daily precip shapefile base URL
    url = "http://water.weather.gov/precip/p_download_new"

    # Get the current date
    c = pytz.timezone("US/Central")
    d = c.localize(datetime.datetime.today())

    # Convert the current date values to strings padded with zeros
    year, month, day = d.year, str(d.month).zfill(2), str(d.day).zfill(2)

    # Format the date values for the URL
    y_m_d = "{}/{}/{}".format(year, month, day)

    # Base filename for the download and shapefile
    base = "nws_precip_last60days_observed"

    # Date string for file names
    ymd = "{}{}{}".format(year, month, day)

    # Tar'd/zipped download name
    targz = "{}_shape_{}.tar.gz".format(base, ymd)

    # Full precipitation data download URL
    download = "{}/{}/{}".format(url, y_m_d, targz)

    if not os.path.isfile(targz):
        # Download the tar-zipped shapefile
        urllib.urlretrieve(download, targz)

        # Extract the shapefile
        with tarfile.open(targz, "r:gz") as tfile:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tfile, ".")

    # precipitation shapefile name    
    shp = "{}_{}.shp".format(base, ymd)
    shx = "{}_{}.shx".format(base, ymd)
    prj = "{}_{}.prj".format(base, ymd)
    dbf = "{}_{}.dbf".format(base, ymd)

    # Shapefile to clip
    in_shp = os.path.join(os.getcwd(), shp)

    # Shapefile we will use to clip
    clip = "/qgis_data/ms/mississippi.shp"

    # Output clipped shapefile
    clipped = "/qgis_data/ms/60_day_rainfall_{}.shp".format(ymd)

    app = QgsApplication([],True)
    QgsApplication.setPrefixPath(r"/Applications/QGIS.app/Contents/Plugins", True)
    QgsApplication.initQgis()

    from processing.core.Processing import Processing
    from processing.tools import general
    Processing.initialize()

    # Clip the shapefile
    general.runalg("qgis:clip", in_shp, clip, clipped)

    if os.path.isfile(targz):
        os.remove(targz)
        os.remove(shp)
        os.remove(shx)
        os.remove(prj)
        os.remove(dbf)
    
    QgsApplication.exitQgis()

schedule.every(30).seconds.do(clip)    
#schedule.every().day.at("16:00").do(clip)

while True:
    schedule.run_pending()
    time.sleep(1)