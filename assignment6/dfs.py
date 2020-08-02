





import numpy as np
import queue
import time
import sys

import collections




import pprintpp
import pprint
import codecs


def read_file(filepath):
    with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as txt:

        raw_txt = txt.read()
        
    raw_txt = raw_txt.upper()
    raw_txt.replace(' ','')
    raw_txt = raw_txt.strip()
    

    matrix = {}

    p = []
    m = raw_txt.split('\n')
    
    print(m)

    for i in m:
        x = i.split('=')

        value = x[1] 
        
        matrix = {x[0]:value}
        # print(matrix)
        p.append(matrix)

    width = 0
    height = 0
    source = 0
    target = 0
    kingmode = False

    person = []
    for i in range(len(p)):

        if 'WIDTH' in p[i].keys():
            
            # print("v",p[i]["WIDTH"])
            width =   p[i]["WIDTH"]

        elif 'HEIGHT' in p[i].keys():
            # print("v",p[i]["HEIGHT"])
            height =  p[i]["HEIGHT"]

        elif 'SOURCE' in p[i].keys():
            # print("v",p[i]["SOURCE"])
            source = p[i]["SOURCE"]

            source = source.split(',')
            # print(source)
            source = (int(source[0]),int(source[1]))


        elif 'TARGET' in p[i].keys():
            # print('v',p[i]['TARGET'])
            target = p[i]['TARGET']
            target = target.split(',')
            # print(target)
            target = (int(target[0]),int(target[1]))

        elif 'KINGMODE' in p[i].keys():
            # print('v',p[i]['KINGMODE'])
            kingmode = p[i]['KINGMODE'].strip()
            
            if kingmode == 'TRUE':
                kingmode =True
            else:
                 kingmode =False
            
        
            

        elif "PERSON" in p[i].keys():
            # print("v",p[i]["PERSON"])s
            

            person.append(p[i]['PERSON'])
###
    width = int(width)+1
    height = int(height)+1


    

    Matrix = [[0 for x in range(height)] for y in range(width)]



    # pprint.pprint(Matrix)

    for i in range(len(person)):

        man  = person[i].split(',')
        x =  int(man[0])
        y =  int(man[1])
        Matrix[x-1][y-1] = 1 






    pprint.pprint(Matrix)

    return Matrix, target, source, kingmode, width, height,target






grid, target, source, kingmode, width, height, target = read_file(sys.argv[1])

print(target[0])

grid[target[0]][target[1]] = 9

print('v',grid[1][2])
pprint.pprint(grid)


def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < height  and 0 <= y2 <  width and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

wall, clear, goal = 1, 0, 9



path = bfs(grid, (0, 0))

print(path)

maze = grid

   
for step in path:
    maze[step[0]][step[1]] = 2

for row in maze:
    line = []
    for col in row:
        if col == 1:
            line.append("p")
        elif col == 0:
            line.append("-")
        elif col == 2:
            line.append("*")
    print("".join(line))

 