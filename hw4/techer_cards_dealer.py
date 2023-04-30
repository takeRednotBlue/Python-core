from random import randrange  # майже те саме що randint
from pprint import pprint


def create_deck():
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    for suit in suits:
        for value in values:
            deck.append(f'{value} of {suit}')
    return deck


def shuffle_deck(deck):
    new_deck = deck.copy()
    len_new_deck = len(new_deck)
    for i in range(len_new_deck):
        random_index = randrange(len_new_deck)
        new_deck[i], new_deck[random_index] = new_deck[random_index], new_deck[i]
    return new_deck


def deal(players, numbers_cards_of_player, deck):
    if players * numbers_cards_of_player > len(deck):
        print(f"Не вистачить карт!")
        return

    table = []
    for _ in range(numbers_cards_of_player):
        for player in range(players):
            if player >= len(table):
                # Додаємо гравця до столу
                table.append([deck.pop()])
            else:
                table[player].append(deck.pop())
    return table


def main():
    init_deck = create_deck()
    pprint(f'Нова колода: {init_deck}')
    deck = shuffle_deck(init_deck)
    print(f'Перемішана колода: {deck}')
    players = 7
    numbers_cards_of_player = 5
    table_deal = deal(players, numbers_cards_of_player, deck)
    for i in range(players):
        print(f"Карти гравця {i + 1} : {table_deal[i]}")

    print(f"Колода після роздачі: {deck}")


if __name__ == '__main__':
    main()
