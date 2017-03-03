# Creating Dynamic Forms in QGIS

# https://github.com/GeospatialPython/Learn/raw/master/MS_UrbanAnC10.zip

from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
popFld = None
dynamicDialog = None
 
def dynamicForm(dialog,lyrId,featId):
    global dynamicDialog
    dynamicDialog = dialog
    global popFld
    popFld = dialog.findChild(QLineEdit,"POP")
    buttonBox = dialog.findChild(QDialogButtonBox,"buttonBox")
    # Disconnect the button box signal.
    buttonBox.accepted.disconnect(dynamicDialog.accept)
    # Create our own signals and connect them to the dialog.
    buttonBox.accepted.connect(validate)
    buttonBox.rejected.connect(dynamicDialog.reject)
 
def validate():
  # Make sure that the population > 0.
    if not float(popFld.text()) > 0:
        msg = QMessageBox(f)
        msg.setText("Population must be greater than zero.")
        msg.exec_()
    else:
        # Return the form as accpeted to QGIS.
        dynamicDialog.accept()