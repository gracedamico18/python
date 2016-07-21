#Project 2 - Grace D'Amico

#Activity 1
import random

def main():
    name, current_money = restore()
    if name == ' ':
        name = input("Name? ")
        current_money = int(1000)
        print(name, " has $", current_money, "\n",sep="")
        bet = 25
        user_bet = input_bet(bet, current_money, name)
        change_in_money = int(0)
        while current_money > 0:
            change_in_money = play_hand(name, user_bet)
            current_money += change_in_money
            print(name, " has $", current_money, "\n", sep="")
            save(name, current_money)
            user_bet = input_bet(user_bet, current_money, name)
    else:
        print("Resume saved game ", name, "? (y/n) ", sep="", end="") 
        resume = input()
        if resume == "y":
            print(name, " has $", current_money, "\n",sep="")
            user_bet = input_bet(25, current_money, name)
            change_in_money = int(0)
            while current_money > 0:
                change_in_money = play_hand(name, user_bet)
                current_money += change_in_money
                print(name, " has $", current_money, "\n", sep="")
                save(name, current_money)
                user_bet = input_bet(user_bet, current_money, name)
            if current_money <= 0:
                print("Game over.")
                quit()
        else:
            name = input("Name? ")
            current_money = int(1000)
            print(name, " has $", current_money, "\n",sep="")
            change_in_money = int(0)
            user_bet = input_bet(25, current_money, name)
            while current_money > 0:
                change_in_money = play_hand(name, user_bet)
                current_money += change_in_money
                print(name, " has $", current_money, "\n", sep="")
                save(name, current_money)
                user_bet = input_bet(user_bet, current_money, name)
            if current_money <= 0:
                print("Game over.")
                quit()
                
def play_hand(name, user_bet):
    dealer_hand_string = []
    dealer_hand_value = 0
    player_hand_string = []
    player_hand_value = 0
    
    deck = new_deck()
    shuffled_deck_list = shuffle_deck(deck)
    
    dealer = shuffled_deck_list[0]
    del shuffled_deck_list[0]
    
    print("\nBet: $", user_bet, sep="")
    dealer_hand_string.append(string_of_hand(dealer))
    dealer_hand_value += value_of_hand(dealer)
    print("Dealer's hand:", *dealer_hand_string, sep=" ")
    print("Value:", dealer_hand_value)

    player1 = shuffled_deck_list[0]
    del shuffled_deck_list[0]
    player2 = shuffled_deck_list[0]
    del shuffled_deck_list[0]
    player_hand_string.append(string_of_hand(player1))
    player_hand_string.append(string_of_hand(player2))
    if value_of_card(player1) == 11 and value_of_card(player2) == 11:
        player1 = 1
        player2 = 11
    player_hand_value += value_of_hand(player1)
    player_hand_value += value_of_hand(player2)

    print(name, "'s hand: ", sep="", end="")
    print(*player_hand_string, sep=" ")
    print("Value:", player_hand_value)

    if player_hand_value == 21:
        print("Player wins \n")
        return int(user_bet)
    
    while player_hand_value < 21:
        move = input("Move? (hit/stay) ")
        if move == "h":
            print("\nBet: $", user_bet, sep="")
            print("Dealer's hand:", *dealer_hand_string, sep=" ")
            print("Value:", dealer_hand_value)
            player3 = shuffled_deck_list[0]
            del shuffled_deck_list[0]
            if value_of_card(player3) == 11 and (value_of_card(player1) == 11 or value_of_card(player2) == 11):
                player3 == 1
            player_hand_string.append(string_of_hand(player3))
            player_hand_value += value_of_hand(player3)
            print(name, "'s hand: ", sep="", end="")
            print(*player_hand_string, sep=" ")
            print("Value:", player_hand_value)

            if player_hand_value > 21:
                print("Player bust \n")
                return int(-user_bet)

            if player_hand_value == dealer_hand_value:
                print("Push \n")
                return int(0)
            elif dealer_hand_value > 21 and player_hand_value != 21:
                print("Dealer bust \n")
                return int(user_bet)
            elif dealer_hand_value != 21 and player_hand_value > 21:
                print("Player bust \n")
                return int(-user_bet)
            elif player_hand_value == 21:
                print("Player wins \n")
                return int(user_bet)
            elif dealer_hand_value == 21:
                print("Dealer wins \n")
                return int(-user_bet)

           
        elif move == "s":
            while dealer_hand_value < 17:
                dealer1 = shuffled_deck_list[0]
                del shuffled_deck_list[0]
                if value_of_card(dealer1) == 11 and value_of_card(dealer) == 11:
                    dealer1 = 1
                print("\nBet: $", user_bet, sep="")
                dealer_hand_string.append(string_of_hand(dealer1))
                dealer_hand_value += value_of_hand(dealer1)
                print("Dealer's hand:", *dealer_hand_string, sep=" ")
                print("Value:", dealer_hand_value)

            if player_hand_value == dealer_hand_value:
                print("Push \n")
                return int(0)
            elif dealer_hand_value > 21 and player_hand_value != 21:
                print("Dealer bust \n")
                return int(user_bet)
            elif dealer_hand_value != 21 and player_hand_value > 21:
                print("Player bust \n")
                return int(-user_bet)
            elif player_hand_value == 21:
                print("Player wins \n")
                return int(user_bet)
            elif dealer_hand_value == 21:
                print("Dealer wins \n")
                return int(-user_bet)
            elif dealer_hand_value >= 17:
                if dealer_hand_value > player_hand_value:
                    print("Player bust \n")
                    return int(-user_bet)
                else:
                    print("Dealer bust \n")
                    return int(user_bet)


