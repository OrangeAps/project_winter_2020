import pygame, os
from MiscellDefAndVars import load_image, C_BLACK


def load(screen):
    return main(screen)


def main(screen):
    screen.fill(C_BLACK)
    lvl = str()
    run = True
    bg = load_image('fon_chose_lvl.png')
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        screen.fill(C_BLACK)
        screen.blit(bg, (0, 0))
    return lvl