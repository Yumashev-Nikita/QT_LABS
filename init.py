import sys

from pages.pages import Pages
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Labs")
    self.resize(600, 1000)
    layout = QVBoxLayout()
    self.setLayout(layout)
    self.pages = Pages()
    layout.addWidget(self.pages)
  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
