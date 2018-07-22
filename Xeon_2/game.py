import pygame
from sprites import Sprites

class Game(object):

    def __init__(self):
        # Create Sprite Groups
        self.entities = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.playerentity = pygame.sprite.Group()
        self.projectilegroup = pygame.sprite.Group()
        self.enemygroup = pygame.sprite.Group()
        self.enemygroup2 = pygame.sprite.Group()
        self.harmful_objects = pygame.sprite.Group()
        self.lives = pygame.sprite.Group()
        self.exitgroup = pygame.sprite.Group()
        self.menugroup = pygame.sprite.Group()
        self.titlegroup = pygame.sprite.Group()
        self.detectablegroup = pygame.sprite.Group()
        self.itemgroup = pygame.sprite.Group()
        # Create Camera
        self.camera = ""
        self.camerafocus = ""
        # Create Platforms
        self.platforms = []
        # Create Screen Focus
        self.screenfocus = "Title"

        '''Menu, Pause and other screens will be implemented later on'''
        # Create Title
        #self.title = Title(self)
        # Create Gameover
        #self.gameover = GameOver(self)
        # Create Level Complete
        #self.levelcomplete = LevelComplete(self)
        # Create Pause Menu
        #self.pausemenu = PauseMenu(self)

