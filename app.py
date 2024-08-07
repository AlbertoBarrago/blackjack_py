# Blackjack game in py
import random

from logo import logo


def getTotal(cards):
    total = 0
    for i in cards:
        total += i
    return total


def hasWin(cards):
    if getTotal(cards) == BLACKJACK_LIMIT:
        return True
    else:
        return False


def assignRandomValueToBot(old_value):
    random_choice = random.random()
    new_value = old_value
    if random_choice > 0.5:
        print('Computer take a card...')
        new_value.append(desk[random.randint(0, 12)])
    else:
        print('Computer pass...')
    return new_value


BLACKJACK_LIMIT = 21
desk = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
choose = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
another_game = True

player_bot_cards = []
player_cards = []

while another_game:
    if choose == 'y':

        player_bot_score = 0
        player_score = 0

        if not player_bot_cards:
            player_bot_cards.append(desk[random.randint(0, 12)])
        if not player_cards:
            player_cards.append(desk[random.randint(0, 12)])
            player_cards.append(desk[random.randint(0, 12)])

        player_score = getTotal(player_cards)
        player_bot_score = getTotal(player_bot_cards)

        print(f"Your card: {player_cards}, Your Score: {player_score}")
        print(f"Computer's card: {player_bot_cards}")

        another_card = input("Do you want to draw another card? Type 'y' or 'n': ")

        if another_card == 'y':
            player_cards.append(desk[random.randint(0, 12)])
            player_score = getTotal(player_cards)
            if player_score > BLACKJACK_LIMIT:
                print(f"You have busted from {player_score}")
                print("You lose")
                exit()
            elif player_score == BLACKJACK_LIMIT:
                print("You have got Blackjack")
                print("You win")
                exit()
        elif another_card == 'n':
            player_bot_cards = assignRandomValueToBot(player_bot_cards)
            player_bot_score = getTotal(player_bot_cards)
            if player_bot_score > BLACKJACK_LIMIT:
                print(f"Computer has busted from {player_bot_score}")
                print("You win")
                exit()
            elif player_bot_score == BLACKJACK_LIMIT:
                print(f"Computer has got Blackjack with {player_bot_cards}")
                print("You lose")
                exit()
    else:
        another_game = False
        print("You have chosen not to play a game of Blackjack")
        print("Thank you for playing")
        exit()
