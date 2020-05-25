import pygame

from ninja_settings import ninja

from ninja_settings import first_player
from ninja_settings import second_player
from ninja_settings import third_player
from ninja_settings import fourth_player
from ninja_settings import fifth_player
from ninja_settings import sixth_player


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

        window.blit(ninja('ninja/sasori.png'), (first_player(100, 750)))
        window.blit(ninja('ninja/sasori.png'), (second_player(350, 750)))
        window.blit(ninja('ninja/sasori.png'), (third_player(650, 750)))
        window.blit(ninja('ninja/sasori.png'), (fourth_player(1050, 700)))
        window.blit(ninja('ninja/sasori.png'), (fifth_player(1250, 750)))
        window.blit(ninja('ninja/sasori.png'), (sixth_player(1500, 700)))

        pygame.display.update()

    pygame.quit()
