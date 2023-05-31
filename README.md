# wd_sprint3_war
This is a public repository to code a card game War (Turing College's Web Development program).

Card game War is played by two or more players with a 52 card deck:

    suits = "Hearts", "Spades", "Diamonds", "Clubs"
    ranks = "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"

At the start of the game, the deck is shuffled and divided between players.

Each player plays a face-up card (called "battle")

Who ever has a card with higher rank wins battle, and adds played cards into their deck (at the bottom)

If there's a tie in ranks, "war" is initiated:

    Each player plays a card face-down

    Each player plays a card face-up (same as in battle)

    Winner takes all cards, repeat on tie.

Player wins the game once they have collected all 52 cards.


## REQUIREMENTS


1) Project should be based on OOP paradigm.


2) Create a class Dealer, which will:

	a) Fill deck with the cards;
	b) Shuffle the deck (using random.shuffle())
    c) Deal the deck to players;
    

3) Create a class Player, which will have it's deck and name as an attributes. Object of class Player, should be able to:

	a) Draw and play a card from it's deck;

	b) Add won cards back to their deck.


4) Create a class GameCotroller, which will control the game flow:

	a) Initialize an object of Dealer class;

	b) Initialize 2 objects of Player class;

	c) Control the game loop (while True):

		* Initiate a battle (each player plays a card face-up, list.pop(0))

		* Check which player won (override comparison operator ">" with __gt__(self, other))

		* In case of a tie, initiate a war (each player plays a card face-down)

		* Check for game over state (someone won)

5) main() method should initialize object of class GameCotroller
