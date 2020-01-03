import pygame
from MiscellDefAndVars import load_image, EventMarioRun, MarioFrameRate
from MiscellDefAndVars import sky, XLenWin, YLenWin, clock, FrameRate, F_jump, g, format_size, EventFps, FPS

class Mario(pygame.sprite.Sprite):
    mario_r = load_image('mario_r.png', -1)
    mario_l = load_image('mario_l.png', -1)
    mario_run_r = load_image('mario_run_r.png', -1)
    mario_run_l = load_image('mario_run_l.png', -1)

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
        self.run = False
        self.direct = True # True - право, False - лево
        self.frames_for_run_r = self.cut_sheet(Mario.mario_run_r, 4, 2)
        self.frames_for_run_l = self.cut_sheet(Mario.mario_run_l, 4, 2)
        self.frames_run = 8
        self.current_frame = 0

    def cut_sheet(self, sheet, columns, rows):
        rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        listt = []
        for j in range(rows):
            for i in range(columns):
                frame_location = (rect.w * i, rect.h * j)
                listt.append(sheet.subsurface(pygame.Rect(
                    frame_location, rect.size)))
        listt = format_size(listt)
        return listt

    def update(self):
        self.current_frame = (self.current_frame + 1) % self.frames_run
        if self.direct:
            self.image = self.frames_for_run_r[self.current_frame]
        else:
            self.image = self.frames_for_run_l[self.current_frame]


def main(screen):
    global F_jump
    pygame.time.set_timer(EventFps, FrameRate)
    pygame.time.set_timer(EventMarioRun, MarioFrameRate)
    mario_group = pygame.sprite.Group()
    mario = Mario(mario_group)
    run = True
    while run:
        mario.run = False
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            mario.rect.x -= 3
            mario.direct = False
            mario.run = True
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            mario.rect.x += 3
            mario.direct = True
            mario.run = True
        if key[pygame.K_SPACE]:
            mario.jump = True
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
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                mario.direct = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                mario.direct = False
            if event.type == EventFps:
                mario_group.draw(screen)
                pygame.display.flip()
                screen.fill(sky)
            if event.type == EventMarioRun and mario.run:
                mario.update()
        if not mario.run:
            if mario.direct:
                mario.image = Mario.mario_r
            else:
                mario.image = Mario.mario_l
        clock.tick(FPS)
    pygame.quit()
    exit('закрыт код')


def load(screen):
    main(screen)


if __name__ == '__main__':
    screen = pygame.display.set_mode((XLenWin, YLenWin))
    screen.fill(sky)
    main(screen)