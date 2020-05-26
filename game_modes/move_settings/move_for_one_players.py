import pygame

speed = 5


def ninja(file):
    return pygame.image.load(file)


def first_player(x, y):
    window = pygame.display.set_mode()
    window.blit(ninja('back/background.jpg'), (0, 0))
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_q]:
            x -= speed
            window.blit(ninja('back/blue-chakra.png'), (25, 490))
        return x

    def ninja_move_y(y):
        if keys[pygame.K_s]:
            y += speed
            window.blit(ninja('back/black-chakra.png'), (25, 480))
        return y

    return ninja_move_x(x), ninja_move_y(y)
