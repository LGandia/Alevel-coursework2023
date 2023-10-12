
import pygame

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

spaceship = sprites.SpaceshipSprite()

# program_loop
program_running = True
while program_running:

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False
        if pygame.KEYDOWN == pygame.K_q:
            program_running = False


    # main menu and initialise new game

    bg_x=0
    bg_y=0
    speed = 0

    spaceship.x = (constants.SCREEN_WIDTH // 2) - (assets.spaceship_sprite_width // 2)
    spaceship.y = (constants.SCREEN_HEIGHT // 2) - (assets.spaceship_sprite_height // 2)

    spaceship.current_speed = spaceship.BASIC_SPEED

    spaceship.hitbox_left = spaceship.x + sprites.SPACESHIP_HITBOX_X_OFFSET
    spaceship.hitbox_top = spaceship.y + sprites.SPACESHIP_HITBOX_Y_OFFSET
    spaceship.rect = pygame.Rect(spaceship.hitbox_left, spaceship.hitbox_top, spaceship.HITBOX_WIDTH, spaceship.HITBOX_HEIGHT)

    
    # game loop
    game_running = True
    while program_running and game_running:

        # check for quit
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                program_running = False

        keys = pygame.key.get_pressed()
        spaceship.control(keys)
        spaceship.update ()
             
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

        # move and draw missiles
        
        for i in sprites.missiles_group:

            i.move()

            screen.blit(i.surface_to_draw, (i.x, i.y-15))
    
        #arrows
        if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_RIGHT]:
            screen.blit(assets.spaceship_2_surface, (spaceship.x, spaceship.y))
        else:
            screen.blit(assets.spaceship_1_surface, (spaceship.x, spaceship.y))
        #awsd
        if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_d]:
            screen.blit(assets.spaceship_2_surface, (spaceship.x, spaceship.y))
        else:
            screen.blit(assets.spaceship_1_surface, (spaceship.x, spaceship.y))
            
        pygame.display.flip()
        clock.tick(15)


print("goodbye")
