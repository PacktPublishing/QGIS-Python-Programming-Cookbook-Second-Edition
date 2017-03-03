# Displaying a Progress Bar

from PyQt4.QtGui import *
from PyQt4.QtCore import *

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
timer.start(500) 

bar.show()