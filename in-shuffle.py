from random import shuffle
class Card:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite

def deck():
    suites = ['heart', 'diamonds', 'spades', 'clubs']
    deck = [Card(value, suite) for value in range(1, 14) for suite in suites]
    return deck

def in_shuffle(deck):
    deck1,deck2=deck[0:int(len(deck)/2)],deck[int(len(deck)/2):len(deck)]
    new_deck=[val for pair in zip(deck2, deck1) for val in pair]
    return new_deck

if __name__ == "__main__":
    
    my_deck=deck()
    shuffle(my_deck)
    # for data in my_deck:
    #     print(data.value,data.suite)
    ################### QUESTION#2 ###################################
    print(my_deck[0].value,my_deck[0].suite)
    print(my_deck[len(my_deck)-1].value,my_deck[len(my_deck)-1].suite)
    shuffled_deck=in_shuffle(my_deck)
    
    
    for i in range(0,27):
        shuffled_deck=in_shuffle(shuffled_deck)
    print(shuffled_deck[len(shuffled_deck)-2].value,shuffled_deck[len(shuffled_deck)-2].suite)
    print(shuffled_deck[len(shuffled_deck)-1].value,shuffled_deck[len(shuffled_deck)-1].suite)

