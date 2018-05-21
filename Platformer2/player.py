import pygame

import constants

from objects import MovingPlatform, Misc
from sprites import Sprites



class Player(pygame.sprite.Sprite):
    GREEN = (0, 255, 0)
    change_x = 0
    change_y = 0
    score = 0
    lost = False
    inv = 0
    timer = 0
    hurt = False

    def set_score(self, bonus):
        self.score += bonus

    def get_score(self):
        return self.score

    def play_death_sound(self):
        dead = pygame.mixer.Sound("death.wav")
        dead.set_volume(0.03)
        dead.play()

    def play_jump_sound(self):
        jump = pygame.mixer.Sound("jump.wav")
        jump.set_volume(0.1)
        jump.play()

    def player_death(self):
         if self.damage > 2:
            self.lost = True
            self.play_death_sound()

         else:
            self.damage += 1
            self.timer = pygame.time.get_ticks()
            self.set_inv_timer()

    def get_damage(self):
        return self.damage

    def get_health(self):
        return self.damage

    def get_status(self):
        return self.lost

    def set_inv_timer(self):
        self.inv = True

    def get_inv_timer(self):
        return self.timer


    # Pinakes eikonwn

    idle_frame_l = None
    idle_frame_l = None
    jump_frame_r = None
    jump_frame_l = None
    death_frame = None
    flash_frame = None
    hurt_frame_l = None
    hurt_frame_r = None
    walking_frames_l = []
    walking_frames_r = []

    moving = False
    direction = "R"
    damage = 0
    level = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #Jump sprites ( Left and Right side )

        sprites = Sprites("jump_001.png")
        image = sprites.get_image(0, 0, 101, 109)
        color_switch = image.get_at((0,0))
        image.set_colorkey(color_switch)
        self.jump_frame_r = image
        image = pygame.transform.flip(image, True, False)
        self.jump_frame_l = image

        ##################################################
        #Right+Left side walking sprites
        sprites = Sprites("walk_000.png")
        image = sprites.get_image(0,0,105,95)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        sprites = Sprites("walk_001.png")
        image = sprites.get_image(0, 0, 105, 95)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        sprites = Sprites("walk_002.png")
        image = sprites.get_image(0, 0, 105, 95)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        sprites = Sprites("walk_003.png")
        image = sprites.get_image(0, 0, 105, 95)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        sprites = Sprites("walk_004.png")
        image = sprites.get_image(0, 0, 105, 95)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #Death Sprite
        sprites = Sprites("die_004.png")
        image = sprites.get_image(0, 0, 95, 91)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.death_frame = image

        sprites = Sprites("idle_000.png")
        image = sprites.get_image(0, 0, 95, 91)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.idle_frame_r = image
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        sprites = Sprites("flash.png")
        image = sprites.get_image(0, 0, 95, 91)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.flash_frame = image

        sprites = Sprites("hurt1.png")
        image = sprites.get_image(0, 0, 125, 91)
        color_switch = image.get_at((0, 0))
        image.set_colorkey(color_switch)
        self.hurt_frame_r = image
        image = pygame.transform.flip(image, True, False)
        self.hurt_frame_l = image


        # Arxiko sprite

        if self.direction == "R":
            self.image = self.walking_frames_r[0]
        else:
            self.image = self.walking_frames_l[0]
        self.rect = self.image.get_rect()




    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()


        self.rect.x += self.change_x
        pos = self.rect.x   # + self.level.world_shift()

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)


        if self.lost == True:
            self.image = self.death_frame
        elif self.direction == "R" and (self.change_y == 0 or self.moving == True):
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L" and (self.change_y == 0 or self.moving == True):
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        elif self.direction == "R" and self.change_y != 0:
            self.image = self.jump_frame_r
        elif self.direction == "L" and self.change_y != 0:
            self.image = self.jump_frame_l




        if enemy_hit_list:
            if self.inv == False:
                self.player_death()

            else:
                if self.hurt == True:
                    if self.direction == "L":
                        self.image = self.hurt_frame_l
                    else:
                        self.image = self.hurt_frame_r

        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom


            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += (block.change_x/10)

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .15


        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
            if self.direction == "R":
                self.image = self.walking_frames_r[0]
            else:
                self.image = self.walking_frames_l[0]

    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -8
            self.walking_frames_r[0]
            self.play_jump_sound()

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        if self.direction == "R":
            self.image = self.idle_frame_r
        else:
            self.image = self.idle_frame_l
        self.change_x = 0

