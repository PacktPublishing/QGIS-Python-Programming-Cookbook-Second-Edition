# Navigating to a Map Bookmark

# https://github.com/GeospatialPython/Learn/raw/master/GIS_CensusTract.zip

import sqlite3
dbPath = QgsApplication.qgisUserDbFilePath()
db = sqlite3.connect(dbPath)
cursor = db.cursor()
cursor.execute("""SELECT * FROM tbl_bookmarks WHERE name='BSL'""")
row = cursor.fetchone()
id,mark_name,project,xmin,ymin,xmax,ymax,srid = row
rect = QgsRectangle(xmin, ymin, xmax, ymax)
canvas = qgis.utils.iface.mapCanvas()
canvas.setExtent(rect)
canvas.refresh()


