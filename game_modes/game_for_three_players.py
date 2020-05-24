import pygame

from ninja_settings import ninja
from ninja_settings import ninja_move_x
from ninja_settings import ninja_move_y


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
        # window.blit(ninja('ninja/deidara.png'), (x, y))

        window.blit(ninja('ninja/sasori.png'), (ninja_move_y(100), ninja_move_x(750)))
        window.blit(ninja('ninja/sasori.png'), (ninja_move_y(900), ninja_move_x(750)))
        window.blit(ninja('ninja/sasori.png'), (ninja_move_y(1600), ninja_move_x(750)))

        pygame.display.update()

    pygame.quit()
