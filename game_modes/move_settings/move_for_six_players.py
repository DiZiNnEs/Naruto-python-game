import pygame

speed = 5


def ninja(file):
    return pygame.image.load(file)


def first_player(x, y):
    global window
    window = pygame.display.set_mode()
    window.blit(ninja('back/background.jpg'), (0, 0))
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_q]:
            x -= speed
            window.blit(ninja('back/blue-chakra.png'), (20, 550))
        return x

    def ninja_move_y(y):
        if keys[pygame.K_s]:
            y += speed
            window.blit(ninja('back/black-chakra.png'), (20, 550))
        return y

    return ninja_move_x(x), ninja_move_y(y)


def second_player(x, y):
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_e]:
            x -= speed
            window.blit(ninja('back/blue-chakra.png'), (270, 550))
        return x

    def ninja_move_y(y):
        if keys[pygame.K_f]:
            y += speed
            window.blit(ninja('back/black-chakra.png'), (270, 550))
        return y

    return ninja_move_x(x), ninja_move_y(y)


def third_player(x, y):
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_t]:
            x -= speed
            window.blit(ninja('back/blue-chakra.png'), (585, 550))
        return x

    def ninja_move_y(y):
        if keys[pygame.K_h]:
            y += speed
            window.blit(ninja('back/black-chakra.png'), (585, 550))
        return y

    return ninja_move_x(x), ninja_move_y(y)


def fourth_player(x, y):
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_u]:
            x -= speed
            window.blit(ninja('back/blue-chakra.png'), (970, 550))
        return x

    def ninja_move_y(y):
        if keys[pygame.K_k]:
            y += speed
            window.blit(ninja('back/black-chakra.png'), (970, 550))
        return y

    return ninja_move_x(x), ninja_move_y(y)


def fifth_player(x, y):
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_o]:
            x -= speed
            window.blit(ninja('back/blue-chakra.png'), (1150, 550))
        return x

    def ninja_move_y(y):
        if keys[pygame.K_p]:
            y += speed
            window.blit(ninja('back/black-chakra.png'), (1150, 550))

        return y

    return ninja_move_x(x), ninja_move_y(y)


def sixth_player(x, y):
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_KP_MULTIPLY]:
            x -= speed
            window.blit(ninja('back/blue-chakra.png'), (1420, 550))
        return x

    def ninja_move_y(y):
        if keys[pygame.K_KP_MINUS]:
            y += speed
            window.blit(ninja('back/black-chakra.png'), (1420, 550))

        return y

    return ninja_move_x(x), ninja_move_y(y)
