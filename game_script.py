import pygame
from miscell import load_image
from miscell import C_BLACK, XLenWin, YLenWin


class Mario(pygame.sprite.Sprite):
    mario = load_image('mario.png')

    def __init__(self, group):
        super.__init__(group)
        self.image = Mario.mario
        self.x = 10
        self.y = 10


def load(screen):
    main(screen)


def main(screen):
    mario_group = pygame.sprite.Group()
    mario = Mario(mario_group)
    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        mario_group.draw(screen)
    pygame.quit()
    exit('тут был код')


if __name__ == '__main__':
    screen = pygame.display.set_mode((XLenWin, YLenWin))
    screen.fill(C_BLACK)
    load(screen)