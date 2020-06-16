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