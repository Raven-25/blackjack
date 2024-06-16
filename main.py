import random
current_total = 0 
computer_total = 0 
total_cards = 51
player_standing = False 
computer_standing = False 

def setup():
    print("Welcome to Blackjack!")
    print("Your goal is to get as close to 21 as possible. You lose if you go over 21")
    print("The one who wins is the closest person to 21")
    print("Number cards are worth their number. J, Q, and K are worth 10. Ace is worth 1 or 11")
    print("Each turn you can choose to Hit and Stand") 
    print("Hit: Get a new card")
    print("Stand: Keep your current total")
    print('')

available_cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K","A","A","A","A"]

def init(): 
    global current_total
    global computer_total
    first_user_card = generate_card()
    second_user_card = generate_card()
    first_ai_card = generate_card()
    second_ai_card = generate_card()

    value = check_value(first_user_card, False)
    current_total += value 
    value = check_value(second_user_card, False)
    current_total += value 
    value = check_value(first_ai_card, True)
    computer_total += value 
    value = check_value(second_ai_card, True)
    computer_total += value

    print("You were dealt a " + str(first_user_card) + " and a " + str(second_user_card) + " your total is " + str(current_total))
    print("The computer was dealt a " + str(first_ai_card) + " and a " + str(second_ai_card) + " their total is " + str(computer_total))


def generate_card():
    global total_cards
    card_index = random.randint(0, len(available_cards))
    chosen_card = available_cards[card_index]
    available_cards.pop(card_index)
    total_cards -= 1
    return chosen_card

def check_value(card, computer):
    face_cards = ["J", "Q", "K"]
    if card in face_cards: 
        value = 10 
    elif card == "A":
        if computer: 
            if computer_total + 11 <= 21: 
                value = 11 
            else:
                value = 1 
        else:       
            print("You drew an ace!")
            value_choice = input("Do you want the card to be worth 1 or 11: ") 
            while value_choice not in ["1", "11"]:
                print("Invalid choice")
                value_choice = input("Do you want the card to be worth 1 or 11: ") 
            value = int(value_choice)
    else:
        value = card
    return value 
            
        


def user_turn():
    global current_total 
    global computer_total
    global player_standing
    #print("You pulled a " + str(chosen_card))
    action_options = ["hit", "stand"]
    face_cards = ["J", "Q", "K"]

    chosen_action = input("Do you want to hit or stand?: ").lower()
    while chosen_action not in action_options: 
        print("You can only hit or stand!")
        chosen_action = input("Do you want to hit or stand?: ").lower()


    if chosen_action == "hit":
        chosen_card = generate_card()
        value = check_value(chosen_card, False)
        current_total += value 
        if current_total > 21: 
            print("You busted")
            exit()
        else:
            print("You drew a " + str(chosen_card) + " your total is now " + str(current_total) + "!")
    elif chosen_action == "stand":
        print("You stand!")
        player_standing = True

    


def computer():
    global computer_standing
    global computer_total
    if computer_total <= 18 or current_total >= computer_total: 
        print("The computer hits") 
        chosen_card = generate_card()
        value = check_value(chosen_card, True) 
        computer_total += value 
        if computer_total > 21: 
            print("You won the computer busted")
            exit()
        else: 
            print("The computer drew a " + str(chosen_card) + " its total is " + str(computer_total))
    else:
        print("The computer stands")
        computer_standing = True
setup()
init()
while True: 
    print("")
    user_turn()
    print("")
    computer()
    if player_standing == True and computer_standing == True:
        if current_total > computer_total: 
            print("You won")
            exit()
        elif current_total < computer_total:
            print("You lost")
            exit()
        else: 
            print("Tied")
            exit()
