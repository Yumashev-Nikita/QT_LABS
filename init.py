import sys

from pages.lab_1 import Lab_1
from pages.lab_2 import Lab_2
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Labs")
    self.resize(600, 1000)
    layout = QVBoxLayout()
    self.setLayout(layout)
    self.tabs = QTabWidget()
    self.tabs.addTab(Lab_1(), "LAB_1")
    self.tabs.addTab(Lab_2(), "LAB_2")
    layout.addWidget(self.tabs)
    self.initUI()
  
  def initUI(self):
    self.tabs.setGeometry(100, 100, 300, 40)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())