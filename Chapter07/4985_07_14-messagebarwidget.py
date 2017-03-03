# Pushing widgets to the message bar

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.gui import *

class Bar(QProgressBar):
  value = 0  

  @pyqtSlot()
  def increaseValue(self):    
    self.setValue(self.value)
    self.value = self.value+1

bar = Bar()

bar.resize(300,40)
bar.setWindowTitle('Working...')

timer = QTimer()
bar.connect(timer,SIGNAL("timeout()"), bar, SLOT("increaseValue()"))
timer.start(100) 

iface.messageBar().pushWidget(bar, QgsMessageBar.INFO, 10)
