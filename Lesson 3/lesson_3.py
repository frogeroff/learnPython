from user import User
from card import Card

alex = User("Alex")

alex.sayName()
alex.setAge(23)
alex.sayAge()

card = Card("4521 5784 4569 1354", "12/65", "Alex F")
card.pay(1000)

alex.addCard(card)
alex.getCard().pay(1000)