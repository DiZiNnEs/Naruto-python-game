import pygame

from ninja_settings import ninja

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

        window.blit(ninja('ninja/itachi2.png'), (move.first_player(100, 650)))
        window.blit(ninja('ninja/naruto.png'), (move.second_player(500, 650)))
        window.blit(ninja('ninja/shikamaru.png'), (move.third_player(1200, 650)))
        window.blit(ninja('ninja/pain.png'), (move.fourth_player(1700, 650)))

        pygame.display.update()

    pygame.quit()
