# Creating Checkboxes

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class CheckBox(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)    
        self.layout = QVBoxLayout()
        self.cb1 = QCheckBox('Option 1')
        self.cb2 = QCheckBox('Option 2')
        self.cb3 = QCheckBox('Option 3')
        self.textbox1 = QLineEdit()
        self.textbox2 = QLineEdit()
        self.textbox3 = QLineEdit()
        self.cb1.toggled.connect(self.cb1_active)
        self.cb2.toggled.connect(self.cb2_active)
        self.cb3.toggled.connect(self.cb3_active)
        self.layout.addWidget(self.cb1)
        self.layout.addWidget(self.cb2)
        self.layout.addWidget(self.cb3)
        self.layout.addWidget(self.textbox1)
        self.layout.addWidget(self.textbox2)
        self.layout.addWidget(self.textbox3)
        self.setLayout(self.layout)
    # First checkbox
    def cb1_active(self, on):
        if on:
            self.textbox1.setText('Option 1 selected')
        else: self.textbox1.setText('') 
    # Second checkbox  
    def cb2_active(self, on):
        if on:
            self.textbox2.setText('Option 2 selected')
        else: self.textbox2.setText('') 
    # Third checkbox      
    def cb3_active(self, on):
        if on:
            self.textbox3.setText('Option 3 selected')
        else: self.textbox3.setText('')

buttons = CheckBox()
buttons.show()