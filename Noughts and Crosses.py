class Board:
    def __init__(self):
        self.spaces = ["TL", "TM", "TR",
                       "ML", "MM", "MR",
                       "BL", "BM", "BR"]
        self.b = ""
        self.update()

    def update(self):
        self.b = f"""
      |      |      
  {self.spaces[0]}  |  {self.spaces[1]}  |  {self.spaces[2]}  
______|______|______
      |      |      
  {self.spaces[3]}  |  {self.spaces[4]}  |  {self.spaces[5]}  
______|______|______
      |      |      
  {self.spaces[6]}  |  {self.spaces[7]}  |  {self.spaces[8]}  
      |      |      
"""


class Player:
    def __init__(self, name, sym):
        self.name = name
        self.choice = None
        self.sym = sym


class Game:
    def __init__(self):
        # Initialise the board object
        self.board = Board()

        # Initialise the player objects
        self.p1 = Player("Player One", "O ")
        self.p2 = Player("Player Two", "X ")

        # Set the base variables
        self.currPlayer = self.p1
        self.winner = "No one"
        self.playing = True

    def main(self):

        print("Welcome to Noughts and Crosses!")  # Just a simple introductory statement

        # Loop until a player has won or all the spaces are used
        while self.playing and self.board.spaces.count("O ") < 5:
            self.action()

        print(f"{self.board.b}\n{self.winner} has won...")

    def action(self):
        while self.currPlayer.choice not in self.board.spaces:  # If the player hasn't entered a valid input the loop will continue

            self.currPlayer.choice = input(f"\nPlease choose a space {self.currPlayer.name}...{self.board.b}\n>>>").upper()

            if self.currPlayer.choice not in self.board.spaces:
                print("That is not an option.")

        self.update()

    def update(self):
        """ This method updates the position on the board with the player's symbol. """

        self.board.spaces = [space if space != self.currPlayer.choice else self.currPlayer.sym for space in self.board.spaces]
        self.currPlayer.choice = None  # resets the player's choice for the next round
        self.board.update()  # Updates the actual string that represents the board

        self.playing = not self.win_check()  # Checks if this player has won

        if self.playing:
            if self.currPlayer == self.p1:
                self.currPlayer = self.p2
            else:
                self.currPlayer = self.p1
        else:
            self.winner = self.currPlayer.name

    def win_check(self):
        """
        :return: True if there are three noughts or crosses in a line
        """
        return ((self.board.spaces[0] == self.currPlayer.sym and self.board.spaces[1] == self.currPlayer.sym and self.board.spaces[2] == self.currPlayer.sym) or  # across the top
                (self.board.spaces[3] == self.currPlayer.sym and self.board.spaces[4] == self.currPlayer.sym and self.board.spaces[5] == self.currPlayer.sym) or  # across the middle
                (self.board.spaces[6] == self.currPlayer.sym and self.board.spaces[7] == self.currPlayer.sym and self.board.spaces[8] == self.currPlayer.sym) or  # across the bottom
                (self.board.spaces[0] == self.currPlayer.sym and self.board.spaces[3] == self.currPlayer.sym and self.board.spaces[6] == self.currPlayer.sym) or  # down the left side
                (self.board.spaces[1] == self.currPlayer.sym and self.board.spaces[4] == self.currPlayer.sym and self.board.spaces[7] == self.currPlayer.sym) or  # down the middle
                (self.board.spaces[2] == self.currPlayer.sym and self.board.spaces[5] == self.currPlayer.sym and self.board.spaces[8] == self.currPlayer.sym) or  # down the right side
                (self.board.spaces[0] == self.currPlayer.sym and self.board.spaces[4] == self.currPlayer.sym and self.board.spaces[8] == self.currPlayer.sym) or  # diagonal
                (self.board.spaces[2] == self.currPlayer.sym and self.board.spaces[4] == self.currPlayer.sym and self.board.spaces[6] == self.currPlayer.sym))  # diagonal


if __name__ == '__main__':
    game = Game()
    game.main()
