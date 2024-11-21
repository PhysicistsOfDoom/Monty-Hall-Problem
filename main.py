import pygame

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
block = pygame.Surface((200, 200))
block.fill(WHITE)
block_rect = pygame.Rect(250, 250, 200, 200)

#Running
running = True


#Game Loop
while running:

    #Input Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
        #Mouse check
        if event.type == pygame.MOUSEBUTTONDOWN:
            if block_rect.collidepoint(event.pos):
                print("You clicked on the block!")

    # ---- GAME MECHANICS BELOW ----

            


    screen.blit(block, (250, 250))






    #Update & FPS control
    pygame.time.Clock().tick(FPS)
    pygame.display.update()