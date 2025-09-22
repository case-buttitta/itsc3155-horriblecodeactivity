import random
class Game():
    def __init__(self):
        self.dimension = 3
        self.board = [" "] * 9
        self.playing = True
    def play(self,move):
        positions = move.split(",")
        self.board[positions[0]][positions[1]] = "X"
        while True:
            random_index = random.randrange(len(self.board))
            if self.board[random_index] == " ":
                self.board[random_index] = 'O'
                break
    def validate(self):
        self.playing = False



    def display_board(self):
        for row in range(0, len(self.board), 3):
            print("|".join(self.board[row:row+3]))




game = Game()
while game.playing:
    print("You are X")
    game.play(input("Your move in the format '1,2': "))
    game.display_board()



