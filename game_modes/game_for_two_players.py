import pygame

from ninja_settings import ninja

from ninja_settings import first_player
from ninja_settings import second_player


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
        window.blit(ninja('ninja/itachi.png'), (first_player(100, 600)))
        window.blit(ninja('ninja/shikamaru.png'), (second_player(1600, 600)))

        pygame.display.update()

    pygame.quit()
