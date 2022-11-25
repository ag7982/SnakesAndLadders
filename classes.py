import random


class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.position = 0
        self.rank = 0
    
    def update_position(self, pos):
        self.position = pos
    
    def get_name(self):
        return self.name



class GameBoard:
    def __init__(self, n):
        self.size = n
        self.board = [i for i in range(n)]

class Snake:
    def __init__(self, snakes_dict = None):
        self.snakes = {}
        if isinstance(snakes_dict, dict):
            self.snakes = snakes_dict
    
    def add_snake(self, start, end):
        self.snakes[start] = end
    
    def get_dict(self):
        return self.snakes

class Ladder:
    def __init__(self, ladders_dict = None):
        self.ladders = {}
        if isinstance(ladders_dict, dict):
            self.ladders = ladders_dict
    
    def add_ladder(self, start, end):
        self.ladders[start] = end
    
    def get_dict(self):
        return self.ladders
        
class Dice:
    def __init__(self, n):
        self.num_dices = n
        self.min = n
        self.max = 6*n
    
    def roll_dice(self):
        return random.randint(self.min, self.max)

class Game:
    def __init__(self, player_names, size_board, num_dice, snakes_dict, ladder_dict):
        
        id = 0
        self.queue = []
        for name in player_names:
            p = Player(name, id)
            id+=1
            
            self.queue.append(p)
        
        if len(player_names) == 0:
            raise ValueError("Number of players should be atleast 1")
        
        self.board = GameBoard(size_board)
        self.dice = Dice(num_dice)

        snakes = Snake(snakes_dict)
        self.snakes = snakes.get_dict()
        ladder = Ladder(ladder_dict)
        self.ladders = ladder.get_dict()

        self.pos = [0 for i in range(len(player_names))]
        self.win = []
    
    def check_snakes_and_ladders(self, snakes_dict, ladders_dict):
        for i in snakes_dict:
            if i in ladders_dict:
                raise RuntimeError(f"Found both snake and ladder at the same position {i}")
        
        if min(snakes_dict.values()) < 0 or min(snakes_dict.keys()) < 0:
            raise ValueError("Snakes dictionary values out of range, found negative value.")
        if max(snakes_dict.keys()) > self.board.size:
            raise ValueError("Snakes dictionary values out of range.")
        if max(ladders_dict.keys()) > self.board.size or max(ladders_dict.values()) > self.board.size:
            raise ValueError("Ladders dictionary values out of range")
        if min(ladders_dict.values()) < 0 or min(ladders_dict.keys()) < 0:
            raise ValueError("Ladders dictionary values out of range, found negative value.")
        return
    
    def play(self):
        
        while self.queue:
            cur_player = self.queue.pop(0)
            move = self.dice.roll_dice()
            print(f"{cur_player.name} rolls a value of {move}")
            old_pos = self.pos[cur_player.id]
            if old_pos + move > self.board.size:
                self.queue.append(cur_player)
            elif old_pos + move < self.board.size:
                new_pos = old_pos+move
                while new_pos in self.snakes:
                    new_pos = self.snakes[new_pos]
                    print(f"{cur_player.name} found snake, moved to {new_pos}")
                while new_pos in self.ladders:
                    new_pos = self.ladders[new_pos]
                    print(f"{cur_player.name} found ladder, moved to {new_pos}")
                
                self.pos[cur_player.id] = new_pos
                print(f"{cur_player.name} reached {new_pos}")
                self.queue.append(cur_player)

            else:
                print(f"{cur_player.name} reached the top.")
                self.win.append(cur_player.name)

        print("Ranks", self.win)
    







        

