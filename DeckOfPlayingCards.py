import random

cardfaces = []  # list holders to place cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
royals = ["J", "Q", "K", "A"]
deck = []

# loops to add our content
for i in range(2, 11):
    cardfaces.append(str(i))  # adds no 2-10 and convert them to string data

for j in range(4):
    cardfaces.append(royals[j])  # add royal faces to the cardbase
# print(cardfaces)

for k in range(4):
    for l in range(13):
        card = (cardfaces[l] + " of " + suits[k])
        # each card cycle through suits but first through  4 faces
        deck.append(card)  # adds the info to the full deck we want to make
        
random.shuffle(deck)  # shuffle the deck

# print the deck
for m in range(52):
    print(deck[m])

