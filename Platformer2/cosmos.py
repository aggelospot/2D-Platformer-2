import pygame

import constants
import objects

class Level():

    platform_list = None
    enemy_list = None

    background = None

    world_shift = 0
    level_limit = 500

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.misc_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

        if self.player.get_damage() > 0:

            self.misc_list.update()                     #objects.Misc.update() ---> deletes all sprites from the misc_list spritegroup

            if self.player.get_damage() == 1:           #If the player has taken 1 dmg, add 2 hearts to the now empty spritegroup
                block = objects.Misc(objects.HEART)
                block.rect.x = 0
                block.rect.y = 0
                block.player = self.player
                self.misc_list.add(block)
                block = objects.Misc(objects.HEART)
                block.rect.x = 50
                block.rect.y = 0
                block.player = self.player
                self.misc_list.add(block)
            elif self.player.get_damage() == 2:         #If the player has taken 2 dmg, add 1 heart.
                block = objects.Misc(objects.HEART)
                block.rect.x = 0
                block.rect.y = 0
                block.player = self.player
                self.misc_list.add(block)
            else:                                       #Otherwise call update() again to remove all the remaining hearts
                self.misc_list.update()


    def get_platform_list(self):
        return self.misc_list

    def draw(self, screen):

        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.misc_list.draw(screen)

    def shift_world(self, shift_x):

        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


class Level1(Level):


    def __init__(self, player):

        Level.__init__(self, player)

        self.background = pygame.image.load("background.png").convert()
        self.level_limit = -1300

        self.level = []

        enemies = [[objects.HOT_MAGMA, -750, 765], [objects.HOT_MAGMA, -450,765], [objects.HOT_MAGMA, -750, 565], [objects.HOT_MAGMA, -450,565],
        [objects.HOT_MAGMA, -750, 365], [objects.HOT_MAGMA, -450,365], [objects.HOT_MAGMA, -450,105]]

        misc_list = [[objects.HEART, 0,0], [objects.HEART, 50,0], [objects.HEART, 100,0]]



        for enemy in enemies:
            block = objects.Harmful(enemy[0])
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.player = self.player
            self.enemy_list.add(block)


        for platform in self.level:
            block = objects.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for misc in misc_list:
            block = objects.Misc(misc[0])
            block.rect.x = misc[1]
            block.rect.y = misc[2]
            block.player = self.player
            self.misc_list.add(block)


        block = objects.MovingPlatform(objects.FLOOR)           #add the moving platforms (direction: horizontal)
        block.rect.x = 0
        block.rect.y = 750
        block.boundary_left = -380
        block.boundary_right = 2000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


        block = objects.MovingPlatform(objects.FLOOR)
        block.rect.x = 385
        block.rect.y = 750
        block.boundary_left = -380
        block.boundary_right = 2000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingPlatform(objects.FLOOR)
        block.rect.x = 770
        block.rect.y = 750
        block.boundary_left = -380
        block.boundary_right = 2000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingPlatform(objects.FLOOR)
        block.rect.x = 1155
        block.rect.y = 750
        block.boundary_left = -380
        block.boundary_right = 2000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingPlatform(objects.FLOOR)
        block.rect.x = 1535
        block.rect.y = 750
        block.boundary_left = -380
        block.boundary_right = 2000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingHarmful(objects.BAT)              #add the moving enemies (direction: horizontal)
        block.rect.x = 2000
        block.rect.y = 550
        block.boundary_left = -380
        block.boundary_bottom = 800
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)

        block = objects.MovingHarmful(objects.BAT)
        block.rect.x = 1600
        block.rect.y = 550
        block.boundary_left = -380
        block.boundary_bottom = 800
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)

        block = objects.MovingHarmful(objects.BAT)
        block.rect.x = 1800
        block.rect.y = 300
        block.boundary_left = -380
        block.boundary_bottom = 800
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)

        block = objects.MovingPlatform(objects.SMALL_PLAT)      #small moving platform (direction: vertical)
        block.rect.x = 200
        block.rect.y = 500
        block.boundary_bottom = 650
        block.boundary_top = 200
        block.boundary_left = -380
        block.boundary_right = 1900
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingPlatform(objects.SMALL_PLAT)
        block.rect.x = 900
        block.rect.y = 120
        block.boundary_bottom = 650
        block.boundary_top = 100
        block.boundary_left = -380
        block.boundary_right = 1900
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingHarmful(objects.PUMPKIN)          #add the moving enemies(direction: vertical)
        block.rect.x = 500
        block.rect.y = -500
        block.boundary_bottom = 750
        block.change_y = 4
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)

        block = objects.MovingHarmful(objects.PUMPKIN)
        block.rect.x = 200
        block.rect.y = -1500
        block.boundary_bottom = 750
        block.change_y = 4
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)


