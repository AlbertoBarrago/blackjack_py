import os
import random

from logo import logo


def clear():
    os.system('clear')


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
        for _ in range(2):
            player_cards.append(desk[random.randint(0, 12)])


def assignRandomValueToBot(old_value):
    random_choice = random.random()
    new_value = old_value
    if random_choice > 0.5:
        # print('Computer take a card... ⚠️')
        new_value.append(desk[random.randint(0, 12)])
    return new_value


def ask_if_restart():
    play_again = input("👾 Do you want to play again? Type 'y' or 'n': ")
    if play_again == 'y':
        clear()
        ask_for_restart()
    else:
        print("see you soon! 👋🏻")
        exit()


def ask_for_restart():
    global player_score, player_bot_score, player_cards, player_bot_cards
    player_bot_score = 0
    player_score = 0
    player_cards = []
    player_bot_cards = []


def handle_aces(cards):
    while 11 in cards and sum(cards) > BLACKJACK_LIMIT:
        cards.remove(11)
        cards.append(1)


def compute_score():
    if player_bot_score == BLACKJACK_LIMIT:
        print(f"You went over {BLACKJACK_LIMIT} 😭, "
              f"\n or because the computer's score is {player_bot_score} has made blackjack 🤖")
    elif player_score == BLACKJACK_LIMIT or player_bot_score > BLACKJACK_LIMIT:
        print(f"You win !!! 🚀")
        print(f"Your score is {player_score} and computer has {player_bot_score}")
    elif player_score > BLACKJACK_LIMIT:
        print('Game Over 😔, out of range')

    ask_if_restart()


def assign_card():
    global player_score, player_bot_cards, player_bot_score
    another_card = input("Do you want to draw another card? Type 'y' or 'n': ")
    if another_card == 'y':
        player_cards.append(desk[random.randint(0, 12)])
        player_score = getTotal(player_cards)

    player_bot_cards = assignRandomValueToBot(player_bot_cards)
    player_bot_score = getTotal(player_bot_cards)

    handle_aces(player_cards)
    handle_aces(player_bot_cards)


BLACKJACK_LIMIT = 21
desk = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
choose = input("Do you want to play a game of Blackjack 🂧 ? Type 'y' or 'n': ")
# vars
is_game_over = True
player_bot_cards = []
player_cards = []

while is_game_over:
    if choose == 'y':
        assignCard()
        player_score = getTotal(player_cards)
        player_bot_score = getTotal(player_bot_cards)

        print(f"Your card: {player_cards}, actual Score: {player_score}")
        print(f"Computer's card: {player_bot_cards}, computer Score: {player_bot_score}")

        assign_card()
        compute_score()
    else:
        is_game_over = False
        print("You have chosen not to play a game of Blackjack")
        exit()
