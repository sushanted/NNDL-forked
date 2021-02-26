import numpy as np

class Board:
    def __init__(self):
        self.cells = np.full((3, 3), '-')
        self.empty_cells = [(i, j) for i in range(3) for j in range(3)]

    def is_empty(self, cell):
        return cell in self.empty_cells

    def get_empty_corner(self):
        for corner in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if self.is_empty(corner):
                return corner

    def get_random_empty_cell(self):
        return self.empty_cells[np.random.randint(0, len(self.empty_cells))]

    def mark_occupied(self,cell,symbol):
        self.cells[cell] = symbol
        self.empty_cells.remove(cell)

    def __str__(self):
        str = "\n"
        for row in self.cells:
            for column in row:
                str = str + column + " "
            str = str +"\n"
        return str


#board = np.random.choice(['X','O','-'],size=(3,3))

    #print(tmp_board)

"""for i in range(9):
    #x,y,value = get_input()
    #board[x,y] = value
    #print(board)"""


won_map_O = dict({"OOO":0})
won_map_X = dict({"XXX":0})

won_maps = dict(O=won_map_O, X=won_map_X)

winnable_map_O = dict({"-OO":0, "O-O":1, "OO-":2})
winnable_map_X = dict({"-XX":0, "X-X":1, "XX-":2})

winnable_maps = dict(O=winnable_map_O, X=winnable_map_X)


def play(game):

    my = game.current_player
    their = game.another_player
    print("Turn of:"+my.symbol)

    selected_cell = my.select_next_cell(game.board,my.symbol, their.symbol)

    # Put the symbol and win
    if(selected_cell):
        game.board.mark_occupied(selected_cell,my.symbol)

    if(get_winning_position(game.board.cells,won_maps,my.symbol)):
        print(my.symbol+ " INDEED WON THE GAME!!")
        return True

    return False

# TODO : use interface
class Player:

   def select_next_cell(self,board,my_symbol, their_symbol):
       pass

class HumanPlayer(Player):
    def select_next_cell(self, board, my_symbol, their_symbol):
        print("Select cell:")
        selected_cell = self.get_next_input()
        while(not self.is_valid(board,selected_cell)):
            print("Invalid value, select another cell:")
            selected_cell = self.get_next_input()
        print("Human player selected cell: "+str(selected_cell))
        return selected_cell

    def get_next_input(self):
        inp = input()
        return (inp / 10, inp % 10)

    def is_valid(self,board,cell):
        return cell[0]<3 and cell[1]<3 and board.is_empty(cell)

class RandomPlayer(Player):
    def select_next_cell(self, board, my_symbol, their_symbol):
        selected_cell =  board.get_random_empty_cell()
        print("Random player selected cell: "+str(selected_cell))
        return selected_cell

class BotPlayer(Player):

    def select_next_cell(self,board,my_symbol, their_symbol):

        print("Checking if I can win in this turn")
        selected_cell = get_winning_position(board.cells,winnable_maps, my_symbol)

        if (not selected_cell):
            print("Checking if they can win in next turn")
            selected_cell = get_winning_position(board.cells,winnable_maps, their_symbol)
            if (selected_cell):
                print("Blocking them at position : " + str(selected_cell))

        if (not selected_cell):
            if (board.is_empty((1, 1))):
                print("Taking central cell")
                selected_cell = (1, 1)
            else:
                selected_cell = board.get_empty_corner()
                print("Taking corner " + str(selected_cell))

        if (not selected_cell):
            print("Selecting random cell")
            selected_cell = board.get_random_empty_cell()
            print("Random cell " + str(selected_cell))

        return selected_cell

# TODO : can be moved to a separate class
def get_next_matching_position(pattern_map, cells):
    i = 0
    for row in cells:
        pattern = str.join('', row)
        if (pattern in pattern_map):
            return(i, pattern_map[pattern])
        i += 1
    return None

def get_next_matching_diagonal_position(pattern_map, cells):
    pattern = str.join('',cells.diagonal())
    if(pattern in pattern_map):
        return pattern_map[pattern],pattern_map[pattern]
    pattern = str.join('', [cells[i, 2-i] for i in range(0, 3)])
    if(pattern in pattern_map):
        return pattern_map[pattern],2-pattern_map[pattern]

def get_winning_position(cells,maps,symbol):

    pos = (get_next_matching_position(maps[symbol], cells))
    print("horizontal position : " + str(pos))

    if (not pos):
        pos = get_next_matching_position(maps[symbol], cells.T)
        if(pos):
            pos=pos[::-1] # Transpose back to get correct position
        print("verticle position : " + str(pos))

    if (not pos):
        pos = get_next_matching_diagonal_position(maps[symbol], cells)
        print("Diagonal position : " + str(pos))

    return pos

class Game:

    def __init__(self,player1,player2,board=Board()):
        self.board = board
        self.current_player = player1
        self.another_player = player2
        # default assignment, the first player will always get an extra chance than the second
        self.current_player.symbol = 'X'
        self.another_player.symbol = 'O'

    def change_turn(self):
        # swap current and another players
        current_player = self.current_player
        self.current_player = self.another_player
        self.another_player = current_player


def play_game(game):

    for i in range(9):

        if(play(game)):
            print("GAME OVER")
            print(game.board)
            break
        print(game.board)
        game.change_turn()

    if i==8:
        print("GAME OVER WITH A DRAW")


# TODO take input the types of two players : Bot, Random, Human
play_game(Game(RandomPlayer(),HumanPlayer()))















