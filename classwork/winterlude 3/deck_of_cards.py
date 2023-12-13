import random, math, getpass, time

class Card:
    
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", 
             "Jack", "Queen", "King", "Ace"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    
    rank: str
    suit: str
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)
    
    
class Deck:
    
    
    def __init__(self, style='standard'):
        self.style = style
        self.cards = []
        self.reset()
        
    def reset(self):
        self.cards = []
        for rank in Card.ranks:
            for suit in Card.suits:
                self.cards.append(Card(rank, suit))
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self):
        return self.cards.pop()
    
    
    def __str__(self):
        return "Deck of {} cards".format(len(self.cards))
    

class Hand:
    
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        self.cards.append(card)
        
    def __str__(self):
        return "Hand of {} cards".format(len(self.cards))
    
    
class Player:
    
    
    
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.played_cards = []
        self.card_slots_per_deal = 4
        
    def draw(self, deck):
        self.hand.add_card(deck.draw())
        
    def play(self, card):
        self.played_cards.append(card)
        self.hand.cards.remove(card)
        
        
    def gain_card_slot(self):
        self.card_slots_per_deal += 1
        
    def lose_card_slot(self):
        self.card_slots_per_deal -= 1
        
    def __str__(self):
        return "{} has {}".format(self.name, self.hand)
    
    
class Game:
    
    turn_per_deal = 3
    players: list[Player]
    
    def __init__(self, players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        for player in players:
            self.players.append(Player(player))
            
    def deal(self):
        for player in self.players:
            for i in range(player.card_slots_per_deal):
                player.draw(self.deck)
            
    def play(self):
        
        self.deal()
        
        
        dealing_turn = 0
        
        while len(self.players) > 1:
            print('-'*20)
            print('Dealing turn {}'.format(dealing_turn))
            print('-'*20)
            # if dealing turn is even, deal
            if dealing_turn % self.turn_per_deal == 0 and dealing_turn != 0:
                self.deal()
                dealing_turn += 1
                continue
            print('All players:')
            print('-'*20)
            for player in self.players:
                print(player)
                for i in range(len(player.hand.cards)):
                    print("{}".format(player.hand.cards[i])) 
                print(f'card slots: {player.card_slots_per_deal}')
                print('-'*20)
            print('Players now choose a card to play')
            print('-'*20)
            for player in self.players:
                self.player_turn(player)
                if len(player.hand.cards) == 0:
                    print('-'*20)
                    print("{} has no cards left and is out of the game".format(player.name))
                    print('-'*20)
                    time.sleep(1)
                    self.players.remove(player)
            if len(self.players) == 1:
                
                self.end_game()
                break
            self.turn_result()
            
            
    def __str__(self):
        return "Game with {} players".format(len(self.players))
    
    def player_choice_input(self, player):
        try:
            choice = int(getpass.getpass("Which card would you like to play? "))
            if choice < 0 or choice > len(player.hand.cards):
                raise ValueError("Choice must be between 1 and {}".format(len(player.hand.cards)))
            return choice - 1
        except ValueError as e:
            print(e)
            return self.player_choice_input(player)
    
    def player_turn(self, player):
        print(player)
        print("Your hand:")
        for i, card in enumerate(player.hand.cards):
            print("{}: {}".format(i + 1, card))            
        choice = self.player_choice_input(player)
        player.play(player.hand.cards[choice])
        
    def get_lowest_card(self, cards: list[Card]):
        lowest_card = cards[0]
        for card in cards:
            if Card.ranks.index(card.rank) < Card.ranks.index(lowest_card.rank):
                lowest_card = card
        return lowest_card
    
    
    def turn_result(self):
        print('-'*20)
        print('Turns over')
        print('-'*20)
        print("The table:")
        time.sleep(1)
        for player in self.players:
            print("{}: {}".format(player.name, player.played_cards[-1]))
            time.sleep(1)
        # get the lowest card value, and remove the number of cards the player can have by one
        time.sleep(3)
        lowest_card = self.get_lowest_card([player.played_cards[-1] for player in self.players])
        for player in self.players:
            if player.played_cards[-1] == lowest_card:
                player.lose_card_slot()
                print('-'*20)
                print("{} has lost a card slot for the remaining deals".format(player.name))
                print('-'*20)
                time.sleep(1)
        
        # print('All players:')
        # print('-'*20)
        # for player in self.players:
        #     print(player)
        #     print(f'card slots: {player.card_slots_per_deal}')
        #     print('-'*20)
        print('-'*20)
        print('Next turn')
        print('-'*20)
    
    
    def get_winner(self):
        return self.players[0]
    
    def end_game(self):
        print('-'*20)
        print('Game over')
        print('-'*20)
        print('The winner is {}'.format(self.get_winner().name))
        print('-'*20)
        print('Thanks for playing!')
        print('-'*20)
    
def add_players():
    players = []
    while True:
        player = input("Enter a player name, or type 'done' to finish: ")
        if player == 'done':
            if len(players) < 2:
                print("You must have at least 2 players")
                continue
            else:
                break
        players.append(player)
    return players
    
if __name__ == "__main__":
    players = add_players()
    game = Game(players)
    game.play()