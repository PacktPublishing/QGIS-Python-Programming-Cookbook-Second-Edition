# Using Log Files

# Settings/Options/System/Environment (use custom variables) 
# QGIS_LOG_FILE=/qgis_data/log.txt
# Restart QGIS

# Message to log file:
QgsLogger.logMessageToFile("This is a message to a log file.")

# Message to QGIS Log Window ( yellow triangle icon in the lower right)
QgsMessageLog.logMessage("This is a message from the Python Console", "Python Console", QgsMessageLog.INFO)