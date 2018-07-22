import pygame

import constants

import objects
from objects import MovingPlatform, Lives, Backgrounds
from sprites import Sprites
from entity import Entity
from game import Game

class Player(Entity):
    #Player Variables Initialization
    xvel = 0
    yvel = 0
    score = 0
    lost = False
    curr_time = 0
    timer = 0
    idletimer = 0
    atkcounter = 0
    atkend = 0;
    hp = 3
    jheight = 0
    damage = 0
    level = None
    attacking = False
    restart = False

    # Sprite List Initialization
    idle_frames_l = []
    idle_frames_r = []
    jump_frame_up_l = []
    jump_frame_up_r = []
    jump_frame_down_r = []
    jump_frame_down_l = []
    death_frame = None
    flash_frame = None
    hurt_frame_l = None
    hurt_frame_r = None
    walking_frames_l = []
    walking_frames_r = []
    test_frames = []
    attack_frames_R = []
    attack_frames_L = []


    def __init__(self, game):
        Entity.__init__(self)

        # Create Player Sprite
        self.image = pygame.Surface((300, 200), pygame.SRCALPHA)
        self.rect = pygame.Rect(0, 0, 300, 200)

        self.game = game
        self.game.playerentity.add(self)

        # Set Player Velocities
        self.xvel = 0
        self.yvel = 0

        # Set Player Offsets (might be implemented later)
        #self.xoffset = -128
        #self.yoffset = 0

        # Counters (might be used later on)
        self.walkcounter = 0
        self.standcounter = 0
        self.attackcounter = 0
        self.takedamagecounter = 0

        # States
        #self.collideright = False
        self.onGround = False
        self.airborne = True
        self.takingdamage = False
        self.attacking = False
        self.moving = False
        self.faceright = True
        self.won = False
        self.quit = False

        # Create Player Detectable Area
        # to be implemented

        # Jump sprites ( jump_frame_up is used when the player takes off, and jump_frame_down when the effects of gravity are taking place  )
        sprites = Sprites("j1.png")
        image = sprites.get_image(0, 0, 65, 75)
        self.jump_frame_up_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.jump_frame_up_l.append(image)


        sprites = Sprites("j2.png")
        image = sprites.get_image(0, 0, 65, 75)
        self.jump_frame_up_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.jump_frame_up_l.append(image)

        sprites = Sprites("j3.png")
        image = sprites.get_image(0, 0, 65, 84)
        self.jump_frame_down_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.jump_frame_down_l.append(image)

        sprites = Sprites("j4.png")
        image = sprites.get_image(0, 0, 65, 84)
        self.jump_frame_down_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.jump_frame_down_l.append(image)

        #Walking Sprites
        sprites = Sprites("w1.png")
        image = sprites.get_image(0, 0, 60, 70)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        sprites = Sprites("w2.png")
        image = sprites.get_image(0, 0, 60, 70)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        sprites = Sprites("w3.png")
        image = sprites.get_image(0, 0, 60, 70)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        sprites = Sprites("w4.png")
        image = sprites.get_image(0, 0, 60, 70)
        self.walking_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Shooting Sprites
        sprites = Sprites("shoot1.png")
        image = sprites.get_image(0, 0, 65, 70)
        self.attack_frames_R.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_L.append(image)

        sprites = Sprites("shoot2.png")
        image = sprites.get_image(0, 0, 65, 70)
        self.attack_frames_R.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_L.append(image)

        sprites = Sprites("shoot3.png")
        image = sprites.get_image(0, 0, 65, 70)
        self.attack_frames_R.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_L.append(image)

        sprites = Sprites("shoot4.png")
        image = sprites.get_image(0, 0, 65, 70)
        self.attack_frames_R.append(image)
        image = pygame.transform.flip(image, True, False)
        self.attack_frames_L.append(image)

        # Death Sprite
        sprites = Sprites("idle1.png")
        image = sprites.get_image(0, 0, 95, 91)
        self.death_frame = image

        # Idle Frames
        sprites = Sprites("idle1.png")
        image = sprites.get_image(0, 0, 55, 70)
        self.idle_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)

        sprites = Sprites("idle2.png")
        image = sprites.get_image(0, 0, 55, 70)
        self.idle_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)

        sprites = Sprites("idle3.png")
        image = sprites.get_image(0, 0, 55, 70)
        self.idle_frames_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.idle_frames_l.append(image)

        sprites = Sprites("flash.png")
        image = sprites.get_image(0, 0, 95, 91)
        self.flash_frame = image

        sprites = Sprites("hurt.png")
        self.hurt_frame_r = image
        image = pygame.transform.flip(image, True, False)
        self.hurt_frame_l = image

        # Arxiko sprite

        if self.faceright == True:
            self.image = self.idle_frames_r[0]
        else:
            self.image = self.idle_frames_l[0]
        self.rect = self.image.get_rect()



    def set_score(self, bonus):
        self.score += bonus

    def get_score(self):
        return self.score

    # Sounds (more and better sounds will be added)
    def play_death_sound(self):
        dead = pygame.mixer.Sound("death.wav")
        dead.set_volume(0.03)
        dead.play()

    def play_jump_sound(self):
        jump = pygame.mixer.Sound("jump.wav")
        jump.set_volume(0.1)
        jump.play()

    #Calculate Damage taken in case of enemy collision
    def take_damage(self):
         if self.hp <= 0:
            self.lost = True
            self.play_death_sound()
            self.damage = 0

         else:
            self.damage = 1
            self.hp -= self.damage
            self.timer = pygame.time.get_ticks()        # set a timer at the time of the first collision
            self.takingdamage = True

    def get_health(self):
        return self.hp

    def get_status(self):
        return self.lost

    # Makes the player unable to take damage more than once in a 1 second time frame
    def invincibility(self):
        self.curr_time = pygame.time.get_ticks()
        self.takingdamage = True
        if self.curr_time > (self.timer + 1000):
            self.takingdamage = False

    # Checks keyboard input
    def input_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                # note: replace the self.lost check with a pause function
                if not self.lost:
                    if event.key == pygame.K_LEFT:
                        self.go_left()
                        self.moving = True
                    if event.key == pygame.K_RIGHT:
                        self.go_right()
                        self.moving = True
                    if event.key == pygame.K_UP:
                        self.jump()
                    if event.key == pygame.K_SPACE:
                        self.attacking = True
                if self.won or self.lost:
                    if event.key ==pygame.K_ESCAPE:
                        self.quit = True
                    if event.key == pygame.K_r:
                        self.restart = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.xvel < 0:
                    self.stop()
                    self.moving = False
                if event.key == pygame.K_RIGHT and self.xvel > 0:
                    self.stop()
                    self.moving = False

    def update(self):

        self.input_handler()                #Check keyboard input
        self.calc_grav()                    #Calculate gravity

        self.animate()                      #Animate the player entity

        self.rect.x += self.xvel            #Increase player x coordinate and check for collisions
        self.collide(self.xvel,0)

        self.rect.y += self.yvel            #Increase player y coordinate and check for collisions
        self.collide(0,self.yvel)


    def animate(self):
        #Coordinates used to calculate the index for the animation arrays
        pos = self.rect.x
        posy = self.rect.y
        #Dying Animation

        #if self.lost:
        #    self.image = self.death_frame
        #Attack Animation
        if self.attacking:
            if self.atkcounter >= 0 and self.atkcounter <= 2:
                if self.faceright:
                    self.image = self.attack_frames_R[0]
                else:
                    self.image = self.attack_frames_L[0]
            elif self.atkcounter >= 2 and self.atkcounter <= 4:
                if self.faceright:
                    self.image = self.attack_frames_R[1]
                else:
                    self.image = self.attack_frames_L[1]
            elif self.atkcounter >= 4 and self.atkcounter <= 6:
                if self.faceright:
                    self.image = self.attack_frames_R[2]
                else:
                    self.image = self.attack_frames_L[2]
            elif self.atkcounter >= 6 and self.atkcounter <= 10:
                if self.faceright:
                    self.image = self.attack_frames_R[3]
                else:
                    self.image = self.attack_frames_L[3]
            elif self.atkcounter >= 8:
                self.atkcounter = 0
                self.attacking = False
                self.shoot()
            self.atkcounter += 1
        #Moving Animation
        elif self.moving and not self.airborne:
            if self.faceright:
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            else:
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]
        #Flying Animation
        elif self.airborne and not self.onGround:
            if self.yvel < 0:
                if self.faceright:
                    frame = (posy // 60) % len(self.jump_frame_up_r)
                    self.image = self.jump_frame_up_r[frame]
                else:
                    frame = (posy // 60) % len(self.jump_frame_up_l)
                    self.image = self.jump_frame_up_l[frame]
            elif self.yvel > 0:
                if self.faceright:
                    frame = (posy // 60) % len(self.jump_frame_down_r)
                    self.image = self.jump_frame_down_r[frame]
                else:
                    frame = (posy // 60) % len(self.jump_frame_down_l)
                    self.image = self.jump_frame_down_l[frame]
        #Idle Animation
        elif self.onGround:
            self.stop()
            #Can also be implemented with a counter instead of a timer
            self.idletimer = pygame.time.get_ticks()
            if self.faceright == True:
                frame = (self.idletimer // 210) % len(self.idle_frames_r)
                self.image = self.idle_frames_r[frame]
            else:
                frame = (self.idletimer // 210) % len(self.idle_frames_l)
                self.image = self.idle_frames_l[frame]

    def collide(self, xvel, yvel):

        # Collide Platforms
        if self.onGround == False:
            self.airborne = True
        self.onGround = False

        for p in self.game.entities:
            if pygame.sprite.collide_rect(self, p):
                self.airborne = False
                self.onGround = True
                if xvel > 0:
                    self.rect.right = p.rect.left
                elif xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.yvel = 0
                elif yvel < 0:
                    self.yvel=0
                    self.rect.top = p.rect.bottom
                if isinstance(p, MovingPlatform):
                    self.rect.x += 2*(p.change_x)
                    #if p.change_y > 0:
        # Collide Enemies
        if yvel == 0:                                                                           #avoids unnecessary iteration (@line 261)
            enemy_hit_list = pygame.sprite.spritecollide(self, self.game.enemygroup, False)
            if enemy_hit_list:
                if not self.takingdamage:
                    self.take_damage()
                else:
                    if self.takingdamage:
                        self.invincibility()
                        # Make the character flash every few miliseconds
                        if (self.curr_time % 5 == 2):
                            self.image = self.flash_frame

            enemy_hit_list = pygame.sprite.spritecollide(self, self.game.enemygroup2, False)
            if enemy_hit_list:
                if not self.takingdamage:
                    self.take_damage()
                else:
                    if self.takingdamage:
                        self.invincibility()
                        if (self.curr_time % 5 == 2):
                            self.image = self.flash_frame

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.yvel == 0:
            self.yvel = 2
        else:
            self.yvel += .15

        self.jheight = constants.SCREEN_HEIGHT - self.rect.height
        if self.rect.y >= self.jheight and self.yvel >= 0:
            self.yvel = 0
            self.rect.y = self.jheight
            #if self.faceright == True:
            #    self.image = self.idle_frames_r[0]
            #else:
            #    self.image = self.idle_frames_l[0]
    def jump(self):

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.game.entities, False)
        self.rect.y -= 2
        #self.onGround = False
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.yvel = -5
            self.play_jump_sound()
    def shoot(self):
        if not self.attacking:
            self.game.projectilegroup.add(objects.Projectile(self, self.game))

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.xvel = -6
        self.faceright = False
        self.moving = True

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.xvel = 6
        self.faceright = True
        self.moving = True

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.xvel = 0
        self.moving = False

