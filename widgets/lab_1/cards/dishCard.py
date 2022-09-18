from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton

class dishCard(QWidget):
  def __init__(self, dishData):
    super().__init__()
    self.initUI(dishData)

  def initUI(self, dishData):
    self.button = QPushButton(dishData.get("name"), self)
    self.button.setFixedWidth(100)

    self.outputText = QLineEdit(self)
    self.outputText.setFixedWidth(30)

    self.name = dishData.get("name")
    self.count = 0
    self.cost = dishData.get("cost")
    self.outputText.setText(str(self.count))

    self.button.clicked.connect(self.addCount)

    self.setFixedHeight(30)

  def addCount(self):
    self.count += 1
    self.outputText.setText(str(self.count))