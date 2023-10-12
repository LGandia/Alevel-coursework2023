
import pygame

import assets


SPACESHIP_HITBOX_X_OFFSET = 36
SPACESHIP_HITBOX_Y_OFFSET = 40


class SpaceshipSprite(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.x = None
        self.y = None

        self.Y_CHANGE = 8

        self.BASIC_SPEED = 8

        self.SPEED_CHANGE = 2

        self.current_speed = None

        self.pic_number = None

        self.hitbox_left = None
        self.hitbox_top = None

        self.HITBOX_WIDTH = 80
        self.HITBOX_HEIGHT = 88

        self.rect = None


    def control(self, keys):

        # movement

        if keys[pygame.K_a]:
            self.current_speed -= self.SPEED_CHANGE

        elif keys[pygame.K_d]:
            self.current_speed += self.SPEED_CHANGE

        else:
            if self.current_speed < self.BASIC_SPEED:
                self.current_speed += self.SPEED_CHANGE
            elif self.current_speed > self.BASIC_SPEED:
                self.current_speed -= self.SPEED_CHANGE

        if keys[pygame.K_w]:
            self.y -= self.Y_CHANGE

        elif keys[pygame.K_s]:
            self.y += self.Y_CHANGE

        # update hitbox

        self.hitbox_left = self.x + SPACESHIP_HITBOX_X_OFFSET
        self.hitbox_top = self.y + SPACESHIP_HITBOX_Y_OFFSET

        self.rect.topleft = (self.hitbox_left, self.hitbox_top)

        # missiles

        # two keys at once

        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            missiles_group.add(MissileSprite(self.hitbox_left, self.hitbox_top, "south_east"))

        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            missiles_group.add(MissileSprite(self.hitbox_left, self.hitbox_top, "south_west"))

        elif keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            missiles_group.add(MissileSprite(self.hitbox_left, self.hitbox_top, "north_west"))

        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            missiles_group.add(MissileSprite(self.hitbox_left, self.hitbox_top, "north_east"))

        # one key

        elif keys[pygame.K_RIGHT]:
            missiles_group.add(MissileSprite(self.hitbox_left, self.hitbox_top, "east"))

        elif keys[pygame.K_DOWN]:
            missiles_group.add(MissileSprite(self.hitbox_left, self.hitbox_top, "south"))

        elif keys[pygame.K_LEFT]:
            missiles_group.add(MissileSprite(self.hitbox_left, self.hitbox_top, "west"))

        elif keys[pygame.K_UP]:
            missiles_group.add(MissileSprite(self.hitbox_left, self.hitbox_top, "north"))


class MissileSprite(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):

        super().__init__()

        self.x = x
        self.y = y

        self.direction = direction

        if self.direction == "east":
            self.surface_to_draw = assets.missile_e_surface

        elif self.direction == "south_east":
            self.surface_to_draw = assets.missile_se_surface

        elif self.direction == "south":
            self.surface_to_draw = assets.missile_s_surface

        elif self.direction == "south_west":
            self.surface_to_draw = assets.missile_sw_surface

        elif self.direction == "west":
            self.surface_to_draw = assets.missile_w_surface

        elif self.direction == "north_west":
            self.surface_to_draw = assets.missile_nw_surface

        elif self.direction == "north":
            self.surface_to_draw = assets.missile_n_surface

        else:
            self.surface_to_draw = assets.missile_ne_surface


    def move(self):

        if self.direction == "east":
            self.x += 20

        elif self.direction == "south_east":
            self.x += 20
            self.y += 20

        elif self.direction == "south":
            self.y += 20

        elif self.direction == "south_west":
            self.x -= 20
            self.y += 20

        elif self.direction == "west":
            self.x -= 20

        elif self.direction == "north_west":
            self.x -= 20
            self.y -= 20

        if self.direction == "north":
            self.y -= 20

        if self.direction == "north_east":
            self.x += 20
            self.y -= 20


spaceship_group = pygame.sprite.Group()
missiles_group = pygame.sprite.Group()


