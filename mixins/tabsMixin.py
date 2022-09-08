from PyQt5.QtWidgets import QWidget,  QTabWidget, QVBoxLayout

class tabsMixin(QWidget):
  def __init__(self, propTabs):
    super().__init__()
    layout = QVBoxLayout()
    self.setLayout(layout)
    self.tabs = QTabWidget()
    for tab in propTabs:
      self.tabs.addTab(tab.get('func'), tab.get('name'))
    layout.addWidget(self.tabs)
    self.initUI()
  
  def initUI(self):
    self.tabs.setGeometry(100, 200, 300, 40)
