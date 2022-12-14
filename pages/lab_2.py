import sys

from mixins.tabsMixin import tabsMixin
from widgets.empty import empty

class Lab_2(tabsMixin):
  def __init__(self):
    super().__init__([
      {
        "func": empty(),
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
