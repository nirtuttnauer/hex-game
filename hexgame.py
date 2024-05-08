'''
This Was Authored by:
    - Nir Tuttnauer
    - Tomer Mizrahi
'''

from disjoint_set import DisjointSet

class HexGame:
    """
    Represents a game of Hex.

    Attributes:
        n (int): The size of the game board.
        winner (str): The winner of the game ('red', 'blue', or None if no winner yet).
        board (list): The game board represented as a 2D list.
        cells (list): The list of all cells on the game board.
        top_node (tuple): The top node used for the red player's disjoint set.
        bottom_node (tuple): The bottom node used for the red player's disjoint set.
        left_node (tuple): The left node used for the blue player's disjoint set.
        right_node (tuple): The right node used for the blue player's disjoint set.
        ds_red (DisjointSet): The disjoint set for the red player.
        ds_blue (DisjointSet): The disjoint set for the blue player.
    """

    def __init__(self, n=11):
        """
        Initializes a HexGame object.

        Args:
            n (int, optional): The size of the game board. Defaults to 11.
        """
        self.n = n
        self.winner = None
        self.board = [[0]*n for _ in range(n)]
        self.cells = [(i, j) for i in range(n) for j in range(n)]
        self.top_node = (-1, 0)
        self.bottom_node = (n, 0)
        self.left_node = (0, -1)
        self.right_node = (0, n)
        self.ds_red = DisjointSet(self.cells + [self.top_node, self.bottom_node])
        self.ds_blue = DisjointSet(self.cells + [self.left_node, self.right_node])
        self._initialize_game()

    def _initialize_game(self):
        """
        Initializes the game by setting up the initial state of the disjoint sets.
        """
        for i in range(self.n):
            self.ds_red.union((0, i), self.top_node)
            self.ds_red.union((self.n-1, i), self.bottom_node)
            self.ds_blue.union((i, 0), self.left_node)
            self.ds_blue.union((i, self.n-1), self.right_node)

    def play(self, i, j, player):
        """
        Makes a move in the game.

        Args:
            i (int): The row index of the cell to play.
            j (int): The column index of the cell to play.
            player (str): The player making the move ('red' or 'blue').

        Raises:
            AssertionError: If the cell is out of bounds or already occupied.
        """
        assert 0 <= i < self.n and 0 <= j < self.n and self.board[i][j] == 0
        self._make_move(i, j, player)
        self._check_winner(player)

    def _make_move(self, i, j, player):
        """
        Makes a move on the game board.

        Args:
            i (int): The row index of the cell to play.
            j (int): The column index of the cell to play.
            player (str): The player making the move ('red' or 'blue').
        """
        code = 1 if player == 'red' else 2
        self.board[i][j] = code
        for nei_i, nei_j in self._get_neighbors(i, j):
            if 0 <= nei_i < self.n and 0 <= nei_j < self.n and code == self.board[nei_i][nei_j]:
                self._union_cells(player, (nei_i, nei_j), (i, j))
        self._print_board()

    def _union_cells(self, player, cell1, cell2):
        """
        Unions two cells in the appropriate disjoint set.

        Args:
            player (str): The player making the move ('red' or 'blue').
            cell1 (tuple): The first cell to union.
            cell2 (tuple): The second cell to union.
        """
        if player == 'red':
            self.ds_red.union(cell1, cell2)
        else:
            self.ds_blue.union(cell1, cell2)

    def _check_winner(self, player):
        """
        Checks if the current player has won the game.

        Args:
            player (str): The player making the move ('red' or 'blue').
        """
        if player == 'red':
            if self.ds_red.find(self.top_node) == self.ds_red.find(self.bottom_node):
                self.winner = 'red'
        else:
            if self.ds_blue.find(self.left_node) == self.ds_blue.find(self.right_node):
                self.winner = 'blue'

    def _get_neighbors(self, i, j):
        """
        Returns the neighbors of a given cell.

        Args:
            i (int): The row index of the cell.
            j (int): The column index of the cell.

        Returns:
            list: A list of tuples representing the neighbors of the cell.
        """
        return [(i+1, j), (i+1, j-1), (i, j+1), (i, j-1), (i-1, j), (i-1, j+1)]

    def _print_board(self):
        """
        Prints the current state of the game board.
        """
        print(*self.board, sep='\n')
        print('\n')

def main():
    game = HexGame(11)
    player = 'red'
    winner = None
    while winner is None:
        user_input = input(f"{player} player's turn. Enter i j: ")
        coords = user_input.split()
        if len(coords) != 2:
            print("Invalid input. Please enter two integers separated by a space.")
            continue
        try:
            i, j = map(int, coords)
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue
        game.play(i, j, player)
        winner = game.winner
        if winner is not None:
            print(f"{winner} player wins!")
        player = 'red' if player == 'blue' else 'blue'

if __name__ == '__main__':
    main()