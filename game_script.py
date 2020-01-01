import pygame
from miscell import load_image
from miscell import sky, XLenWin, YLenWin, clock, FPS, F_jump, g


class Mario(pygame.sprite.Sprite):
    mario_r = load_image('mario_r.png', -1)
    mario_l = load_image('mario_l.png', -1)
    mario_run_r = load_image('mario_run_r.png', -1)

    def __init__(self, group):
        super().__init__(group)
        self.image = Mario.mario_r
        self.image_run = Mario.mario_run_r
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 350
        self.multipl_jump = 1.0
        self.jump = False
        self.multipl_fall = 1.0


def main(screen):
    global F_jump
    mario_group = pygame.sprite.Group()
    mario = Mario(mario_group)
    run = True
    while run:
        tick = clock.tick()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            mario.rect.x -= 3
            mario.image = Mario.mario_l
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            mario.rect.x += 3
            mario.image = Mario.mario_r
        if key[pygame.K_SPACE]:
            mario.jump = True
        if tick % 1000 == 0:
            if mario.jump:
                mario.multipl_fall = 0
                if mario.multipl_jump >= 0:
                    mario.rect.y -= round(mario.multipl_jump * F_jump)
                    mario.multipl_jump -= 0.1
                else:
                    mario.multipl_jump = 1.0
                    mario.jump = False
            else:
                mario.multipl_fall += 0.1
                mario.rect.y += round(mario.multipl_fall * g)
        mario_group.draw(screen)
        if tick % 24 == 0:
            pygame.display.flip()
            screen.fill(sky)
        clock.tick(FPS)
    pygame.quit()
    exit('закрыт код')


def load(screen):
    main(screen)


if __name__ == '__main__':
    screen = pygame.display.set_mode((XLenWin, YLenWin))
    screen.fill(sky)
    main(screen)