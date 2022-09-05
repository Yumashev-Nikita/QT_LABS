import sys

from widgets.wordSwitcher import wordSwitcher
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTabWidget, QVBoxLayout

class Lab_2(QWidget):
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.setLayout(layout)
    self.tabs = QTabWidget()
    self.tabs.addTab(wordSwitcher(), "Task_1")
    self.tabs.addTab(wordSwitcher(), "Task_2")
    layout.addWidget(self.tabs)
    self.initUI()
  
  def initUI(self):
    self.tabs.setGeometry(100, 200, 300, 40)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Lab_2()
    window.show()
    sys.exit(app.exec())