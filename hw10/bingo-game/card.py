from random import randint, sample
from collections import UserDict

class Card(UserDict):
    numbers_per_letter = 15
    limit_line = 5
    loto_fields = ['B', 'I', 'N', 'G', 'O']

    def __init__(self):
        super().__init__()
        self.start_num = 1
        # end num is 16 so to use it end as param in range
        self.end_num = self.start_num + self.numbers_per_letter 
        self.create_card()

    def create_card(self):
        for letter in self.loto_fields:
            self.data[letter] = sample(range(self.start_num, self.end_num), k=self.limit_line)
            self.start_num = self.end_num
            self.end_num = self.start_num + self.numbers_per_letter

    def pretty_info(self):
        # *self.data - unpack dict keys to a function
        print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*self.data))
        for i in range(self.limit_line):
            line = []
            for letter in self.loto_fields:
                line.append(self.data[letter][i])
            print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*line))

    def set_num_to_zero(self, num):
        for key, line in self.data.items():
            self.data[key] = list(map(lambda x: 0 if x == num else x, line))


if __name__ == '__main__':
    card = Card()
    print(card)
    card.pretty_info()
