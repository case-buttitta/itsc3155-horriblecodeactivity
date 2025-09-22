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
    def convert_one_dimensional(self,positions_list):
        return ((int(positions_list[0]) - 1) * 3) + (int(positions_list[1]) - 1)
    def play(self,move):
        positions = move.split(",")
        place = [int(n) for n in positions]
        if place[0] > 3 or place[1] > 3:
            print("Can't play there, pick another area")
            return False
        if self.board[place[0]-1][place[1]-1] != " ":
            print("Can't play there, pick another area")
            return False
        self.board[place[0] - 1][place[1] - 1] = "X"
        while True:
            random_index = [random.randrange(self.dimension),random.randrange(self.dimension)]
            if self.board[random_index[0]][random_index[1]] == " ":
                self.board[random_index[0]][random_index[1]] = 'O'
                break
        if self.validate("X") or self.validate("O"):
            self.playing = False
        return True
    def validate(self,player):
        if player == "X":
            person = 'you'
        else:
            person = "I"
        for row in self.board:
            if all(cell == player for cell in row):
                print(f'{person} won!')
                return True


            # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                print(f'{person} won!')
                return True


            # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            print(f'{person} won!')
            return True

        if all(self.board[i][2 - i] == player for i in range(3)):
            print(f'{person} won!')
            return True

        return False





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



