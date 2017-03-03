# Stepping the User through a Wizard

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Page1(QWizardPage):
    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)
        self.setTitle("What's Your Name?")
        self.setSubTitle("Please enter your name.")
        self.label = QLabel("Name:")
        self.uname = QLineEdit("<enter your name>")
        self.registerField("uname", self.uname)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.uname)
        self.setLayout(layout)

class Page2(QWizardPage):
    def __init__(self, parent=None):
        super(Page2, self).__init__(parent)
        self.setTitle("When's Your Birthday?")
        self.setSubTitle("Please Select Your Birthday.")
        self.cal = QCalendarWidget() 
        self.registerField("cal", self.cal, "selectedDate")
        layout = QVBoxLayout()
        layout.addWidget(self.cal)
        self.setLayout(layout)

class Page3(QWizardPage):
    def __init__(self, parent=None):
        super(Page3, self).__init__(parent)
        self.setTitle("About You")
        self.setSubTitle("Here is Your Information:")
        self.name_lbl = QLabel()
        self.date_lbl = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.name_lbl)
        layout.addWidget(self.date_lbl)
        self.setLayout(layout)
    # Initialize the page with dynamic data           
    def initializePage(self):
        uname = self.field("uname")
        date = self.field("cal").toString()
        self.name_lbl.setText("Your name is %s" % uname)
        self.date_lbl.setText("Your birthday is %s" % date)

wiz = QWizard()
wiz.addPage(Page1())
wiz.addPage(Page2())
wiz.addPage(Page3())
wiz.show()

