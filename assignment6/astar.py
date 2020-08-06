
from warnings import warn
import heapq

import sys
import sys
import re

import time
import subprocess
import binascii

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

    return Matrix, target, source, kingmode
    





# Credit for this: Nicholas Swift
# as found at https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2


class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f

def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def astar(maze, start, end, allow_diagonal_movement):


    count = 0;
    """
    Returns a list of tuples as a path from the given start to the given end in the given maze
    :param maze:
    :param start:
    :param end:
    :return:
    """

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = (len(maze[0]) * len(maze) // 2)

    # what squares do we search
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if allow_diagonal_movement:
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    # Loop until you find the end
    while len(open_list) > 0:
        
        count += 1
        

        outer_iterations += 1

        if outer_iterations > max_iterations:
          # if we hit this point return the path such as it is
          # it will not contain the destination
          warn("giving up on pathfinding too many iterations")
          return return_path(current_node), count 
 

        
        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)
        


        # Found the goal
        if current_node == end_node:

            return return_path(current_node), count

        # Generate children
        children = []
        
        for new_position in adjacent_squares: # Adjacent squares

            count += 1

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                count+=1

                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                count+=1

                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:


            count += 1
            

            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                count += 1
                
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                count+=1
                continue


            # Add the child to the open list
            heapq.heappush(open_list, child)
        
    warn("Couldn't get a path to destination")
    return None





def example( argv ,  print_maze = True):

    maze, target, source, kingmode = read_file(argv[1])
    
 
    
    print(kingmode)

    path, count = astar(maze, source, target, kingmode)

    if print_maze:
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

    print(path)

    return count


def main(argv):

    start_time = time.time()
    result =   example(argv) 
    time_taken = format(round((time.time() - start_time),9))
    result = {'astar':{'comparisons':result,'clock':time_taken}}

    print(result)

  

if __name__ == "__main__":
    main(sys.argv)

