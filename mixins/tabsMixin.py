import sys

from widgets.empty import empty
from widgets.lab_1.wordSwitcher import wordSwitcher
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTabWidget, QVBoxLayout

class tabsMixin(QWidget):
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.setLayout(layout)
    self.tabs = QTabWidget()
    for tab in propTabs:
      self.tabs.addTab(tab.func, tab.name)
    self.tabs.addTab(wordSwitcher(), "Task_1")
    self.tabs.addTab(empty(), "Task_2")
    self.tabs.addTab(empty(), "Task_3")
    self.tabs.addTab(empty(), "Task_4")
    layout.addWidget(self.tabs)
    self.initUI()
  
  def initUI(self):
    self.tabs.setGeometry(100, 200, 300, 40)
