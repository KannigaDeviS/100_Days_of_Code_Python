import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def restart_game():
    choice = input("Do you wish to restart the game? 'y' or 'n': ").lower()
    if choice == 'y':
        print("\n"*20)
        print(art.logo)
        start_game()
    else:
        print("Ending Game")
        exit()

def calculate_score(list_to_sum):
    if len(list_to_sum) == 2 and 11 in list_to_sum and 10 in list_to_sum:
        return 0
    else:
        if 11 in list_to_sum and sum(list_to_sum) > 21:
            list_to_sum.remove(11)
            list_to_sum.append(1)
            return sum(list_to_sum)
        else:
            return sum(list_to_sum)

def bj_or_user_over(user_sum, computer_sum):
    if computer_sum == 0:
        print("You lose! Computer has Blackjack!")
        restart_game()
    elif user_sum == 0:
        print("You win! You have Blackjack!")
        restart_game()
    elif user_sum > 21:
        print("You score went over! You lose")
        restart_game()


def score_compare(user_sum, computer_sum):
    if  computer_sum > 21:
        print("Computer score went over! You win")
        return False
    elif computer_sum == user_sum:
        print("It's a draw!")
        return False
    elif user_sum > computer_sum and computer_sum > 17:
        print("You win!")
        return False
    elif computer_sum > user_sum and computer_sum > 17:
        print("Computer wins! you lose")
        return False
    else:
        return True


###############################################################################
def start_game():
    inital_draw = 2
    user_cards = []
    computer_cards = []
    for c in range(inital_draw):
        user_cards.append(deal_card())
    for c in range(inital_draw):
        computer_cards.append(deal_card())

    user_sum = calculate_score(user_cards)
    computer_sum = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_sum}")
    print(f"Computer's first card is {computer_cards[0]}")
    bj_or_user_over(user_sum, computer_sum)

    can_continue_user = True
    while can_continue_user:
        user_choice = input("Do you want to draw another card? 'y' or 'n': ").lower()
        if user_choice == 'y':
            user_cards.append(deal_card())
            user_sum = calculate_score(user_cards)
            computer_sum = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_sum}")
            print(f"Computer's first card is {computer_cards[0]}")
            bj_or_user_over(user_sum, computer_sum)
        else:
            can_continue_user= False

    #computer's turn
    can_continue_computer = False
    if computer_sum < 17:
        can_continue_computer = True
    else:
        score_compare(user_sum, computer_sum)
    while can_continue_computer:
        computer_cards.append(deal_card())
        computer_sum = calculate_score(computer_cards)
        can_continue_computer = score_compare(user_sum, computer_sum)

    print(f"Your final hand: {user_cards}, final score: {user_sum}")
    print(f"Computers final hand: {computer_cards}, final score: {computer_sum}")
    restart_game()

start_game()
