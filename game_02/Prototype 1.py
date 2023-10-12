import pygame
import random

import constants
import assets
import sprites

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

#background
bg = pygame.image.load("assets/graphics/spaceground.png")
bg = pygame.transform.scale(bg,(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

assets.set_up_graphics()

# program_loop

program_running = True
while program_running:

    pygame.event.clear()

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False

    # draw the start menu
    screen.blit(assets.start_menu_surface, (0, 0))
    pygame.display.flip()

    # start menu loop
    start_menu = True
    while start_menu:

        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_menu = False
                program_running = False
            elif event.type == pygame.KEYDOWN:
                start_menu = False

    # initialise a new game

    bg_x=0
    bg_y=0
    speed = 0

    # game loop

    game_running = True
    pause = False
    while program_running and game_running:

        # check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_running = False


        # screen background

        speed = speed + 0.05 
        bg_x -= speed/2

        bg_x1 = -constants.SCREEN_WIDTH + bg_x
        screen.blit(bg, (bg_x1, bg_y))

        bg_x2 = bg_x1 + constants.SCREEN_WIDTH
        screen.blit(bg, (bg_x2, bg_y))

        bg_x += 0
        if bg_x < 0:
            bg_x += constants.SCREEN_WIDTH
        elif bg_x >= constants.SCREEN_WIDTH:
            bg_x -= constants.SCREEN_WIDTH


        pygame.display.flip()
        clock.tick(15)

print("goodbye")

