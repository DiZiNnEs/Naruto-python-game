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

        window.blit(ninja('back/background.jpg'), (0, 0))
        window.blit(ninja('ninja/shikamaru.png'), (ninja_move_r(100), ninja_move2_r(600)))
        window.blit(ninja('ninja/shikamaru.png'), (ninja_move_r(1600), ninja_move2_r(600)))

        pygame.display.update()

    pygame.quit()
