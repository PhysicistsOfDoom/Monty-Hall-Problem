import pygame
from classes import Door

#initialize
pygame.init()

#FPS
FPS = 60

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Screen, Caption, Logo
screen = pygame.display.set_mode((800,800))
screen_x, screen_y = screen.get_size()
pygame.display.set_caption("Monty Hall Probability")

#Variables
door1 = Door(400,400, "./media/DOOR OPEN.png", "./media/DOOR.png") #Object

#Game States
running = True
door_open = False

#Game Loop
while running:

    #Update Screen
    screen.fill(BLACK)

    #Input Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
        #Mouse check
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Check events
            if door1.rec.collidepoint(event.pos):
                door1.toggle(door_open)
                door_open = not door_open
                    

    # ---- GAME MECHANICS BELOW ----

            


    
    screen.blit(door1.image, door1.rec)





    #Update & FPS control
    pygame.time.Clock().tick(FPS)
    pygame.display.update()