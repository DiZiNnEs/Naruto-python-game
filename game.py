import pygame

from ninja_settings import ninja
from ninja_settings import ninja_move
from ninja_settings import ninja_move2

from ninja_settings import ninja_move_r
from ninja_settings import ninja_move2_r


def start_game():

    pygame.init()


    window = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption('Naruto: Chakra')



    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        x = 500
        y = 500
        speed = 50
        if keys[pygame.K_LEFT]:
            x -= speed
        elif keys[pygame.K_RIGHT]:
            x += speed
        elif keys[pygame.K_UP]:
            y -= speed
        elif keys[pygame.K_DOWN]:
            y += speed

        window.blit(ninja('back/background.jpg'), (0, 0))
        # window.blit(ninja('ninja/deidara.png'), (x, y))
        window.blit(ninja('ninja/itachi.png'), (ninja_move_r(100), ninja_move2_r(600)))
        window.blit(ninja('ninja/itachi2.png'), (ninja_move_r(300), ninja_move2_r(600)))
        window.blit(ninja('ninja/naruto_6_way.png'), (ninja_move_r(500), ninja_move2_r(600)))

        window.blit(ninja('ninja/obito.png'), (ninja_move(1700), ninja_move2(700)))
        window.blit(ninja('ninja/obito3.png'), (ninja_move(1500), ninja_move2(700)))
        window.blit(ninja('ninja/pain.png'), (ninja_move(1200), ninja_move2(700)))

        pygame.display.update()

    pygame.quit()


