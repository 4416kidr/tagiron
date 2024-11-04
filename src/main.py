from enum import Enum
import random


class PlayColor(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3

class PlayCard:
    def __init__(self, color: PlayColor, number: int):
        self.color = color
        self.number = number
        self.validate()
    
    def validate(self):
        if isinstance(self.color, PlayColor) == False and isinstance(self.number, int) == False:
            raise ValueError('Invalid type')
        if self.number < 0 or self.number > 9:
            raise ValueError('Number must be between 0 and 9')
        if self.color == PlayColor.GREEN and self.number != 5:
            raise ValueError('Green cards must have number 5')
    
    def __repr__(self):
        return f"{self.color.name[0]}{self.number}"

class PlayDeck:
    def __init__(self):
        self.cards = [
            PlayCard(color, n) for n in range(10) for color in [PlayColor.RED, PlayColor.BLUE] if n != 5
        ]
        self.cards.append(PlayCard(PlayColor.GREEN, 5))
        self.cards.append(PlayCard(PlayColor.GREEN, 5))
        self.cards = sorted(self.cards, key=lambda x: x.number)
    def distribute(self, player: int):
        if player < 2 or player > 4:
            raise ValueError('Invalid number of players')
        temp_deck = self.cards[:]
        random.shuffle(temp_deck)
        hands = [[] for _ in range(player)]
        for _ in range(5):
            for i in range(player):
                hands[i].append(temp_deck.pop(0))
        hands = [sorted(hand, key=lambda x: (x.number, x.color.value)) for hand in hands]
        return hands

class GameMaster:
    def __init__(self):
        deck = PlayDeck()
        hands = deck.distribute(2)
        print(hands)
            

if __name__ == "__main__":
    master = GameMaster()
