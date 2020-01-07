import pygame, os
from MiscellDefAndVars import load_image


def load(screen):
    return main(screen)


def main(screen):
    lvl = str()
    run = True
    bg = load_image('fon_chose_lvl.png')
    while run:
        screen.blit(bg, (0, 0))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        screen.blit(bg, (0, 0))
    return lvl