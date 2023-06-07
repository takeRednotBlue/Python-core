class Gamer:
    def __init__(self, name, card):
        self.name = name
        self.card = card
        self.winner = False

    def check_winner(self):
        # check vertical lines of the card
        for col in self.card.values():
            if sum(col) == 0:
                self.winner = True
        
        # check horizontal lines of the card
        for i in range(self.card.limit_line):
            row = []
            for key in self.card:
                row.append(self.card[key][i])
            if sum(row) == 0:
                self.winner = True

    def mark_number(self, num):
        self.card.set_num_to_zero(num)
