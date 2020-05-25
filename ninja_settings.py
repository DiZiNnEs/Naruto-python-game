import pygame

speed = 5


def ninja(file):
    return pygame.image.load(file)


def first_player(x, y):
    window = pygame.display.set_mode()
    window.blit(ninja('back/background.jpg'), (0, 0))

    def ninja_move_x(x):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            x -= speed
            window.blit(ninja('back/blue-chakra.png'), (25, 490))
        return x

    def ninja_move_y(y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            y += speed
            window.blit(ninja('back/black-chakra.png'), (25, 480))
        return y

    return ninja_move_x(x), ninja_move_y(y)


def second_player(x, y):
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_e]:
            x -= speed
        return x

    def ninja_move_y(y):
        if keys[pygame.K_f]:
            y += speed
        return y

    return ninja_move_x(x), ninja_move_y(y)


def third_player(x, y):
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_t]:
            x -= speed
        return x

    def ninja_move_y(y):
        if keys[pygame.K_h]:
            y += speed
        return y

    return ninja_move_x(x), ninja_move_y(y)


def fourth_player(x, y):
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_u]:
            x -= speed
        return x

    def ninja_move_y(y):
        if keys[pygame.K_k]:
            y += speed
        return y

    return ninja_move_x(x), ninja_move_y(y)


def fifth_player(x, y):
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_o]:
            x -= speed
        return x

    def ninja_move_y(y):
        if keys[pygame.K_p]:
            y += speed
        return y

    return ninja_move_x(x), ninja_move_y(y)


def sixth_player(x, y):
    keys = pygame.key.get_pressed()

    def ninja_move_x(x):
        if keys[pygame.K_KP_MULTIPLY]:
            x -= speed
        return x

    def ninja_move_y(y):
        if keys[pygame.K_KP_MINUS]:
            y += speed
        return y

    return ninja_move_x(x), ninja_move_y(y)
