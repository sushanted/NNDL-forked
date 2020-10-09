import numpy as np

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


board = np.array([0.5]*9).reshape((3,3))

print(board)

for i in range(9):
    x,y,value = get_input()
    board[x,y] = value
    print(board)








