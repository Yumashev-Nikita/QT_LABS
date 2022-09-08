from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton

class wordSwitcher(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.textLeft = QLineEdit(self)
    self.textLeft.setGeometry(10, 10, 100, 20)
  
    self.textRight = QLineEdit(self)
    self.textRight.setGeometry(175, 10, 100, 20)

    self.button = QPushButton("->", self)
    self.button.setGeometry(115, 10, 50, 20)
    self.button.clicked.connect(self.changeText)

  def changeText(self):
    if(self.button.text() == "->"):
      temp = self.textRight.text()
      self.textRight.setText(self.textLeft.text())
      self.textLeft.setText(temp)
      self.button.setText('<-')
    else:
      temp = self.textLeft.text()
      self.textLeft.setText(self.textRight.text())
      self.textRight.setText(temp)
      self.button.setText('->')