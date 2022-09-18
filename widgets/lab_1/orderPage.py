from PyQt5.QtWidgets import QWidget, QPlainTextEdit, QPushButton, QVBoxLayout
from widgets.lab_1.cards.dishCard import dishCard

class orderPage(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.layout = QVBoxLayout()

    DISHES = [
      {
        "name": "Chicken",
        "cost": "55",
      },
      {
        "name": "Beef",
        "cost": "75",
      },
      {
        "name": "Pork",
        "cost": "65",
      },
    ]

    self.dishCards = []
    for dish in DISHES:
      DISH_CARD = dishCard(dish)
      self.dishCards.append(DISH_CARD)
      self.layout.addWidget(DISH_CARD)

    self.orderButton = QPushButton("Заказать", self)
    self.orderButton.setMaximumWidth(100)
    self.orderButton.clicked.connect(self.makeOrder)

    self.outputText = QPlainTextEdit(self)
    self.outputText.setGeometry(10, 10, 100, 1000)

    self.layout.addWidget(self.orderButton)
    self.layout.addWidget(self.outputText)

    self.setFixedHeight(300)
    self.setFixedWidth(300)
    self.setLayout(self.layout)

  def makeOrder(self):
    self.outputText.clear()
    for dishCard in self.dishCards:
      self.outputText.appendPlainText(str(dishCard.name) + " * " + str(dishCard.count) + " * " + str(dishCard.cost) + "Р = " + str(int(dishCard.count) * int(dishCard.cost)) + "Р")
