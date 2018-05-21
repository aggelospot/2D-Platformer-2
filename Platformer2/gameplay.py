import pygame
import constants
import cosmos

from player import Player


def main():
    pygame.init()

    size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("HOT MAGMA")

    pc = Player()

    level_list = []
    level_list.append(cosmos.Level1(pc))
    level_list.append(cosmos.Level2(pc))

    player_level = 0
    current_level = level_list[player_level]

    active_sprite_list = pygame.sprite.Group()

    pc.level =current_level




    pc.rect.x = 340
    #pc.rect.y = constants.SCREEN_HEIGHT - pc.rect.height + 1000

    active_sprite_list.add(pc)

    end = False
    won = False

    font = pygame.font.Font(None, 40)
    youlost = font.render("YOU LOST", 1, (255, 255, 255))
    youwon = font.render("YOU WIN!", 1, (255, 255, 255))

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN and end == False:
                if event.key == pygame.K_LEFT:
                    pc.go_left()
                    pc.moving = True
                if event.key == pygame.K_RIGHT:
                    pc.go_right()
                    pc.moving = True
                if event.key == pygame.K_UP:
                    pc.jump()
                if event.key == pygame.K_F1:
                    end = True
                    won = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and pc.change_x < 0:
                    pc.stop()
                    pc.moving = False
                if event.key == pygame.K_RIGHT and pc.change_x > 0:
                    pc.stop()
                    pc.moving = False

        active_sprite_list.update()

        current_level.update()

        curr_time = pygame.time.get_ticks()
        timeofdmg = pc.get_inv_timer()

        if curr_time > (timeofdmg + 1000):
            pc.inv = False
        if ((curr_time - timeofdmg)/2 == 0):
            pc.hurt = True



        if pc.get_score() > 30:
            if player_level < len(level_list)-1:
                pc.rect.x = 120
                pc.rect.y = 0
                player_level += 1
                current_level = level_list[player_level]
                pc.level = current_level
            elif pc.get_score() > 99:
                won = True

        # Draw

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        score = pc.get_score()
        score_conv = str(score)
        score_text = font.render("Score: " + score_conv, 1, (255,255,255))



        if pc.get_status() == False:
            if not won:
                screen.blit(score_text, (1060, 0))
                if player_level == 0:
                    screen.blit(font.render("Level 1", 1, (255, 255, 255)), (1070, 30))
                elif player_level == 1:
                    screen.blit(font.render("Level 2", 1, (255, 255, 255)), (1070, 30))
            else:
                screen.blit(youwon, (500, 50))
                screen.blit(score_text, (500, 100))
                end = True

        else:
            end = True
            screen.blit(score_text, (500, 100))
            screen.blit(youlost, (500, 50))


        clock.tick(60)

        pygame.display.flip()

    pygame.quit()

main()
