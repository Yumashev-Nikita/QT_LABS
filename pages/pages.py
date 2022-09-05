import sys

from mixins.tabsMixin import tabsMixin
from widgets.empty import empty
from pages.lab_1 import Lab_1
from pages.lab_2 import Lab_2

class Pages(tabsMixin):
  def __init__(self):
    super().__init__([
      {
        "func": Lab_1(),
        "name": "Lab_1"
      },
      {
        "func": Lab_2(),
        "name": "Lab_2"
      },
      {
        "func": empty(),
        "name": "Lab_3"
      },
    ])
    self.initUI()
  
  def initUI(self):
    self.tabs.setGeometry(100, 100, 300, 40)
