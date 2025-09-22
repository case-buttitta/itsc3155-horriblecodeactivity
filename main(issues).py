import random
class Game():
    def __init__(self):
        self.dimension = 3 #number of dimensions
        self.board = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "],
        ]
        self.playing = True
    #function that does the code
    def play(self,move):
        positions = move.split(",")
        adjusted_positions = [int(n) for n in positions]
        if int(positions[0]) - 1 > 3 or int(positions[1]) - 1> 3 or self.board[adjusted_positions[0]-1][adjusted_positions[1]-1] != " ":
            print("Can't play there, pick another area")
            return False
        self.board[adjusted_positions[0] - 1][adjusted_positions[1] - 1] = "X"
        while True:
            random_index = [random.randrange(self.dimension),random.randrange(self.dimension)]
            if self.board[random_index[0]][random_index[1]] == " ":
                self.board[random_index[0]][random_index[1]] = 'O'
                break
        for row in self.board:
            print(f"|{"|".join(row)}|")
        #checks rows
        for row in self.board:
            if all(cell == 'X' for cell in row):
                print('You won!')
                return True
        #check columns
        for col in range(3):
            if all(self.board[row][col] == 'X' for row in range(3)):
                print('You won!')
                return True
        #check diagonals left to right
        if all(self.board[i][i] == 'X' for i in range(3)):
            print('You won!')
            return True
        #check diagonals right to left
        if all(self.board[i][2 - i] == 'X' for i in range(3)):
            print('You won!')
            return True
        #checks rows
        for row in self.board:
            if all(cell == 'O' for cell in row):
                print('I won!')
                return True
        #check columns
        for col in range(3):
            if all(self.board[row][col] == 'O' for row in range(3)):
                print('I won!')
                return True
        #check diagonals left to right
        if all(self.board[i][i] == 'O' for i in range(3)):
            print('I won!')
            return True
        #check diagonals right to left
        if all(self.board[i][2 - i] == 'O' for i in range(3)):
            print('I won!')
            return True
        return True




game = Game()
print("You are X")
while game.playing:
    gameplay = game.play(input("Your move in the format '1,2': "))
    if not gameplay:
        continue



