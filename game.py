import pygame


def start_game():
    pygame.init()
    window = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption('Naruto: Chakra')

    player = pygame.image.load('ninja/deidara.png')
    background = pygame.image.load('back/background.jpg')
    x = 500
    y = 500
    speed = 50

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= speed
        elif keys[pygame.K_RIGHT]:
            x += speed
        elif keys[pygame.K_UP]:
            y -= speed
        elif keys[pygame.K_DOWN]:
            y += speed

        window.blit(background, (0, 0))
        window.blit(player, (x, y))

        pygame.display.update()

    pygame.quit()
