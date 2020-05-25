import pygame

speed = 5


def ninja(file):
    return pygame.image.load(file)


def ninja_move_x(x):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        x -= speed
    return x


def ninja_move_y(y):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        y += speed
    return y


def second_player():
    def ninja_move_x(x):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            x -= speed
        return x

    def ninja_move_y(y):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            y += speed
        return y
