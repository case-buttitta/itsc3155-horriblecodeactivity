import random
class Game():
    def __init__(self):
        self.dimension = 3
        self.board = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "],
        ]
        self.playing = True
    #function to make player move, checking if possible forst or if proposed position is on the board
    def play(self,move):
        positions = move.split(",")
        adjusted_positions = [int(n) for n in positions]
        place = self.board[adjusted_positions[0]-1][adjusted_positions[1]-1]
        if adjusted_positions[0] > 3 or adjusted_positions[1] > 3 or place != " ":
            print("Can't play there, pick another area")
            return False
        place = "X"
        return True
    #computer picks a random avilable spot, being the second to go it then validates whether either have won yet
    def respond(self):
        while True:
            random_index = [random.randrange(self.dimension),random.randrange(self.dimension)]
            if self.board[random_index[0]][random_index[1]] == " ":
                self.board[random_index[0]][random_index[1]] = 'O'
                break
        if self.validate("X") or self.validate("O"):
            self.playing = False
        return True
    #checks for winning combinations along rows, columns, and diagonals
    def validate(self,player):
        if player == "X":
            person = 'you'
        else:
            person = "I"
        #checks rows
        for row in self.board:
            if all(cell == player for cell in row):
                print(f'{person} won!')
                return True
        #check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                print(f'{person} won!')
                return True
        #check diagonals left to right
        if all(self.board[i][i] == player for i in range(3)):
            print(f'{person} won!')
            return True
        #check diagonals right to left
        if all(self.board[i][2 - i] == player for i in range(3)):
            print(f'{person} won!')
            return True

        return False
    #used to pretty print the board
    def display_board(self):
        for row in self.board:
            print(f"|{"|".join(row)}|")




game = Game()
print("You are X")
while game.playing:
    gameplay = game.play(input("Your move in the format '1,2': "))
    if not gameplay:
        continue
    game.display_board()



