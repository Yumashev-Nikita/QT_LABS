import sys

from mixins.tabsMixin import tabsMixin
from widgets.empty import empty
from widgets.lab_1.wordSwitcher import wordSwitcher
from widgets.lab_1.evaluator import evaluator
from widgets.lab_1.checkBoxes import checkBoxes

class Lab_1(tabsMixin):
  def __init__(self):
    super().__init__([
      {
        "func": wordSwitcher(),
        "name": "Task_1"
      },
      {
        "func": evaluator(),
        "name": "Task_2"
      },
      {
        "func": checkBoxes(),
        "name": "Task_3"
      },
    ])
    self.initUI()
  
  def initUI(self):
    self.tabs.setGeometry(100, 200, 300, 40)
