import pygame

import constants
import objects

class Level():

    entities = None
    enemy_list = None
    camerafocus = ""
    background = None

    def __init__(self, player, game):
        self.game = game
        game.entities = pygame.sprite.Group()
        game.enemygroup = pygame.sprite.Group()
        game.lives = pygame.sprite.Group()
        self.heart_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.game.entities.update()
        self.game.enemygroup.update()
        self.game.enemygroup2.update(self.game.entities, self.game.projectilegroup, self.player)
        self.game.projectilegroup.update(self.game.entities, self.game.enemygroup2)


        #self.game.lives.update(self.player)

    def drawBackground(self, screen):
        screen.blit(self.background, (0, 0))

    def setLives(self):
        heart_list = [[objects.HEART, 0, 0]]

        for hearts in heart_list:
            block = objects.Lives(hearts[0])
            block.rect.x = hearts[1]
            block.rect.y = hearts[2]
            block.player = self.player
            self.game.lives.add(block)

    def setGroups(self, neutral, enemy):

        for enemy in enemy:
            block = objects.Harmful(enemy[0])
            block.rect.x = enemy[1]
            block.rect.y = enemy[2]
            block.player = self.player
            self.game.enemygroup.add(block)

        for platform in neutral:
            block = objects.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.game.entities.add(block)



