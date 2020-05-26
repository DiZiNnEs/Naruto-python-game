import pygame

from ninja_settings import ninja

from ninja_settings import first_player
from ninja_settings import second_player
from ninja_settings import third_player
from ninja_settings import fourth_player

from .move_settings import move_for_four_players as move


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

        # window.blit(ninja('ninja/sasori.png'), (first_player(100, 750)))
        # window.blit(ninja('ninja/sasori.png'), (second_player(500, 700)))
        # window.blit(ninja('ninja/sasori.png'), (third_player(1200, 750)))
        # window.blit(ninja('ninja/sasori.png'), (fourth_player(1700, 700)))

        window.blit(ninja('ninja/itachi.png'), (move.first_player(100, 650)))
        window.blit(ninja('ninja/itachi.png'), (move.second_player(500, 650)))
        window.blit(ninja('ninja/itachi.png'), (move.third_player(1200, 650)))
        window.blit(ninja('ninja/itachi.png'), (move.fourth_player(1700, 650)))

        pygame.display.update()

    pygame.quit()
