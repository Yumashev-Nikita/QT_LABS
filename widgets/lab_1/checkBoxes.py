from widgets.lab_1.wordSwitcher import wordSwitcher
from widgets.lab_1.evaluator import evaluator

from PyQt5.QtWidgets import QWidget, QCheckBox, QFormLayout

class checkBoxes(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.layout = QFormLayout()
    self.layout.setVerticalSpacing(30)

    self.wordSwitcher = wordSwitcher()
    self.evaluator = evaluator()

    self.wordSwitcherSwitch = QCheckBox("Word Switch")
    self.wordSwitcherSwitch.stateChanged.connect(self.toggle)

    self.evaluatorSwitch = QCheckBox("Evaluator Switch")
    self.evaluatorSwitch.stateChanged.connect(self.toggle)

    self.layout.addRow('111', self.wordSwitcherSwitch)
    self.layout.addRow('111', self.evaluatorSwitch)

    self.layout.addRow('111', self.wordSwitcher)
    self.layout.addRow('111', self.evaluator)
    self.setLayout(self.layout)

  def toggle(self):
    self.evaluator.setHidden(self.evaluatorSwitch.isChecked())
    self.wordSwitcher.setHidden(self.wordSwitcherSwitch.isChecked())
