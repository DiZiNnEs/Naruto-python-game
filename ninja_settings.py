import pygame


def ninja(file):
    return pygame.image.load(file)


def ninja_move_y(y):
    keys = pygame.key.get_pressed()
    speed = 5
    if keys[pygame.K_LEFT]:
        y -= speed
    elif keys[pygame.K_RIGHT]:
        y += speed
    return y


def ninja_move_x(x):
    keys = pygame.key.get_pressed()
    speed = 5
    if keys[pygame.K_UP]:
        x -= speed
    elif keys[pygame.K_DOWN]:
        x += speed
    return x


def ninja_move(x):
    keys = pygame.key.get_pressed()
    speed = 5
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    return x


def ninja_move2(y):
    keys = pygame.key.get_pressed()
    speed = 5
    if keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    return y


def ninja_move_r(x):
    keys = pygame.key.get_pressed()
    speed = 50
    if keys[pygame.K_a]:
        x -= speed
    elif keys[pygame.K_d]:
        x += speed
    return x


def ninja_move2_r(y):
    keys = pygame.key.get_pressed()
    speed = 50
    if keys[pygame.K_w]:
        y -= speed
    elif keys[pygame.K_s]:
        y += speed
    return y
