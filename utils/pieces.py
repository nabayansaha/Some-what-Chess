# this file is to describe the pieces of the chess game

class pawn:
    def __init__(self, color, position=None): #pass the poisttion as a tuple (x, y)
        self.color = color
        self.name = 'pawn'
        self.on_board = True
        self.position = None, None

    def move(self):
        dx = [1]
        dy = [0]
        if self.color == 'black':
            dx = [-1]
        
        # update the position
        if self.position is not None:
            self.position = (self.position[0] + dx[0], self.position[1] + dy[0])
        else:
            self.position = None, None
    
    def attack(self):
        dx = [1, 1]
        dy = [-1, 1]
        if self.color == 'black':
            dx = [-1, -1]

        if self.position is not None:
            return [(self.position[0] + dx[0], self.position[1] + dy[0]), (self.position[0] + dx[1], self.position[1] + dy[1])]
        else:
            return None
        
class rook:
    def __init__(self, color, position=None): #pass the poisttion as a tuple (x, y)
        self.color = color
        self.name = 'rook'
        self.on_board = True
        self.position = None, None

    def move(self):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        if self.position is not None:
            return [(self.position[0] + dx[i], self.position[1] + dy[i]) for i in range(4)]
        else:
            return None
    
    def attack(self):
        return self.move()
    
class knight:
    def __init__(self, color, position=None): #pass the poisttion as a tuple (x, y)
        self.color = color
        self.name = 'knight'
        self.on_board = True
        self.position = None, None

    def move(self):
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]
        
        if self.position is not None:
            return [(self.position[0] + dx[i], self.position[1] + dy[i]) for i in range(8)]
        else:
            return None
    
    def attack(self):
        return self.move()

class bishop:
    def __init__(self, color, position=None): #pass the poisttion as a tuple (x, y)
        self.color = color
        self.name = 'bishop'
        self.on_board = True
        self.position = None, None

    def move(self):
        dx = [1, 1, -1, -1]
        dy = [1, -1, 1, -1]
        
        if self.position is not None:
            return [(self.position[0] + dx[i], self.position[1] + dy[i]) for i in range(4)]
        else:
            return None
    
    def attack(self):
        return self.move()
    
class queen:
    def __init__(self, color, position=None): #pass the poisttion as a tuple (x, y)
        self.color = color
        self.name = 'queen'
        self.on_board = True
        self.position = None, None

    def move(self):
        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]
        
        if self.position is not None:
            return [(self.position[0] + dx[i], self.position[1] + dy[i]) for i in range(8)]
        else:
            return None
    
    def attack(self):
        return self.move()
    
class king:
    def __init__(self, color, position=None): #pass the poisttion as a tuple (x, y)
        self.color = color
        self.name = 'king'
        self.on_board = True
        self.position = None, None

    def move(self):
        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]
        
        if self.position is not None:
            return [(self.position[0] + dx[i], self.position[1] + dy[i]) for i in range(8)]
        else:
            return None
    
    def attack(self):
        return self.move()
    