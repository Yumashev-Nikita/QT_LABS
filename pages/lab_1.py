import sys

from mixins.tabsMixin import tabsMixin
from widgets.empty import empty
from widgets.lab_1.wordSwitcher import wordSwitcher
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTabWidget, QVBoxLayout

class Lab_1(tabsMixin):
  def __init__(self):
    super().__init__([
      {
        "func": wordSwitcher(),
        "name": "Task_1"
      },
      {
        "func": empty(),
        "name": "Task_2"
      },
      {
        "func": empty(),
        "name": "Task_3"
      },
    ])
    self.initUI()
  
  def initUI(self):
    self.tabs.setGeometry(100, 200, 300, 40)
