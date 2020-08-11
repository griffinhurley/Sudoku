import random


class Sudoku:

    def __init__(self):
        self.game = None
        self.solved = None

    def start_game(self):
        """ Starts a game"""
        self.game = [[0 for _ in range(9)] for _ in range(9)]
        self.__fill_board()
        self.__generate_game()
        for x in self.game:
            print(x)

    def __fill_board(self, idx=1):
        """Fills an empty self.game with a valid sudoku solution"""
        if idx > 81:
            return True
        i = (idx-1) // 9
        j = (idx-1) % 9
        possible = list(self.get_possible_values(i, j))
        if not possible:
            return False
        random.shuffle(possible)
        for legal_move in possible:
            self.game[i][j] = legal_move
            if self.is_valid():
                return True
            elif self.__fill_board(idx+1):
                return True
            self.game[i][j] = 0
        return False

    def __generate_game(self):
        """ Randomly removes values from filled sudoku board"""
        for i in range(9):
            for j in range(9):
                choice = random.randrange(1, 7)
                if choice <= 3:
                    continue
                else:
                    self.game[i][j] = 0

    def move(self, i, j, num):
        """ Places num on board at row i, column j"""
        self.game[i][j] = num
        for x in self.game:
            print(x)

    def is_valid(self):
        """ Checks whether a sudoku solution is valid"""
        complete = set(range(1, 10))
        # check rows are valid
        for row in self.game:
            if set(row) != complete:
                return False
        # check columns are valid
        for i in range(9):
            col = [self.game[i][j] for j in range(9)]
            if set(col) != complete:
                return False
        # check boxes
        for i in range(3):
            for j in range(3):
                box = self.game[i*3][j*3:j*3+3] + self.game[i*3+1][j*3:j*3+3] + self.game[i*3+2][j*3:j*3+3]
                if set(box) != complete:
                    return False
        return True

    def get_possible_values(self, i, j):
        """ Returns values that can be placed in ith column and jth row of board without violating sudoku rules"""
        possible = set(range(1, 10))
        remove = set(self.game[i]) | \
            {self.game[x][j] for x in range(9)} | \
            set(self.game[i // 3 * 3][j // 3 * 3:j // 3 * 3 + 3]) | \
            set(self.game[i // 3 * 3 + 1][j // 3 * 3:j // 3 * 3 + 3]) | \
            set(self.game[i // 3 * 3 + 2][j // 3 * 3:j // 3 * 3 + 3])
        possible -= remove
        return possible

    def solution(self):
        """Shows the solution to the game"""
        self.solve()
        for x in self.game:
            print(x)

    def solve(self, idx=1):
        """ Solves a game of sudoku using backtracking"""
        if idx > 81:
            return True
        i = (idx-1) // 9
        j = (idx-1) % 9

        if self.game[i][j] != 0:
            return self.solve(idx+1)

        for legal_move in self.get_possible_values(i, j):
            self.game[i][j] = legal_move
            if self.is_valid():
                return True
            elif self.solve(idx+1):
                return True
            self.game[i][j] = 0
        return False

