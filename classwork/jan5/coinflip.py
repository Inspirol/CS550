import random

class Coin:
        
        def __init__(self, value):
            self.value = value
            self.flip()
            
        def flip(self):
            self.value = random.choice(['heads', 'tails'])
            
        def __str__(self):
            return self.value
        
class Player:
    
        
        def __init__(self, name):
            self.previous_results = []
            self.name = name
            self.coin = Coin('heads')
            
        def flip(self):
            self.coin.flip()
            self.previous_results.append(self.coin.value)
            
        def heads(self):
            return self.previous_results.count('heads') / len(self.previous_results)
            
        def __str__(self):
            return "{} has a coin showing {}".format(self.name, self.coin)
        
class Game:
    
    def __init__(self, players):
        self.players = players
        
    def play(self, num_flips=1):
        for player in self.players:
            for i in range(num_flips):
                player.flip()
                
            
    def __str__(self):
        return "\n".join([str(player) for player in self.players])
    
    def heads(self):
        return [player.heads() for player in self.players]
    
    
if __name__ == "__main__":
    players = [Player('Alice'), Player('Bob')]
    game = Game(players)
    game.play(10000)
    print(game)
    print(game.heads())