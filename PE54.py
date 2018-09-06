import time


class PlayingCard:
    def __init__(self, card=''):
        self.card = card
        self.value = self.card[0]
        self.suit = self.card[1]

        if self.value in '23456789':
            self.value = int(self.value)
        elif self.value == 'T':
            self.value = 10
        elif self.value == 'J':
            self.value = 11
        elif self.value == 'Q':
            self.value = 12
        elif self.value == 'K':
            self.value = 13
        elif self.value == 'A':
            self.value = 14

class PlayingHand:
    def __init__(self, hand=[PlayingCard] * 5):
        self.hand = hand
        self.vis_hand = ['{}{}'.format(card.value, card.suit) for card in self.hand]
        self.values = sorted([card.value for card in self.hand])
        self.suits = [card.suit for card in self.hand]
        self.high = 0
        self.pair = False
        self.two_pair = False
        self.three_kind = False
        self.straight = False
        self.flush = False
        self.full = False
        self.four_kind = False
        self.st_flush = False
        self.r_flush = False

        self.high_win = 0
        self.score = 0

        self.check_hand()


    def check_hand(self):
        self.high = max(self.values)

        for val in set(self.values):
            if self.values.count(val) == 2:
                if self.pair:
                    self.two_pair = True
                    self.score = 2
                    if val > self.high_win:
                        self.high_win = val
                else:
                    self.pair = True
                    self.score = 1
                    self.high_win = val

            if self.values.count(val) == 3:
                self.three_kind = True
                self.score = 3
                self.high_win = val

            if self.values.count(val) == 4:
                self.four_kind = True
                self.score = 7
                self.high_win = val

        if self.values[-1] - self.values[0] == 4 and len(set(self.values)) == 5:
            self.straight = True
            self.score = 4
            self.high_win = self.values[-1]

        if len(set(self.suits)) == 1:
            self.flush = True
            self.score = 5
            self.high_win = self.values[-1]

        if self.pair and self.three_kind:
            self.full = True
            self.score = 6
            self.high_win = self.values[-1]

        if self.straight and self.flush:
            self.st_flush = True
            self.score = 8
            self.high_win = self.values[-1]

        if self.st_flush and sum(self.values) == 60:
            self.r_flush = True
            self.score = 9
            self.high_win = self.values[-1]


def main():
    with open('p054_poker.txt', 'r') as raw:
        all_cards = raw.read().split('\n')

    p1_hands = []
    p2_hands = []
    for deal in all_cards[:-1]:
        cards = deal.split(' ')
        p1_hands.append(PlayingHand([PlayingCard(card) for card in cards[:5]]))
        p2_hands.append(PlayingHand([PlayingCard(card) for card in cards[5:]]))

    p1_wins = 0

    for i in range(len(p1_hands)):
        if p1_hands[i].score > p2_hands[i].score:
            p1_wins += 1

        elif p1_hands[i].score == p2_hands[i].score and p1_hands[i].score != 0:
            if p1_hands[i].high_win > p2_hands[i].high_win:
                p1_wins += 1

        elif p1_hands[i].score == 0 and p2_hands[i].score == 0:
            for k in range(4, -1, -1):
                if p1_hands[i].values[k] > p2_hands[i].values[k]:
                    p1_wins += 1
                    break
                elif p1_hands[i].values[k] < p2_hands[i].values[k]:
                    break
    print(p1_wins)


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
    