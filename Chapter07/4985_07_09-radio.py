# Creating Radio Buttons

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class RadioButton(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.layout = QVBoxLayout()
        self.rb1 = QRadioButton('Option 1')
        self.rb2 = QRadioButton('Option 2')
        self.rb3 = QRadioButton('Option 3')
        self.textbox = QLineEdit()
        self.rb1.toggled.connect(self.rb1_active)
        self.rb2.toggled.connect(self.rb2_active)
        self.rb3.toggled.connect(self.rb3_active)
        self.layout.addWidget(self.rb1)
        self.layout.addWidget(self.rb2)
        self.layout.addWidget(self.rb3)
        self.layout.addWidget(self.textbox)
        self.setLayout(self.layout)

    # First radio button selected
    def rb1_active(self, on):
        if on:
            self.textbox.setText('Option 1 selected')

    # Second radio button selected
    def rb2_active(self, on):
        if on:
            self.textbox.setText('Option 2 selected')

    # Third radio button selected
    def rb3_active(self, on):
        if on:
            self.textbox.setText('Option 3 selected')


buttons = RadioButton()
buttons.show()