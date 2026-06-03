import random



def poker_hand():
    cards = []
    def_suit = ["Ruter", "Hjärter", "Spader", "Klöver"]
    def_card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dam", "Kung", "Ess"]

    while len(cards) < 5:

        card_value = random.choice(def_card_value)
        card_suit = random.choice(def_suit)
        cards.append(card_suit + " " + str(card_value))

    return cards

your_hand = poker_hand()

print(f"Din hand: \n")
for i in your_hand:
    print(i)