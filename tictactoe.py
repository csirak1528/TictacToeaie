import random
from frmt import ul
import tictacbrain as brain

def menu():
    global mode
    mode = int(input("What mode\n1:Single Player\n2:Two Player"))


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
                
    
   
xyz=0

taken = []
taken_comp = []

def turn(taken,taken_comp):
    x = int(input("What is your move? 0-8 : "))
    if x in taken or x in taken_comp:
        x = int(input("That spot is taken. What is your move? 0-8 : "))
    taken.append(x)
    if len(taken) == 1:
        y = brain.first(taken_comp)
    if len(taken) == 2:
        y = brain.second(taken_comp)
    if len(taken) == 3:
        y = brain.third(taken_comp)
    if len(taken) == 4:
        y = brain.fourth(taken_comp)

    xyz = 0
    for i in range(100):
        if y in taken or y in taken_comp:
            if i > 5:
                y = random.randint(0,8)
            elif len(taken) == 1:
                y = brain.first(taken_comp)
            elif len(taken) == 2:
                y = brain.second(taken_comp)
            elif len(taken) == 3:
                y = brain.third(taken_comp)
            elif len(taken) == 4:
                y = brain.fourth(taken_comp)
            

        
            

    taken_comp.append(y)

    

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
    board_load()
        
            
def win(taken,taken_comp):
    combos = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for i in combos:
        x = 0
        for j in i:
            if j in taken:
                x+=1
        if x >= 3:
            return "Player Wins"
    for i in combos:
        x = 0
        for j in i:
            if j in taken_comp:
                x+=1
        if x >= 3:
            return "Computer Wins"

board_load()
game = True
while game:
    turn(taken,taken_comp)
    update(taken, taken_comp)
    if win(taken, taken_comp) == "Computer Wins" or win(taken, taken_comp) == "Player Wins":
        print(win(taken, taken_comp))
        game == False
        break
 
