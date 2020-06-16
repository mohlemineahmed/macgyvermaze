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