from widgets.lab_1.wordSwitcher import wordSwitcher
from widgets.lab_1.evaluator import evaluator

from PyQt5.QtWidgets import QWidget, QCheckBox, QFormLayout

class checkBoxes(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.layout = QFormLayout()

    self.wordSwitcher = wordSwitcher()
    self.evaluator = evaluator()

    self.wordSwitcherSwitch = QCheckBox("Word Switch")
    self.wordSwitcherSwitch.stateChanged.connect(self.toggle)
    self.wordSwitcherSwitch.setFixedHeight(30)

    self.evaluatorSwitch = QCheckBox("Evaluator Switch")
    self.evaluatorSwitch.stateChanged.connect(self.toggle)
    self.evaluatorSwitch.setFixedHeight(30)

    self.layout.addWidget(self.wordSwitcherSwitch)
    self.layout.addWidget(self.evaluatorSwitch)

    self.layout.addWidget(self.wordSwitcher)
    self.layout.addWidget(self.evaluator)
    self.setLayout(self.layout)

  def toggle(self):
    self.evaluator.setHidden(self.evaluatorSwitch.isChecked())
    self.wordSwitcher.setHidden(self.wordSwitcherSwitch.isChecked())