class Level1(Level):


    def __init__(self, player):

        Level.__init__(self, player, player.game)

        self.background = pygame.image.load("background1.png").convert()

        #Invisible obstacles stop the player from going out of bounds
        self.level = [[objects.INV_OBSTACLE, -50, -400], [objects.INV_OBSTACLE, -50, 0], [objects.INV_OBSTACLE, -50, 408]]

        self.harmful_objects = [[objects.SPIKES, 480, 768],[objects.SPIKES, 600, 768], [objects.SPIKES, 720, 768], [objects.SPIKES, 840, 768], [objects.SPIKES, 450, 185],  [objects.SPIKES, 578, 185], [objects.SPIKES, 706, 185], [objects.SPIKES, 833, 185],]

        # Add the hearts and enemy/platform sprites to spritegroups in class Game
        self.setLives()
        self.setGroups(self.level, self.harmful_objects)

        block = objects.Bat(500, 600, 2)
        block.boundary_left = 300
        block.player = self.player
        self.game.enemygroup2.add(block)

        block = objects.Bat(350, 285, 2)
        block.boundary_left = 200
        block.boundary_right = 630
        block.player = self.player
        self.game.enemygroup2.add(block)

        block = objects.Bat(300, 50, 2)
        block.boundary_left = 150
        block.boundary_right = 780
        block.player = self.player
        self.game.enemygroup2.add(block)

        block = objects.Bat(1300, 600, 2)
        block.boundary_left = 1100
        block.boundary_right = 1500
        block.player = self.player
        self.game.enemygroup2.add(block)

        block = objects.Bat(1300, 400, 2)
        block.boundary_left = 1000
        block.boundary_right = 1500
        block.player = self.player
        self.game.enemygroup2.add(block)

        block = objects.Bat(1100, 300, 2)
        block.boundary_left = 1000
        block.boundary_right = 1500
        block.player = self.player
        self.game.enemygroup2.add(block)

        block = objects.Bat(1100, 200, 2)
        block.boundary_left = 1000
        block.boundary_right = 1500
        block.player = self.player
        self.game.enemygroup2.add(block)

        '''
        block = objects.Harmful(objects.SPIKES)
        block.rect.x = 330
        block.rect.y = 550
        block.player = self.player
        block.level = self
        self.game.entities.add(block)
        '''

        block = objects.Platform(objects.FLOOR)
        block.rect.x = 0
        block.rect.y = 750
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.FLOOR)
        block.rect.x = 480
        block.rect.y = 783
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.FLOOR)
        block.rect.x = 960
        block.rect.y = 750
        block.player = self.player
        block.level = self
        self.game.entities.add(block)



        block = objects.Platform(objects.FLOOR)
        block.rect.x = 1200
        block.rect.y = 750
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.FLOOR)
        block.rect.x = 1350
        block.rect.y = 750
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 960
        block.rect.y = 141
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 960
        block.rect.y = 237
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 960
        block.rect.y = 333
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 960
        block.rect.y = 429
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 1810
        block.rect.y = 650
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 1810
        block.rect.y = 650
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 1810
        block.rect.y = 555
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 1810
        block.rect.y = 460
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 1810
        block.rect.y = 365
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 1810
        block.rect.y = 270
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 1810
        block.rect.y = 175
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 1810
        block.rect.y = 80
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.CHAINS)
        block.rect.x = 1810
        block.rect.y = -15
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.BOX_S_STRIPPED)
        block.rect.x = 960
        block.rect.y = 686
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.BOX_S_STRIPPED)
        block.rect.x = 960
        block.rect.y = 623
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.BOX_S_STRIPPED)
        block.rect.x = 960
        block.rect.y = 560
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.BOX_S_STRIPPED)
        block.rect.x = 960
        block.rect.y = 497
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.BOX_B_STRIPPED)
        block.rect.x = 1023
        block.rect.y = 653
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_W_WINDOWS)
        block.rect.x = 270
        block.rect.y = 520
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_W_WINDOWS)
        block.rect.x = 270
        block.rect.y = 270
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_W_WINDOWS)
        block.rect.x = 843
        block.rect.y = 520
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_W_WINDOWS)
        block.rect.x = 1227
        block.rect.y = 520
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_W_WINDOWS)
        block.rect.x = -300
        block.rect.y = 270
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_W_WINDOWS)
        block.rect.x = 843
        block.rect.y = 270
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_W_WINDOWS)
        block.rect.x = 1227
        block.rect.y = 270
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_BOXES)
        block.rect.x = 0
        block.rect.y = 143
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_BOXES)
        block.rect.x = 764
        block.rect.y = 143
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_BOXES)
        block.rect.x = 380
        block.rect.y = 143
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_BOXES)
        block.rect.x = 0
        block.rect.y = 0
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_BOXES)
        block.rect.x = 764
        block.rect.y = 0
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_BLACK_BOXES)
        block.rect.x = 380
        block.rect.y = 0
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)


        block = objects.Platform(objects.FLOOR)
        block.rect.x = -125
        block.rect.y = 526
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Backgrounds(objects.BACKGROUND_W_STAIRS)
        block.rect.x = 0
        block.rect.y = 526
        block.player = self.player
        block.level = self
        self.game.backgrounds.add(block)


        block = objects.Platform(objects.PLATFORM_DARK_GREY)
        block.rect.x = 500
        block.rect.y = 200
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.PLATFORM_DARK_GREY)
        block.rect.x = 720
        block.rect.y = 200
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.PLATFORM_DARK_GREY)
        block.rect.x = 256
        block.rect.y = 200
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.PLATFORM_DARK_GREY)
        block.rect.x = 960
        block.rect.y = 113
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.MovingPlatform(objects.SMALL_PLAT)
        block.rect.x = 770
        block.rect.y = 400
        block.boundary_bottom = 680
        block.boundary_top = 350
        block.boundary_left = -380
        block.boundary_right = 1900
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.MovingPlatform(objects.SMALL_PLAT)
        block.rect.x = 1300
        block.rect.y = 400
        block.boundary_bottom = 630
        block.boundary_top = 150
        block.boundary_left = -380
        block.boundary_right = 1900
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.MovingPlatform(objects.SMALL_PLAT)
        block.rect.x = 0
        block.rect.y = 250
        block.boundary_bottom = 450
        block.boundary_top = 150
        block.boundary_left = -380
        block.boundary_right = 1900
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.MovingPlatform(objects.PLATFORM_GREY_SMALL)
        block.rect.x = 700
        block.rect.y = 150
        block.boundary_bottom = 450
        block.boundary_top = 150
        block.boundary_left = 450
        block.boundary_right = 900
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.BOX_S_STRIPPED)
        block.rect.x = 200
        block.rect.y = 463
        block.player = self.player
        block.level = self
        self.game.entities.add(block)


        block = objects.Platform(objects.PLATFORM_GREY_SMALL)
        block.rect.x = 550
        block.rect.y = 700
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        block = objects.Platform(objects.PLATFORM_GREY_SMALL)
        block.rect.x = 550
        block.rect.y = 400
        block.player = self.player
        block.level = self
        self.game.entities.add(block)

        '''
        block = objects.MovingPlatform(objects.SMALL_PLAT)
        block.rect.x = 550
        block.rect.y = 700
        block.boundary_bottom = 700
        block.boundary_top = 100
        block.boundary_left = 550
        block.boundary_right = 750
        block.change_x = -1
        block.player = self.player
        block.level = self
        self.game.entities.add(block)
        '''
        '''
        block = objects.MovingPlatform(objects.FLOOR)           #add the moving platforms (direction: horizontal)
        block.rect.x = 0
        block.rect.y = 750
        block.boundary_left = -380
        block.boundary_right = 2000
        block.change_x = -2
        block.player = self.player
        block.level = self
        self.game.entities.add(block)
        '''

class Level2(Level):
    #Level 2 Empty for now
    def __init__(self, player):

        Level.__init__(self,player, player.game)

        self.background = pygame.image.load("back4.png").convert()

        self.level = [[objects.FLOOR, 390,700], [objects.AIR_PLAT, 500, 400]]

        self.game.harmful_objects = [[objects.HOT_MAGMA, 0, 765], [objects.HOT_MAGMA, 295, 765], [objects.HOT_MAGMA, 2 * 295, 765],
                   [objects.HOT_MAGMA, 3 * 295, 765], [objects.HOT_MAGMA, 4 * 295, 765],[objects.HOT_MAGMA, -250,765], [objects.HOT_MAGMA, -500,765]]


        self.setLives()
        self.setGroups(self.level, self.game.harmful_objects)





