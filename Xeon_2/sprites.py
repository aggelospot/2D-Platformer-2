import pygame

import constants

'''I have implemented different methods to grab a sprite sheet but currently only use one of them because i found that splitting the images creates less problems'''
class Sprites(object):
    """ Class used to grab images out of a sprite sheet. """
    # This points to our sprite sheet image
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)

        # Return the image
        return image

    def get_image_part(self, x, y, width, height):
        #sprite_sheet = pygame.image.load("Xeonsheet.bmp").convert()

        character = pygame.Surface((80, 70), pygame.SRCALPHA)
        character.blit(self.sprite_sheet, (-14, -171))
        # character = pygame.transform.scale(character, (19 * 4, 22 * 4))
        stage = pygame.Surface((350, 150), pygame.SRCALPHA)
        stage.blit(character, (130, 0))
        self.test_frames.append(stage)



    def image_at(self, rectangle, colorkey=None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sprite_sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey=None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colorkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey=None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
            for x in range(image_count)]
        return self.images_at(tups, colorkey)