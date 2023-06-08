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
        deck = self.deck[(i-1)*int(len(self.deck)/2):i*int(len(self.deck)/2)]
        return deck

class Player:
    def __init__(self, name, deck, i):
        if name == "":
            self.name = f"Player {i}"
        else:
            self.name = name
        self.deck = deck

    def __str__(self):
        return self.name

    def draw_card(self):
        self.card = self.deck.pop(0)
        Table.cards_in_play.append(self.card)

    def announce_card(self, face_side):
        # For regular battle, card are played face-up, annouce them:
        if face_side == "up":
            print(f"{self} put {self.card[0]} of {self.card[1]}.")
        # For war, cards are played face-down:
        else:
            print(f"{self} put a card face-down.")

    def __gt__(self, other):

        #Check which player has a card with a higher rank
        if Dealer.ranks.index(self.card[0]) > Dealer.ranks.index(other.card[0]):
            return True
        else:
            return False
        
    def won(self):
        print(f"{self} won the battle")

        # Shuffle cards in play before adding it to player's deck (should help to avoid infinite games)
        Dealer.shuffle(Dealer, Table.cards_in_play)
        self.deck.extend(Table.cards_in_play)

        # Remove all cards from cards_in_play
        Table.cards_in_play = []

        # User is asked to provide input in order to go to next round
        input("Press Enter to continue")

class Table:

    players =[]
    cards_in_play = []
    methods = [Player.draw_card, Player.announce_card]

    def __init__(self):

        # Create a dealer object
        dealer = Dealer()

        # Ask user for player's inputs and create player objects
        player_index = 1 
        while player_index <= 2:
            name = input(f"Enter name for Player {player_index}: ")
            deck = dealer.deal_deck(player_index)
            player = Player(name,deck,player_index)
            self.players.append(player)
            player_index += 1

        # Start the game loop
        self.game_loop()

    def game_loop(self):
        while True:
            try:

                # Each player goes into battle, they draw a card and then play it face-up:
                self.battle("up")

                # Check which player won a battle (or go to tie):
                if self.players[0] > self.players[1]:
                    self.players[0].won()
                elif self.players[1] > self.players[0]:
                    self.players[1].won()
                else:
                    print("War!")
                    self.battle("down")
            # IndexError is raised once one of the player's decks is empty:
            except IndexError:
                    for player in self.players:
                        # In a two player game, the player with non empty deck will win:
                        if len(player.deck) > 0:
                            print(f"{player} won the game!")
                    break


    # Both players need to try and draw a card from a deck before announcing it.
    # This is done to avoid the situation where one player plays a card, while other cannot do it.
    # If they are unable to draw a card because their deck is empty (IndexError is raised), the game is over
    def battle(self, face_side):
        for method in self.methods:
            for player in self.players:
                if method == Player.draw_card:
                    method(player)
                else:
                    method(player, face_side)


def main():
    table = Table()

if __name__ == "__main__":
    main()