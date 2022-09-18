from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QPushButton, QGridLayout

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

class calculator(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.buttonMap = {}
    buttonsLayout = QGridLayout()
    keyBoard = [
      ["7", "8", "9", "/", "C"],
      ["4", "5", "6", "*", "("],
      ["1", "2", "3", "-", ")"],
      ["0", "00", ".", "+", "="],
    ]
    for row, keys in enumerate(keyBoard):
      for col, key in enumerate(keys):
        self.buttonMap[key] = QPushButton(key)
        self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
        self.buttonMap[key].clicked.connect(self.evaluateInput)
        buttonsLayout.addWidget(self.buttonMap[key], row, col)
    self.setLayout(buttonsLayout)

    self.inputText = QPlainTextEdit(self)

  def evaluateInput(self):
    current_input = self.inputText.toPlainText()
    user_input = self.sender().text()

    self.inputText.clear()
    if (self.sender().text() == "="):
      self.inputText.appendPlainText(str(eval(current_input)))
    else:
      self.inputText.appendPlainText(current_input + user_input)