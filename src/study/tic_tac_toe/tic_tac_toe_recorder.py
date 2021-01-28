import numpy as np

class Turn:
    def __init__(self,start_symbol='O'):
        self.turn = start_symbol

    def change(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def current(self):
        return self.turn

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
        return board.empty_cells[np.random.randint(0, len(board.empty_cells))]

    def mark_occupied(self,cell,symbol):
        self.cells[cell] = symbol
        self.empty_cells.remove(cell)

    def print_board(self):
        print("")
        for row in self.cells:
            for column in row:
                print(column),
            print(" ")

def get_input():
    inp = input()

    value = inp % 10
    #print(value)
    inp = inp / 10
    y = inp % 10
    #print(y)
    x = inp / 10
    #print(x)
    return x-1,y-1,value*1.0

def get_next_input():
    inp = input()
    return (inp/10,inp%10)

#board = np.random.choice(['X','O','-'],size=(3,3))

    #print(tmp_board)

"""for i in range(9):
    #x,y,value = get_input()
    #board[x,y] = value
    #print(board)"""





won_map_O = dict({"0OO":0,"O0O":1,"OO0":2})
won_map_X = dict({"XXX":0,"XXX":1,"XXX":2})

won_maps = dict(O=won_map_O, X=won_map_X)

winnable_map_O = dict({"-OO":0, "O-O":1, "OO-":2})
winnable_map_X = dict({"-XX":0, "X-X":1, "XX-":2})

winnable_maps = dict(O=winnable_map_O, X=winnable_map_X)

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


def play(turn):

    finished = False

    my_symbol = turn.current()

    # Next is their turn
    turn.change()

    their_symbol = turn.current()


    print("Turn of:"+my_symbol)

    print("Checking if I can win in this turn")
    selected_cell = get_winning_position(my_symbol)
    if(selected_cell):
        print(my_symbol+" WON THE GAME!!! \n\n")
        finished = True

    if(not selected_cell):
        print("Checking if they can win in next turn")
        selected_cell = get_winning_position(their_symbol)
        if(selected_cell):
            print("Blocking them at position : "+str(selected_cell))

    if(not selected_cell):
        if(board.is_empty((1,1))):
            print("Taking central cell")
            selected_cell = (1,1)
        else:
            selected_cell = board.get_empty_corner()
            print("Taking corner "+str(selected_cell))

    if(not selected_cell):
            print("Selecting random cell")
            selected_cell = board.get_random_empty_cell()
            print("Random cell "+str(selected_cell))

    # Put the symbol and win
    if(selected_cell):
        board.mark_occupied(selected_cell,my_symbol)

    return finished


def get_winning_position(symbol):

    pos = (get_next_matching_position(winnable_maps[symbol], board.cells))
    print("horizontal position : " + str(pos))

    if (not pos):
        pos = get_next_matching_position(winnable_maps[symbol], board.cells.T)
        if(pos):
            pos=pos[::-1] # Transpose back to get correct position
        print("verticle position : " + str(pos))

    if (not pos):
        pos = get_next_matching_diagonal_position(winnable_maps[symbol], board.cells)
        print("Diagonal position : " + str(pos))

    return pos

board = Board()

board.print_board()

# init with a random initial value
# board[np.random.randint(0,3),np.random.randint(0,3)] = "-"

board.print_board()

def play_game(mode="auto"):
    turn = Turn('O')
    for i in range(9):
        if(mode!="auto"):
            pass
        if(play(turn)):
            print("GAME OVER")
            print(board)
            break
        board.print_board()

play_game()










