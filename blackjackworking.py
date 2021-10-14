import random

deck_of_cards = {
    "AD":11, "2D":2, "3D":3, "4D":4, "5D":5, "6D":6, "7D":7, "8D":8, "9D":9, "10D":10, "JD":10, "QD":10, "KD":10,
    "AH":11, "2H":2, "3H":3, "4H":4, "5H":5, "6H":6, "7H":7, "8H":8, "9H":9, "10H":10, "JH":10, "QH":10, "KH":10,
    "AC":11, "2C":2, "3C":3, "4C":4, "5C":5, "6C":6, "7C":7, "8C":8, "9C":9, "10C":10, "JC":10, "QC":10, "KC":10,
    "AS":11, "2S":2, "3S":3, "4S":4, "5S":5, "6S":6, "7S":7, "8S":8, "9S":9, "10S":10, "JS":10, "QS":10, "KS":10}

def shuffle_deck():
    random.shuffle(deck)

def deal_player():
    hand.append(deck.pop())

def deal_dealer():
    dealer.append(deck.pop())

def show_options():
    print("")
    print("| 1. Hit | 2. Stay |")

def get_choice():
    global choice
    choice = input("What do you choose?: ")
    return choice

def check_dealer_bj():
    if d_total == 21:
        print("Dealer has BlackJack, you lose!")
        quit()
    else:
        #print("Dealer does not have BlackJack")
        pass

def show_player_hand():
    print("")
    print("You have:")
    for x,y in hand:
        print(x)
    
def show_dealer_hand():
    print("Dealer has:")
    for x,y in dealer:
        print(x)
    print("")

def show_first_dealer():
    global dealer_ace
    dealer_ace = 0
    first_card = []
    for x,y in dealer:
        first_card.append(x)
    print("Dealer shows:",first_card[0])
    if "AC" == first_card[0] or "AD" == first_card[0] or "AS" == first_card[0] or "AH" == first_card[0]:
        dealer_ace = 1
    else:
        dealer_ace = 0
    return dealer_ace
    
def cal_hand():
    global h_total
    hand_cards = [] 
    for x,y in hand:
        hand_cards.append(y)
    h_total = sum(hand_cards)
    return h_total 
        
def cal_dealer():
    global d_total
    dealer_cards = [] 
    for x,y in dealer:
        dealer_cards.append(y)
    d_total = sum(dealer_cards)
    return d_total

def compare_hands():
    if h_total > d_total:
        print(f"You have {h_total}, dealer has {d_total}. You Win!")
    elif h_total < d_total and d_total < 21:
        print(f"You have {h_total}, dealer has {d_total}. You Lose!")
    elif h_total < d_total and d_total > 21:
        print(f"You have {h_total}, dealer has {d_total}. You Win!")
    elif h_total == d_total:
        print(f"You have {h_total}, dealer has {d_total}. You tied for a Push!")
    quit()
   
def busted():
    print("You busted with:",h_total)
    quit()

def dealer_option():
    while d_total < 17:
        print("Dealer has less than 17, and hits.")
        deal_dealer()
        cal_dealer()
        show_dealer_hand()
        if d_total > 21:
            print("Dealer busted with a total of:", d_total)
            pass
    
deck = list(deck_of_cards.items())
shuffle_deck()
hand = []
dealer = []
h_total = 0
d_total = 0
dealer_ace = 0

while True:
    start_game = input("Do you want to play BlackJack? (Y/N): ").lower()

    if start_game == "y":
        print("")
        deal_player()
        deal_dealer()
        deal_player()
        deal_dealer()
        show_first_dealer()
        show_player_hand()
        cal_dealer()
        cal_hand()
        if h_total == 21:
            print("You have BlackJack! You Win!")
            quit()
        else:
            pass
        if dealer_ace == 1:
            check_dealer_bj()
        else:
            pass
        show_options()
        get_choice()
        if choice == "1":
            deal_player()
            show_player_hand()
            cal_hand()
            if h_total < 21:
                show_options()
                get_choice()
                if choice == "1":
                    deal_player()
                    show_player_hand()
                    cal_hand()
                    if h_total < 21:
                        show_options()
                        get_choice()
                        if choice == "1":
                            deal_player()
                            show_player_hand()
                            cal_hand()
                            if h_total < 21:
                                show_options()
                                get_choice()
                            else:
                                busted()
                        elif choice == "2":
                            show_dealer_hand()
                            dealer_option()
                            compare_hands() 
                    else:
                        busted()
                elif choice == "2":
                    show_dealer_hand()
                    dealer_option()
                    compare_hands()    
            else:
                busted()
        elif choice == "2":
            show_dealer_hand()
            dealer_option()
            compare_hands()
        else:
            print("Not a valid option")
    elif start_game == "n":
        print("Sorry you didn't want to play.")
        print("Goodbye!")
        quit()
    else:
        print("Enter 'Y' for Yes, or 'N' for No.")
