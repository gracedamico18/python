#make a Card class
#data attributes: __type (int) and __suit (str)
#methods: set_type(), set_suit(), __init__, value(), __str__()

class Card:
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    def value(self):
        return self.__rank

    def __str__(self):
        if self.__rank == 1:
            return "A" + self.__suit
        elif self.__rank == 11:
            return "J" + self.__suit
        elif self.__rank == 12:
            return "Q" + self.__suit
        elif self.__rank == 13:
            return "K" + self.__suit
        else:
            return str(self.__rank) + self.__suit

    def set_rank(self, new_rank):
        self.__rank = new_rank

    def set_suit(self, new_suit):
        self.__suit = new_suit

def main():
    ace_of_spades = Card(1, '\u2660')
    print(ace_of_spades, "has value", ace_of_spades.value())
    two_of_spades = Card(2, '\u2660')
    print(two_of_spades, "has value", two_of_spades.value())


main()
 

