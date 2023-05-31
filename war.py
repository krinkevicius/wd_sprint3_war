import random

class Dealer:

    deck =[]
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.create_deck()
        self.shuffle(self.deck)
    

    def create_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append((rank, suit))

    def shuffle(self, deck):
        random.shuffle(deck)
    
    def deal_deck(self, i):
        print(type(len(self.deck)/2))
        print(len(self.deck)/2)
        deck = self.deck[(i-1)*int(len(self.deck)/2):i*int(len(self.deck)/2)]
        return deck

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def __str__(self):
        return self.name

    def play_card(self):
        self.card = self.deck.pop(0)
        return self.card

    def __gt__(self, other):

        if Dealer.ranks.index(self.card[0]) > Dealer.ranks.index(other.card[0]):
            return True
        else:
            return False
        
    def won(self):
        print(f"{self} won the battle")
        self.deck.extend(Table.cards_in_play)
        Table.cards_in_play = []
        input("Press Enter to continue")

class Table:

    players =[]
    cards_in_play = []
    def __init__(self):
        dealer = Dealer()
        player_index = 1 
        while player_index <= 2:
            name = input(f"Enter name for Player {player_index}: ")
            deck = dealer.deal_deck(player_index)
            player = Player(name,deck)
            print(player.name, player.deck)
            self.players.append(player)
            player_index += 1
        self.game_loop()

    def game_loop(self):
        while True:
            try:
                for player in self.players:
                    card = player.play_card()
                    print(card)
                    self.cards_in_play.append(card)

                if self.players[0] > self.players[1]:
                    self.players[0].won()
                elif self.players[1] > self.players[0]:
                    self.players[0].won()
                else:
                    print("tie")
                    self.war()
            except IndexError:
                    print("someone won the whole game")
                    break

            for player in self.players:
                print(len(player.deck))

    def war(self):
        for player in self.players:
            card = player.play_card()
            print(card)
            self.cards_in_play.append(card)


def main():
    table = Table()

if __name__ == "__main__":
    main()