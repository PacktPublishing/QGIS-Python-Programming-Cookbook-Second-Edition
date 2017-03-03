# Run in QGIS Python Console
QgsProject.instance().title("My QGIS Project")
QgsProject.instance().title()
proj.writeEntry("MyPlugin", "splash", "Geospatial Python Rocks!")
proj.readEntry("MyPlugin", "splash", "Welcome!")[0]
