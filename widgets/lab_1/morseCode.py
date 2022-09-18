from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

class morseCode(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.layout = QVBoxLayout()

    self.outputText = QLineEdit(self)
    self.outputText.setGeometry(10, 10, 100, 20)

    self.layout.addWidget(self.outputText)

    for letter in MORSE_CODE_DICT:
      button = QPushButton(letter, self)
      button.setFixedWidth(30)
      button.setFixedHeight(30)
      button.clicked.connect(self.morseTranslate)
      self.layout.addWidget(button)

    self.setFixedHeight(900)
    self.setLayout(self.layout)

  def morseTranslate(self):
    sender = self.sender()
    self.outputText.setText(MORSE_CODE_DICT[sender.text()])