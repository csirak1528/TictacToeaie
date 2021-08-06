import random
import load_data_
from frmt import ul

board = [['   |','  ','| '],['   |','  ','| '],['   |','  ','| ']]

def board_load():
    y = 0
    for i in board:
        y+=1
        if y<3:
            x = ''.join(i)
            print(ul(x))
        else:
            print(''.join(i))
                
    
   


taken = []
taken_comp = []

    
def update(taken, taken_comp):
    for i in taken:
        if i == 0:
            board[0][0] = ' X|'
        if i == 1:
            board[0][1] = ' X '
        if i == 2:
            board[0][2] = '| X'
        if i == 3:
            board[1][0]= ' X |'
        if i == 4:
            board[1][1]= ' X '
        if i == 5:
            board[1][2]= '| X'
        if i == 6:
            board[2][0]= ' X |'
        if i == 7:
            board[2][1]= ' X '
        if i == 8:
            board[2][2]= '| X'

    for i in taken_comp:
        if i == 0:
            board[0][0] = ' O |'
        if i == 1:
            board[0][1] = ' O'
        if i == 2:
            board[0][2] = '| O '
        if i == 3:
            board[1][0]= ' O |'
        if i == 4:
            board[1][1]= ' O '
        if i == 5:
            board[1][2]= '| O'
        if i == 6:
            board[2][0]= ' O |'
        if i == 7:
            board[2][1]= 'O '
        if i == 8:
            board[2][2]= '| O'
        if i == 9:
            continue
    board_load()


data = load_data_.data

for i in data:
    print(i)
    update(i,[])
    x = int(input('>>>'))
    board = [['   |','  ','| '],['   |','  ','| '],['   |','  ','| ']]
    i.append(x)
load_data_.data = data
