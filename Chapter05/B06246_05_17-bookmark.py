# Creating a Map Bookmark

# https://github.com/GeospatialPython/Learn/raw/master/GIS_CensusTract.zip

import sqlite3
dbPath = QgsApplication.qgisUserDbFilePath()
db = sqlite3.connect(dbPath)
cursor = db.cursor()

cursor.execute("""INSERT INTO tbl_bookmarks(
	bookmark_id, name, project_name,
	xmin, ymin, xmax, ymax, 
	projection_srid)
	VALUES(NULL, "BSL", NULL,
		-89.51715550010032,
		30.233838337125075,
		-89.27257255649518,
		30.381717490617945,
		4269)""")

db.commit()