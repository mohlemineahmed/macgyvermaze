import pygame  # Import pygame
import constantes #Import the constants
import os #Import the os module
import random #Import the random module
from pygame.locals import *
from constantes import *

class Maze:

    def __init__(self, file):

        self.file = file

        self.structure = 0
    def generate(self):
        with open(self.file, 'r') as file:  # to read the file
            maze_structure = []  # Liste list which will contain each line in a list form
            for line in file:
                maze_line = []  # List for the lines
                for sprite in line:  # Pour each character in a line
                    if sprite != '\n':  # If the character is not a back to line
                        maze_line.append(sprite) # Adds the character to the maze_line list
                maze_structure.append(maze_line) # Adds the line as a list to maze_structure
            # To place the objects randomly
            randlist1 = random.choice(maze_structure)
            randindex1 = maze_structure.index(randlist1)
            randspace1 = [i for i, a in enumerate(randlist1) if a == "0"]
            randlist1[random.choice(randspace1)] = 'A'
            maze_structure[randindex1] = randlist1

            randlist2 = random.choice(maze_structure)
            randindex2 = maze_structure.index(randlist2)
            randspace2 = [i for i, a in enumerate(randlist2) if a == "0"]
            randlist2[random.choice(randspace2)] = 'B'
            maze_structure[randindex2] = randlist2

            randlist3 = random.choice(maze_structure)
            randindex3 = maze_structure.index(randlist3)
            randspace3 = [i for i, a in enumerate(randlist3) if a == "0"]
            randlist3[random.choice(randspace3)] = 'C'
            maze_structure[randindex3] = randlist3

        self.structure = maze_structure  # Sauvegarde
