import sys

from widgets.empty import empty
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTabWidget, QVBoxLayout

class Lab_2(QWidget):
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.setLayout(layout)
    self.tabs = QTabWidget()
    self.tabs.addTab(empty(), "Task_1")
    self.tabs.addTab(empty(), "Task_2")
    layout.addWidget(self.tabs)
    self.initUI()
  
  def initUI(self):
    self.tabs.setGeometry(100, 200, 300, 40)
