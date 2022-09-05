import sys

from widgets.wordSwitcher import wordSwitcher
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTabWidget, QVBoxLayout

class Lab_1(QWidget):
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.setLayout(layout)
    self.tabs = QTabWidget()
    self.tabs.addTab(wordSwitcher(), "Task_1")
    self.tabs.addTab(wordSwitcher(), "Task_2")
    self.tabs.addTab(wordSwitcher(), "Task_3")
    self.tabs.addTab(wordSwitcher(), "Task_4")
    layout.addWidget(self.tabs)
    self.initUI()
  
  def initUI(self):
    self.tabs.setGeometry(100, 200, 300, 40)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Lab_1()
    window.show()
    sys.exit(app.exec())