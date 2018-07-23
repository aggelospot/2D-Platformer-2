"""
Module for managing platforms.
"""
import pygame
import random
import constants
from game import Game
from sprites import Sprites
from entity import Entity

FLOOR = (0,416,480,32)
SMALL_PLAT=(575,512,161,32)
PLATFORM_DARK_GREY = (865, 385, 256, 31)
PLATFORM_DARK_GREY_2 = (865, 418, 256, 31)
PLATFORM_GREY_SMALL = (830, 64, 96, 32)
BOX_S_STRIPPED = (160, 128, 65, 63)
BOX_B_STRIPPED = (577, 256, 96, 96)
BACKGROUND_W_STAIRS = (0, 192, 322, 258)
BACKGROUND_BLACK_W_WINDOWS = (0, 448, 574, 255)
BACKGROUND_BLACK_BOXES = (738,127,384,128)
BAT=(158,20,128,69)
SPIKES = (2,80,128,15)
SPIKES_V = (434, 0, 15, 128)
CHAINS =  (1121, 1, 23, 104)
INV_OBSTACLE = (320, 0, 46, 408)
HEART = (0,0, 48, 48)


class Harmful(Entity):

    def __init__(self, enemies):
        pygame.sprite.Sprite.__init__(self)
        enemy_list = Sprites("spikez.png")

        image = enemy_list.get_image(0, 0, 1, 1)
        color_switch = image.get_at((0, 0))

        self.image = enemy_list.get_image(enemies[0], enemies[1], enemies[2], enemies[3])
        self.image.set_colorkey(color_switch)

        self.rect = self.image.get_rect()

class Bat(Entity):

    walkright = []
    walkleft = []


    def __init__(self, x, y, xvel):
        Entity.__init__(self)
        # Create Surface Area
        self.image = pygame.Surface((90, 90), pygame.SRCALPHA)
        self.rect = pygame.Rect(0, 0, 80, 80)


        # Initialize variables
        self.xvel = xvel
        self.yvel = 0
        self.rect.x = x
        self.rect.y = y
        self.boundary_left = 0
        self.boundary_right = 1000

        # States
        self.onGround = False
        self.airborne = True
        self.destroyed = False
        self.faceright = True
        self.counter = 0

        # Load Sprites
        sprites = Sprites("bat8.png")
        image = sprites.get_image(15, 9, 67, 73)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.walkleft.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walkright.append(image)

        sprites = Sprites("bat9.png")
        image = sprites.get_image(18, 11, 73, 69)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.walkleft.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walkright.append(image)

        sprites = Sprites("bat10.png")
        image = sprites.get_image(20, 26, 59, 35)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.walkleft.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walkright.append(image)

    def update(self, platforms, projectiles, player):

        #self.calc_grav()
        '''
        if self.yvel < 0: self.airborne = True
        if self.onGround == True: self.airborne = False
        if not self.onGround:
            self.yvel += .15
            if self.yvel > 1.2: self.airborne = True
            if self.yvel > 100: self.yvel = 100
        '''
        pos = self.rect.x
        #print(pos)
        #print(self.rect.y)

        if pos < self.boundary_left or pos > self.boundary_right:
            self.xvel *= -1
            if self.faceright == False: self.faceright = True
            else: self.faceright = False
        self.rect.x += self.xvel
        self.animate()

        # Collide with platforms (No player collision)
        self.collide(self.xvel, 0, platforms, projectiles, player)

        # Move
        self.rect.y += self.yvel
        self.onGround = False
        self.collide(0, self.yvel, platforms, projectiles, player)



    def collide(self, xvel, yvel, platforms, projectiles, player):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -2
                    self.faceright = False
                elif xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = 2
                    self.faceright = True
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                elif yvel < 0:
                    self.rect.top = p.rect.bottom
        for p in projectiles:
            if pygame.sprite.collide_rect(self, p):
                self.kill()
                player.score += 1



    def animate(self):
        self.walkloop()

    def walkloop(self):
        if self.counter >= 0 and self.counter <= 10:
            if self.faceright == True:
                self.image = self.walkright[1]
            else:
                self.image = self.walkleft[1]
        elif self.counter > 10 and self.counter <= 20:
            if self.faceright == True:
                self.image = self.walkright[2]
            else:
                self.image = self.walkleft[2]

        elif self.counter > 20:
            if self.faceright == True:
                self.image = self.walkright[0]

            else:
                self.image = self.walkleft[0]
            if self.counter >= 30:
                self.counter = 0
        self.counter = self.counter + 1

    # No gravity because this is a flying entity
    def calc_grav(self):
       return


