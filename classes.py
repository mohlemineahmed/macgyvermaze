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
        
    def display(self, window):  # Pour afficher le labyrinthe après avoir run la fonction generate

        # These variables correspond to the pictures which will represent each texture of the labyrinth
        wall = pygame.image.load(wall_img)
        badguy = pygame.image.load(badguy_img)
        background = pygame.image.load(background_img)
        aiguille = pygame.image.load(a_img)
        ether = pygame.image.load(b_img)
        tube = pygame.image.load(c_img)
        # compteur pour les lignes (listes dans la liste principale)
        line_number = 0
        for line in self.structure:
            sprite_number = 0  # compteur pour chaque élément dans chaque ligne
            for sprite in line:
                x = sprite_number * sprite_size
                y = line_number * sprite_size
                if sprite == "W":
                    window.blit(wall, (x, y))
                elif sprite == "S":
                    window.blit(badguy, (x, y))
                elif sprite == "A":
                    window.blit(aiguille, (x, y))
                elif sprite == "B":
                    window.blit(ether, (x, y))
                elif sprite == "C":
                    window.blit(tube, (x, y))
                else:
                    window.blit(background, (x, y))
                sprite_number += 1
            line_number += 1

class MacGyver:
    def __init__(self, move, maze):

        self.cell_x = 0
        self.cell_y = 0
        self.x = 0
        self.y = 0
        self.move = pygame.image.load(mcgyver_img).convert_alpha()
        self.maze = maze
    def deplacer(self, move):

        if move == 'right':

            if self.cell_x < (15 - 1):

                if self.maze.structure[self.cell_y][self.cell_x+1] != 'W':

                    self.cell_x += 1

                    self.x = self.cell_x * sprite_size

        if move == 'left':
            if self.cell_x > 0:
                if self.maze.structure[self.cell_y][self.cell_x-1] != 'W':
                    self.cell_x -= 1
                    self.x = self.cell_x * sprite_size

        if move == 'up':
            if self.cell_y > 0:
                if self.maze.structure[self.cell_y-1][self.cell_x] != 'W':
                    self.cell_y -= 1
                    self.y = self.cell_y * sprite_size

        if move == 'down':
            if self.cell_y < (15 - 1):
                if self.maze.structure[self.cell_y+1][self.cell_x] != 'W':
                    self.cell_y += 1
                    self.y = self.cell_y * sprite_size
