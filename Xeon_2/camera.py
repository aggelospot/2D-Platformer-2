import pygame
import constants

'''A Camera class that can be used to focus at any entity in the game. Currently used to follow the player'''
class Camera(object):
    def __init__(self, camera_function, width, height):
        self.camera_function = camera_function
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)


    def update(self, target):
        self.state = self.camera_function(self.state, target.rect)

def simple_camera(camera, target_rect):
    left, top, _, _ = target_rect
    _, _, width, height = camera
    return pygame.Rect((constants.HALF_WIDTH) - left, (constants.HALF_HEIGHT) - top, width, height)

def complex_camera(camera, target_rect):
    left, top, _, _ = target_rect
    _, _, width, height = camera
    left, top, _, _ = -left + constants.HALF_WIDTH, -top + constants.HALF_HEIGHT, width, height  # center player

    left = min(0, left)                                         # stop scrolling at the left edge
    left = max(-(camera.width-constants.SCREEN_WIDTH), left)    # stop scrolling at the right edge
    top = max(-(camera.height-constants.SCREEN_HEIGHT), top)    # stop scrolling at the bottom
    top = min(0, top)                                           # stop scrolling at the top

    return pygame.Rect(left, top, width, height)