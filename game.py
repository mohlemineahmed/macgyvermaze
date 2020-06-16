import classes
from classes import *
pygame.init()
window = pygame.display.set_mode((window_size, window_size))
labyrinth = Maze('maze.txt')
labyrinth.generate()
continueGame= True
MacGyver = MacGyver(mcgyver_img, labyrinth)
compteurA = 0
continueMain = True
youwon = pygame.image.load(win_img).convert()
youlost = pygame.image.load(lose_img).convert()
while continueMain:
    startingMenu = pygame.image.load(titlescreen_img).convert()
    window.blit(startingMenu, (0, 0))
    pygame.display.flip()
    continueTitleScreen = True
    continueGame= True