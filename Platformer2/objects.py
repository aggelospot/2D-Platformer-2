"""
Module for managing platforms.
"""
import pygame
import random
import constants
from sprites import Sprites

FLOOR =(116, 377, 388, 50)
AIR_PLAT=(351,88,162,59)
SMALL_PLAT=(340,198,148,35)
BAT=(158,20,128,69)
HOT_MAGMA=(16,139,298,43)
WITCH=(3,12,106,88)
HEART = (0,0, 38, 34)
PUMPKIN=(308,6,110,115)

class Harmful(pygame.sprite.Sprite):

    def __init__(self, enemies):
        pygame.sprite.Sprite.__init__(self)
        enemy_list = Sprites("bad_stuff.png")

        image = enemy_list.get_image(0, 0, 1, 1)
        color_switch = image.get_at((0, 0))

        self.image = enemy_list.get_image(enemies[0], enemies[1], enemies[2], enemies[3])
        self.image.set_colorkey(color_switch)

        self.rect = self.image.get_rect()


class Misc(pygame.sprite.Sprite):

    def __init__(self,misc):
        pygame.sprite.Sprite.__init__(self)
        misc_list = Sprites("heart2.png")

        image = misc_list.get_image(0, 0 ,1 , 1)
        color_switch = image.get_at((0,0))

        self.image = misc_list.get_image(misc[0], misc[1], misc[2], misc[3])
        self.image.set_colorkey(color_switch)

        self.rect = self.image.get_rect()

    def update(self):
        removed = False
        for misc in self.groups():
            if removed == False:
                self.remove(misc)


class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = Sprites("organic_tiles.png")
        image = sprite_sheet.get_image(0, 0, 1, 1)
        color_switch = image.get_at((0, 0))


        self.image = sprite_sheet.get_image(sprite_sheet_data[0], sprite_sheet_data[1], sprite_sheet_data[2], sprite_sheet_data[3])
        self.image.set_colorkey(color_switch)

        self.rect = self.image.get_rect()

class MovingHarmful(Harmful):
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        self.rect.x += self.change_x

        self.rect.y += self.change_y

        cur_pos_y = self.rect.y

        if cur_pos_y > self.boundary_bottom:
            self.rect.x = random.randint(100, 800)
            self.rect.y = random.randint(-1000, -200)
            if not self.player.lost:
                if self.change_y == 4:                      # if enemy is pumkin get +1 score
                    self.player.set_score(1)

        cur_pos = self.rect.x - self.level.world_shift

        if cur_pos < self.boundary_left:
            self.rect.x = constants.SCREEN_WIDTH + 380
            self.rect.y = random.randint(0, 500)
            if not self.player.lost:
                if self.change_x == -4:                    #if enemy is bat get +2 score
                    self.player.set_score(2)
                elif self.change_x == -8:                  #if enemy is witch get +4 score
                    self.player.set_score(4)


class MovingPlatform(Platform):
    change_x = 0
    change_y = 0
    distance = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way.  """
        self.rect.x += self.change_x

        collision = pygame.sprite.collide_rect(self, self.player)
        if collision:

            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        self.rect.y += self.change_y
        self.distance += 1

        collision = pygame.sprite.collide_rect(self, self.player)
        if collision:

            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom


        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        pos = self.rect.x - self.level.world_shift

        if pos < self.boundary_left or pos > self.boundary_right:
            self.player.level
            self.rect.x = constants.SCREEN_WIDTH + 388

