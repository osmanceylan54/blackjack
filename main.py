import random
import art

cards_dict = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "K": 10,
    "Q": 10,
    "J": 10,
    }
def random_card(number):
    the_list = []
    for item in range(number):
        the_list.append(random.choice(list(cards_dict.keys())))
    return the_list

def draw_card(cards, score):
    new_card = random_card(1)[0]
    cards.append(new_card)
    score += cards_dict[new_card]
    if new_card == "A" and score > 21:
        score -= 10
    return score

def main_body():
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()
    if play_game != "y":
        exit()
    print("\n" * 20)
    print(art.logo)

    user_cards = random_card(1)
    user_score = cards_dict[user_cards[0]]
    user_score = draw_card(user_cards, user_score)
    # user_score = cards_dict[user_cards[0]] + cards_dict[user_cards[1]]
    print(f"    Your cards are {', '.join(user_cards)}. Your current score is {user_score}")

    computer_cards = random_card(1)
    computer_score = cards_dict[computer_cards[0]]
    print(f"    Computer's first card is {computer_cards[0]}.")

    if user_score == 21:
        print("Win with a blackjack!")
        main_body()

    while user_score < 22:
        should_draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if should_draw_card == "y":
            user_score = draw_card(user_cards, user_score)
            print(f"    Your cards are {', '.join(user_cards)}. Your current score is {user_score}")
            if user_score > 21:
                print("You went over, you lose.")
                main_body()
        else:
            while computer_score <= 16:
                computer_score = draw_card(computer_cards, computer_score)
            print(f"  Your final hand is {', '.join(user_cards)}, final score is {user_score}.")
            print(f"  Computer's final hand is {', '.join(computer_cards)}, final score is {computer_score}.")
            if computer_score > 21:
                print("Opponent went over. You win.")
            elif computer_score > user_score:
                print("You lose.")
            elif computer_score == user_score:
                print("It's a draw.")
            else:
                print("You win")
            main_body()

main_body()
