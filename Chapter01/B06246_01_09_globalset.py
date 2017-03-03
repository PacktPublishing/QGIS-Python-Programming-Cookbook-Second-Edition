# Run in QGIS python console
settings = QSettings(QSettings.NativeFormat, QSettings.UserScope, 'QuantumGIS', 'QGis')
settings.setValue('/Projections/projectDefaultCrs', 'EPSG:2278')
settings.value('/Projections/projectDefaultCrs')
settings.sync()
