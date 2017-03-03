# Creating a Vector Layer in Memory

vectorLyr =  QgsVectorLayer('Point?crs=epsg:4326&field=city:string(25)&field=population:int', 'Layer 1' , "memory")
vectorLyr.isValid()
# True