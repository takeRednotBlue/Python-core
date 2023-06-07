from random import randint
from card import Card
from gamer import Gamer

class LotoGame:
    def __init__(self, gamers):
        self.gamers = gamers
        self.min_number = 1
        self.max_number = Card.numbers_per_letter * Card.limit_line
        self.winners = []
        self.draw_numbers = []
        self.progress = 0

    def start(self):
        while True:
            self.step_game()
            self.check_winners()
            if self.winners:
                break
        return self.progress, self.winners

    def step_game(self):
        while True:
            current_num = randint(self.min_number, self.max_number)
            if current_num not in self.draw_numbers:
                self.draw_numbers.append(current_num)
                break
            self.progress += 1
            for gamer in self.gamers:
                gamer.mark_number(current_num)
                gamer.check_winner()

    def check_winners(self):
        for gamer in self.gamers:
            if gamer.winner:
                self.winners.append(gamer)


if __name__ == '__main__':
    players_names = ['Oleksandr', 'Volodymyr', 'Roman', 'Andrii', 'Borys', 'Iryna', 'Serhii', 'Nissa', 'Krabat', 'Oleh', 'Oleksandra']

    gamers = []
    for name in players_names:
        card = Card()
        gamer = Gamer(name, card)
        gamers.append(gamer)

    game = LotoGame(gamers)
    # for gamer in gamers:
    #     print(gamer.name)
    #     gamer.card.pretty_info()
    quantity, winners = game.start()
    print(f"Кількість кроків {quantity}")
    print(f"Випавші номери {game.draw_numbers}")
    for winner in winners:
        print(f"Переможець {winner.name}")
        winner.card.pretty_info()