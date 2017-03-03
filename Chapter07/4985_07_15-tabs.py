# Creating Tabs

from PyQt4.QtCore import *
from PyQt4.QtGui import *

qtw = QTabWidget()
qtw.setWindowTitle("PyQGIS Tab Example")
qtw.resize(400,300)

tab1 = QWidget()
tab2 = QWidget()
tab3 = QWidget()

layout1 = QVBoxLayout()
layout1.addWidget(QTextEdit("<b>Type text here</b>"))
tab1.setLayout(layout1)

layout2 = QVBoxLayout()
layout2.addWidget(QPushButton("Button"))
tab2.setLayout(layout2)

layout3 = QVBoxLayout()
layout3.addWidget(QLabel("Label text example"))
tab3.setLayout(layout3)

qtw.addTab(tab1, "First Tab")
qtw.addTab(tab2, "Second Tab")
qtw.addTab(tab3, "Third Tab")

qtw.show()