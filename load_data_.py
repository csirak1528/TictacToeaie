import random

combos = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]

data = [[7, 6, 1, 4], [7, 4, 5, 1], [0, 8, 7, 4], [8, 6, 4, 2], [4, 8, 0, 5, 9], [3, 2, 4], [3, 5, 8, 2, 9], [4], [7, 8, 3, 6], [4], [5, 1, 4, 6, 2], [1, 7, 5, 6, 8], [2, 7, 4], [1, 0, 2, 6, 9], [4], [2, 4], [6, 8, 3, 1, 0], [0, 7, 8, 6], [5, 8, 2], [4], [7, 3, 1, 8, 6], [4], [6, 5, 1, 2, 4], [4, 5, 0, 3, 9], [7, 4, 6, 2, 1], [4, 3, 0, 2, 6], [8, 3, 4], [7, 0, 4, 5, 1], [3, 5, 6, 1, 0], [8, 2, 5], [4], [8, 4, 1, 7], [4], [4], [0, 4], [4, 6, 7, 8, 9], [5, 3, 4], [4], [8, 0, 3, 6], [7, 5, 4], [4, 7], [5, 4, 0], [6, 1, 8], [0, 7], [4], [5], [6, 4, 8], [8, 5], [0, 2, 1], [2, 1, 0], [0, 1, 2], [3, 5, 4], [5, 4, 3], [3, 4, 5], [6, 8, 7], [8, 7, 6], [6, 7, 8], [0, 8, 4], [8, 4, 0], [0, 4, 8], [2, 6, 4], [6, 4, 2], [2, 4, 6], [0, 6, 3], [6, 3, 0], [0, 3, 6], [1, 7, 4], [7, 4, 1], [1, 4, 7], [2, 8, 5], [8, 5, 2], [2, 5, 8]]


def response(taken):
    for i in combos:
        x = 0
        for j in i:
            if j in taken:
                x+=1

moves =[]
for i in combos:
    moves.append([[i[0],i[2],i[1]],[i[2],i[1],i[0]],i])


for i in data:
    response(i)