#Activity 2
def value_of_card(card):
    if card[0] == 1:
        point_value = 11
    elif 2 <= card[0] <= 10:
        point_value = card[0]
    else:
        point_value = 10
    return point_value

#Activity 2 & 6
def string_of_card(card):
    if card[0] == 1:
        string_value = "A" + card[1]
    elif card[0] == 2:
        string_value = "2" + card[1]
    elif card[0] == 3:
        string_value = "3" + card[1]
    elif card[0] == 4:
        string_value = "4" + card[1]
    elif card[0] == 5:
        string_value = "5" + card[1]
    elif card[0] == 6:
        string_value = "6" + card[1]
    elif card[0] == 7:
        string_value = "7" + card[1]
    elif card[0] == 8:
        string_value = "8" + card[1]
    elif card[0] == 9:
        string_value = "9" + card[1]
    elif card[0] == 10:
        string_value = "10" + card[1]
    elif card[0] == 11:
        string_value = "J" + card[1]
    elif card[0] == 12:
        string_value = "Q" + card[1]
    else:
        string_value = "K" + card[1]
    return string_value


#Activity 3 - saves name and money to file
def save(name, money):
    blackjack_file = open("blackjack.txt", "w")
    blackjack_file.write(name + "\n")
    blackjack_file.write(str(money) + "\n")
    blackjack_file.close()

#Activity 3 - read name and money from file
def restore():
    try:
        open_file = open("blackjack.txt", "r")
    except ValueError:
        name = " "
        money = -1
        return name, money
    except FileNotFoundError:
        name = " "
        money = -1
        return name, money
    
    name = open_file.readline()
    name = name.rstrip('\n')
    money = open_file.readline()
    money = money.rstrip('\n')
    money = int(money)
    return name, money

#Activity 4
def input_bet(bet, money, name):
    print("Bet? (0 to quit, Enter to stay at $", bet, ") ", sep="", end="")
    user_bet = input()
    if user_bet == '':
        user_bet = bet
        return user_bet
    elif user_bet == '0':
        save(name, money)
        print("Game over.")
        quit()
        
    error = True
    while error == True:
        try:
            user_bet = int(user_bet)
            error = False
        except ValueError:
            print("Must enter an integer. ", end="")
            user_bet = input()
            error = True

    while user_bet < 0 or user_bet > money:
        user_bet = input("Bet must be greater than 0 and less than your current amount of money. ")
        error = True
        while error == True:
            try:
                user_bet = int(user_bet)
            except ValueError:
                print("Must enter an integer. ", end="")
                user_bet = input()
                error = True
            else:
                error = False
    return user_bet
        
#Activity 5 & 6
def new_deck():
    deck_list = []
    for card in range(1, 14):
        club = (card, '♣')
        diamond = (card, '♦')
        heart = (card, '♥')
        spade = (card, '♠')
        for number in range(0,4):
            if number == 0:
                deck_list.append(club)
            elif number == 1:
                deck_list.append(diamond)
            elif number == 2:
                deck_list.append(heart)
            else:
                deck_list.append(spade)
    return deck_list

#Activity 5
def shuffle_deck(deck):
    deck_shuffled = []
    deck_length = len(deck_shuffled)
    n = 51
    while deck_length < 52:
        random_card = random.randint(0, n)
        value = deck[random_card]
        deck_shuffled.append(value)
        del deck[random_card]
        n -= 1
        deck_length = len(deck_shuffled)
    return deck_shuffled

#Activity 7
def string_of_hand(hand):
    hand_string = string_of_card(hand)
    return hand_string

def value_of_hand(hand):
    hand_value = value_of_card(hand)       
    return hand_value

main()
