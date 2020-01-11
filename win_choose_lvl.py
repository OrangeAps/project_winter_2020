import pygame, os
from MiscellDefAndVars import load_image, C_BLACK, XLenWin, YLenWin


def load(screen):
    return main(screen)


def main(screen):
    screen.fill(C_BLACK)
    lvl = str()
    run = True
    # bg_group = pygame.sprite.Group()
    # bg = pygame.sprite.Sprite(bg_group)
    # bg.image = load_image('fon_chose_lvl.png')
    # bg.rect = bg.image.get_rect
    bg = load_image('fon_chose_lvl.png')
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        screen.fill(C_BLACK)
        # bg_group.draw(screen)
        screen.blit(bg, (0, 0))
        pygame.display.flip()
    return lvl


if __name__ == '__main__':
    screen = pygame.display.set_mode((XLenWin, YLenWin))
    screen.fill(C_BLACK)
    main(screen)