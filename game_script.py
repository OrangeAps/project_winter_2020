import pygame
from miscell import load_image
from miscell import sky, XLenWin, YLenWin, clock, FPS


class Mario(pygame.sprite.Sprite):
    mario_r = load_image('mario_r.png', -1)
    mario_l = load_image('mario_l.png', -1)

    def __init__(self, group):
        super().__init__(group)
        self.image = Mario.mario_r
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 350


def load(screen):
    main(screen)


def main(screen):
    mario_group = pygame.sprite.Group()
    mario = Mario(mario_group)
    run = True
    while run:
        tick = clock.tick()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    mario.rect.x -= 1
                    mario.image = Mario.mario_l
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    mario.rect.x += 1
                    mario.image = Mario.mario_r
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            mario.rect.x -= 1
            mario.image = Mario.mario_l
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            mario.rect.x += 1
            mario.image = Mario.mario_r
        mario_group.draw(screen)
        if tick % 24 == 0:
            pygame.display.flip()
            screen.fill(sky)
        clock.tick(FPS)
    pygame.quit()
    exit('закрыт код')


if __name__ == '__main__':
    screen = pygame.display.set_mode((XLenWin, YLenWin))
    screen.fill(sky)
    load(screen)