import pygame

from src.ninja_settings import ninja

from .move_settings import move_for_five_players as move


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

        window.blit(ninja('ninja/pain.png'), (move.first_player(100, 750)))
        window.blit(ninja('ninja/naruto.png'), (move.second_player(400, 750)))
        window.blit(ninja('ninja/itachi2.png'), (move.third_player(800, 750)))
        window.blit(ninja('ninja/shikamaru.png'), (move.fourth_player(1200, 750)))
        window.blit(ninja('ninja/sasori.png'), (move.fifth_player(1500, 750)))

        pygame.display.update()

    pygame.quit()
