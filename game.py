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
    while continueTitleScreen:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                continueTitleScreen = False
                continueMain = False
                continueGame= False
                pygame.quit()
                os._exit(0)
            elif event.type == KEYDOWN and event.key == K_RETURN:
                while continueGame:
                    for event in pygame.event.get():

                        if event.type == KEYDOWN:

                            if event.key == K_RIGHT:
                                MacGyver.deplacer('right')
                            elif event.key == K_LEFT:
                                MacGyver.deplacer('left')
                            elif event.key == K_UP:
                                MacGyver.deplacer('up')
                            elif event.key == K_DOWN:
                                MacGyver.deplacer('down')
                    labyrinth.display(window)
                    window.blit(MacGyver.move, (MacGyver.x, MacGyver.y))
                    if compteurA == 1:
                        MacGyver.move = pygame.image.load(
                            mcgyver1_img).convert_alpha()
                    elif compteurA == 2:
                        MacGyver.move = pygame.image.load(
                            mcgyver2_img).convert_alpha()
                    elif compteurA == 3:
                        MacGyver.move = pygame.image.load(
                            mcgyver3_img).convert_alpha()
                    if MacGyver.maze.structure[MacGyver.cell_y][MacGyver.cell_x] == 'A':
                        MacGyver.maze.structure[MacGyver.cell_y][MacGyver.cell_x] = '0'
                        compteurA += 1
                        print(
                            "YOU COLLECTED AN OBJECT : THE SERINGE. OJECTS COUNT = ", compteurA)
                    elif MacGyver.maze.structure[MacGyver.cell_y][MacGyver.cell_x] == 'B':
                        MacGyver.maze.structure[MacGyver.cell_y][MacGyver.cell_x] = '0'
                        compteurA += 1
                        print(
                            "YOU COLLECTED AN OBJECT : THE ETHER. OJECTS COUNT = ", compteurA)
                    elif MacGyver.maze.structure[MacGyver.cell_y][MacGyver.cell_x] == 'C':
                        MacGyver.maze.structure[MacGyver.cell_y][MacGyver.cell_x] = '0'
                        compteurA += 1
                        print(
                            "YOU COLLECTED AN OBJECT : THE TUBE. OJECTS COUNT = ", compteurA)
                    if MacGyver.maze.structure[MacGyver.cell_y][MacGyver.cell_x] == 'S' and compteurA == 3:
                        print(" YOU WIN")
                        continueGame= False
                        window.blit(youwon, (0, 0))
                        pygame.display.flip()
                        if event.type == KEYDOWN and event.key == K_ESCAPE:
                            pygame.quit()
                            os._exit(0)

                    elif MacGyver.maze.structure[MacGyver.cell_y][MacGyver.cell_x] == 'S' and compteurA < 3:
                        print("YOU LOOSE")
                        continueGame= False
                        window.blit(youlost, (0, 0))
                        pygame.display.flip()
                        if event.type == KEYDOWN and event.key == K_ESCAPE:
                            pygame.quit()
                            os._exit(0)

                    pygame.display.flip()