class Level2(Level):

    def __init__(self, player):

        Level.__init__(self,player)

        self.background = pygame.image.load("back4.png").convert()
        self.level_limit = -1300

        self.level = [[objects.FLOOR, 390,700], [objects.AIR_PLAT, 500, 400]]

        enemies = [[objects.HOT_MAGMA, 0, 765], [objects.HOT_MAGMA, 295, 765], [objects.HOT_MAGMA, 2 * 295, 765],
                   [objects.HOT_MAGMA, 3 * 295, 765], [objects.HOT_MAGMA, 4 * 295, 765],[objects.HOT_MAGMA, -250,765], [objects.HOT_MAGMA, -500,765]]

        misc_list = [[objects.HEART, 0, 0], [objects.HEART, 50, 0], [objects.HEART, 100, 0]]

        for enemy in enemies:
            block = objects.Harmful(enemy[0])
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.player = self.player
            self.enemy_list.add(block)

        for platform in self.level:
            block = objects.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for misc in misc_list:
            block = objects.Misc(misc[0])
            block.rect.x = misc[1]
            block.rect.y = misc[2]
            block.player = self.player
            self.misc_list.add(block)

        block = objects.MovingHarmful(objects.WITCH)
        block.rect.x = 1600
        block.rect.y = 350
        block.boundary_left = -380
        block.boundary_bottom = 550
        block.change_x = -8
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)

        block = objects.MovingPlatform(objects.AIR_PLAT)
        block.rect.x = 100
        block.rect.y = 200
        block.boundary_bottom = 470
        block.boundary_top = 200
        block.boundary_left = -100
        block.boundary_right = 1000
        block.change_y = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingPlatform(objects.AIR_PLAT)
        block.rect.x = 900
        block.rect.y = 400
        block.boundary_bottom = 470
        block.boundary_top = 200
        block.boundary_left = -100
        block.boundary_right = 1000
        block.change_y = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingPlatform(objects.FLOOR)
        block.rect.x = 1200
        block.rect.y = 700
        block.boundary_bottom = 700
        block.boundary_top = 200
        block.boundary_left = -380
        block.boundary_right = 1000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingPlatform(objects.AIR_PLAT)
        block.rect.x = 400
        block.rect.y = 600
        block.boundary_bottom = 700
        block.boundary_top = 200
        block.boundary_left = -100
        block.boundary_right = 2000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingPlatform(objects.AIR_PLAT)
        block.rect.x = 1200
        block.rect.y = 600
        block.boundary_bottom = 700
        block.boundary_top = 200
        block.boundary_left = -100
        block.boundary_right = 2000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        '''
        block = objects.MovingPlatform(objects.FLOOR)
        block.rect.x = 1600
        block.rect.y = 700
        block.boundary_bottom = 700
        block.boundary_top = 200
        block.boundary_left = -380
        block.boundary_right = 2000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block = objects.MovingPlatform(objects.FLOOR)
        block.rect.x = 800
        block.rect.y = 700
        block.boundary_bottom = 700
        block.boundary_top = 200
        block.boundary_left = -380
        block.boundary_right = 2000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        '''
        block = objects.MovingHarmful(objects.BAT)
        block.rect.x = 1800
        block.rect.y = 300
        block.boundary_left = -380*4
        block.boundary_bottom = 800
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)
        '''
        block = objects.MovingHarmful(objects.BAT)
        block.rect.x = 1000
        block.rect.y = 800
        block.boundary_left = -380
        block.boundary_bottom = 800
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)
        '''
        block = objects.MovingHarmful(objects.BAT)
        block.rect.x = 600
        block.rect.y = 800
        block.boundary_left = -380*3
        block.boundary_bottom = 800
        block.change_x = -4
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)

        block = objects.MovingHarmful(objects.PUMPKIN)  # add the moving enemies(direction: vertical)
        block.rect.x = 500
        block.rect.y = -1500
        block.boundary_bottom = 750
        block.change_y = 4
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)

