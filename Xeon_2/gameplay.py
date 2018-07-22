import pygame
import constants
import cosmos

from player import Player
from camera import Camera, complex_camera, simple_camera
from game import Game

def main():
    pygame.init()

    size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Xeon2")

    game = Game()

    pc = Player(game)

    level_list = []
    level_list.append(cosmos.Level1(pc))

    player_level = 0
    current_level = level_list[player_level]

    active_sprite_list = pygame.sprite.Group()

    pc.level = current_level


    camera = Camera(complex_camera, constants.SCREEN_WIDTH*4, constants.SCREEN_HEIGHT*4)

    pc.rect.x = 15
    pc.rect.y = 700


    #active_sprite_list.add(pc)

    end = False
    won = False

    font = pygame.font.Font(None, 40)
    youlost = font.render("YOU LOST", 1, (255, 255, 255))
    youwon = font.render("YOU WIN!", 1, (255, 255, 255))

    done = False
    clock = pygame.time.Clock()

    while not pc.quit:

        pc.update()
        current_level.update()

        if pc.get_score() >= 14:
            pc.won = True

            '''
            #if player_level < len(level_list)-1:
            if player_level < 2:
                pc.rect.x = 120
                pc.rect.y = 0
                player_level += 1
                level_list.append(cosmos.Level2(pc))
                current_level = level_list[player_level]
                pc.level = current_level
            elif pc.get_score() >= 2:
            '''


        # Draw

        camerafocus = pc
        camera.update(camerafocus)


        # Draw the background
        screen.fill(constants.BLUE)
        current_level.drawBackground(screen)          #this calls cosmos.Level.draw()

        # Draw the spritegroups
        for p in pc.game.backgrounds:
            screen.blit(p.image, camera.apply(p))
        for p in game.enemygroup:
            screen.blit(p.image, camera.apply(p))

        for p in game.enemygroup2:
            screen.blit(p.image, camera.apply(p))

        for p in pc.game.entities:
            screen.blit(p.image, camera.apply(p))
        for p in game.playerentity:
            screen.blit(p.image, camera.apply(p))

        for p in game.projectilegroup:
            screen.blit(p.image, camera.apply(p))

        for p in game.lives:
            for i in range (0, pc.get_health()):    # draws hearts depending on the player's hp
                screen.blit(p.image, (i*50,0))



        score = pc.get_score()
        score_conv = str(score)
        score_text = font.render("Score: " + score_conv, 1, (255,255,255))



        if not pc.lost:
            if not pc.won:
                screen.blit(score_text, (1060, 0))
                if player_level == 0:
                    screen.blit(font.render("Level 1", 1, (255, 255, 255)), (1070, 30))
                elif player_level == 1:
                    screen.blit(font.render("Level 2", 1, (255, 255, 255)), (1070, 30))
            else:
                if pc.restart:
                    main()
                msg = font.render("Press Escape to quit or the 'R' key to restart", 1, (255, 255, 255))
                screen.blit(msg, (300, 100))
                screen.blit(youwon, (500, 50))
                screen.blit(score_text, (510, 150))
                pc.won = True

        else:
            if pc.restart:
                main()
            #pc.quit = True
            msg = font.render("Press Escape to quit or the 'R' key to restart", 1, (255, 255, 255))
            screen.blit(msg, (300, 100))
            screen.blit(score_text, (500, 100))
            screen.blit(youlost, (500, 50))


        clock.tick(60)

        pygame.display.flip()

    pygame.quit()

main()