class Projectile(Entity):

    projectileR = []
    projectileL = []
    counter = 0
    distance = 0

    def __init__(self, player, game):
        Entity.__init__(self)
        # Append sprites
        sprites = Sprites("proj1.png")
        image = sprites.get_image(6,6,35,13)
        self.projectileR.append(image)
        image = pygame.transform.flip(image, True, False)
        self.projectileL.append(image)

        sprites = Sprites("proj2.png")
        image = sprites.get_image(6, 8, 35, 9)
        self.projectileR.append(image)
        image = pygame.transform.flip(image, True, False)
        self.projectileL.append(image)

        sprites = Sprites("proj3.png")
        image = sprites.get_image(6, 8, 35, 9)
        self.projectileR.append(image)
        image = pygame.transform.flip(image, True, False)
        self.projectileL.append(image)

        sprites = Sprites("proj4.png")
        image = sprites.get_image(6, 7, 35, 9)
        self.projectileR.append(image)
        image = pygame.transform.flip(image, True, False)
        self.projectileL.append(image)



        self.player = player
        self.xvel = 5
        self.castright = player.faceright
        self.image = self.projectileR[0]
        self.rect = self.image.get_rect()
        self.rect.y = ((self.player.rect.top + self.player.rect.bottom ) / 2) - 10
        if self.castright == True:
            self.rect.x = self.player.rect.x + 55
        if self.castright == False:
            self.xvel *= -1
            self.rect.x = player.rect.left - 55
            self.image = self.projectileL[0]




    def update(self, platforms, enemygroup2):
        self.rect.x += self.xvel
        self.animate()
        self.collide(platforms, enemygroup2)

    def animate(self):
        # Changes sprite every 10 updates
        if (self.counter % 10) == 0:
            index = (self.counter // 10)
            if self.castright:
                self.image = self.projectileR[index - 1]
            else:
                self.image = self.projectileL[index - 1]

        if self.counter > 40:
            self.counter = 0
        self.counter += 1
        self.distance += 1

        # Delete the projectile after 150 updates
        if self.distance >= 150:
            self.kill()

    def collide(self, platforms, enemies):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                self.kill()
        for p in enemies:
            if pygame.sprite.collide_rect(self, p):
                    #self.kill()
                    self.distance = 150

class Backgrounds(Entity):

    def __init__(self,misc):
        Entity.__init__(self)
        misc_list = Sprites("tiles.png")

        image = misc_list.get_image(0, 0 ,48 , 48)
        color_switch = image.get_at((0,0))

        self.image = misc_list.get_image(misc[0], misc[1], misc[2], misc[3])

        self.image.set_colorkey(color_switch)
        self.rect = self.image.get_rect()

class Lives(Entity):

    def __init__(self,misc):
        Entity.__init__(self)
        misc_list = Sprites("heart.png")

        image = misc_list.get_image(0, 0 ,48 , 48)
        color_switch = image.get_at((0,0))

        self.image = misc_list.get_image(misc[0], misc[1], misc[2], misc[3])

        self.image.set_colorkey(color_switch)
        self.rect = self.image.get_rect()

    # Remove Heart from all groups
    def update(self):
        if self.player.get_damage() > 0:
            self.kill()


class Platform(Entity):

    def __init__(self, sprite_sheet_data):
        Entity.__init__(self)

        sprite_sheet = Sprites("tiles.png")
        image = sprite_sheet.get_image(0, 0, 1, 1)
        color_switch = image.get_at((0, 0))

        self.image = sprite_sheet.get_image(sprite_sheet_data[0], sprite_sheet_data[1], sprite_sheet_data[2], sprite_sheet_data[3])
        self.image.set_colorkey(color_switch)

        self.rect = self.image.get_rect()


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

        self.rect.x += self.change_x
        self.rect.y += self.change_y
        #print(self.change_y)
        self.distance += 1

        collision = pygame.sprite.collide_rect(self, self.player)
        if collision:

            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            elif self.change_y > 0:
                self.player.rect.top = self.rect.bottom
                #self.player.airborne = False
                #self.player.onGround = True
        #self.rect.y += self.change_y

        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
        if self.rect.left < self.boundary_left or self.rect.right > self.boundary_right:
            self.change_x *= -1
