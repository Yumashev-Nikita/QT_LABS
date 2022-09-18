from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton

class evaluator(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.inputText = QLineEdit(self)
    self.inputText.setGeometry(10, 10, 100, 20)

    self.outputText = QLineEdit(self)
    self.outputText.setGeometry(175, 10, 100, 20)

    self.button = QPushButton("=", self)
    self.button.setGeometry(115, 10, 50, 20)
    self.button.clicked.connect(self.evaluateInput)

    self.setFixedHeight(30)

  def evaluateInput(self):
    self.outputText.setText(str(eval(self.inputText.text())))