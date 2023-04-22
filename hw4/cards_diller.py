"""
Створіть скрипт, який буде працювати, як картковий дилер. Для цього створіть методи для:
а) створення колоди карт ("10 of spades", "Jack of hearts", etc.)
б) перемішування колоди (можете використати метод random.randrange)
в) роздача карт (список гравців, кожен гравець має список карт)

В функції main() використайте ці методи та визначіть, скільки людей бере участь в грі і по скільки карт на людину 
роздавати. Передбачте сценарій, коли карт на всіх не вистачить. Додатково можна кількість гравців і карт на гравця 
передавати при виклику скрипта.

1. Створити колоду карт.
2. Перемішати її.
3. Роздати карти з колоди гравцям, щоб вони були унікальні та в колоді залишились карти окрім тих що у гравців.
4. Гравець має бути прив'язаний до списку карт.
5. Обмеження щодо кількості гравців та карт.
"""

from random import randrange, shuffle
import sys

"""
When invoking script enter at first number of players than number of cards per player.
"""

def create_deck() -> list:
    """
    Creates deck of 52 cards
    """
    # nominals = [str(i) for i in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    # suits = ["hearts", "clubs", "diamonds", "spades"]
    
    nominals = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
    # Uses UTF-8 codes to represent suits as symbols
    suits = [chr(0x2663), chr(0x2664), chr(0x2665), chr(0x2666)]

    cards_deck =[]
    for card in nominals:
        for suit in suits:
            # cards_deck.append(card + " of " + suit)
            cards_deck.append(card + suit)
    return cards_deck

def main ():
    try:
        players_num = int(sys.argv[1])
        cards_per_player = int(sys.argv[2])
    except ValueError:
        print("Invalid arguments. Integers are expected.")
    else:
        deck = create_deck()
        shuffle(deck)
        
        if players_num * cards_per_player <= len(deck):
            # Creates players dictionary to store hands values
            players = [f"Player №{num}" for num in range(1, players_num + 1)]
            hands = [list() for _ in range(players_num)]
            players_dic = dict(zip(players, hands))
            
            # Gives cards to all players
            for _ in range(cards_per_player):
                for player in players_dic:
                    players_dic[player].append(deck.pop())
            
            # Prints which hand each player has
            for player, hand in players_dic.items():
                print("{} has {}".format(player, hand))
        else:
            print(f"There is not enough cards for all players.")
        

if __name__ == "__main__":
    main()




