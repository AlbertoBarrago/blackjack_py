# Blackjack game in py
import os
import random

from logo import logo


def getTotal(cards):
    total = 0
    for i in cards:
        total += i
    return total


def assignCard():
    if not player_bot_cards:
        clear()
        player_bot_cards.append(desk[random.randint(0, 12)])
    if not player_cards:
        player_cards.append(desk[random.randint(0, 12)])
        player_cards.append(desk[random.randint(0, 12)])


def clear():
    os.system('clear')


def assignRandomValueToBot(old_value):
    random_choice = random.random()
    new_value = old_value
    if random_choice > 0.5:
        # print('Computer take a card... ⚠️')
        new_value.append(desk[random.randint(0, 12)])
    return new_value


def restart_game(p_bot_cards, p_cards, p_score, p_bot_score):
    p_bot_cards = []
    p_cards = []
    p_score = 0
    p_bot_score = 0
    clear()
    print('Game restarted... 🔄')
    return {
        'p_bot_cards': p_bot_cards,
        'p_cards': p_cards,
        'p_score': p_score,
        'p_bot_score': p_bot_score,
    }


BLACKJACK_LIMIT = 21
desk = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
choose = input("Do you want to play a game of Blackjack 🂧 ? Type 'y' or 'n': ")
another_game = True

player_bot_cards = []
player_cards = []


def ask_for_restart():
    global player_score
    global player_bot_score
    global player_cards
    global player_bot_cards
    player_bot_score = 0
    player_score = 0
    player_cards = []
    player_bot_cards = []


while another_game:
    if choose == 'y':
        assignCard()
        player_score = getTotal(player_cards)
        player_bot_score = getTotal(player_bot_cards)

        print(f"Your card: {player_cards}, Your Score: {player_score}")
        print(f"Computer's card: {player_bot_cards}, Computer Score: {player_bot_score}")

        another_card = input("Do you want to draw another card? Type 'y' or 'n': ")
        if another_card == 'y':
            player_cards.append(desk[random.randint(0, 12)])
            player_score = getTotal(player_cards)

            player_bot_cards = assignRandomValueToBot(player_bot_cards)
            player_bot_score = getTotal(player_bot_cards)
        elif another_card == 'n':
            player_bot_cards = assignRandomValueToBot(player_bot_cards)
            player_bot_score = getTotal(player_bot_cards)

        if player_score > BLACKJACK_LIMIT or player_bot_score == BLACKJACK_LIMIT:
            print(f"You have busted from because your score is {player_score} > {BLACKJACK_LIMIT} 😭, "
                  f"or because the computer's score is {player_bot_score} has made blackjack 🤖")
            play_again = input("Do you want to play again? Type 'y' or 'n': ")
            if play_again == 'y':
                clear()
                ask_for_restart()
            else:
                print("You have chosen not to play a game of Blackjack")
                exit()
        elif player_score == BLACKJACK_LIMIT or player_bot_score > BLACKJACK_LIMIT:
            print(f"You win because {player_score} vs {player_bot_score} or have you made blackjack! 🚀")
            play_again = input("Do you want to play again? Type 'y' or 'n': ")
            if play_again == 'y':
                clear()
                ask_for_restart()
            else:
                print("You have chosen not to play a game of Blackjack")
                exit()
    else:
        another_game = False
        print("You have chosen not to play a game of Blackjack")
        exit()
