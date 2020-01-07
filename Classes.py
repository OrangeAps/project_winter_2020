import pygame
from MiscellDefAndVars import load_image, format_size, reformat_coords


class Mario(pygame.sprite.Sprite):
    mario_r = load_image('mario_r.png', -1)
    mario_l = load_image('mario_l.png', -1)
    mario_run_r = load_image('mario_run_r.png', -1)
    mario_run_l = load_image('mario_run_l.png', -1)

    def __init__(self, x, y, group):
        super().__init__(group)
        self.group = group
        self.life = 10
        self.image = Mario.mario_r
        self.image_run = Mario.mario_run_r
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = reformat_coords(x, y)
        self.jump = False
        self.run = False
        self.direct = True # True - право, False - лево
        self.frames_for_run_r = self.cut_sheet(Mario.mario_run_r, 4, 2)
        self.frames_for_run_l = self.cut_sheet(Mario.mario_run_l, 4, 2)
        self.frames_run = 8
        self.current_frame = 0
        self.collision = False
        self.t_jump = 0
        self.t_fall = 0

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

    def update_coords(self, o_g):
        if self.jump:
            self.t_fall = 0
            self.jumpf()
        else:
            self.fall(o_g)

    def update(self):
        if self.run:
            self.current_frame = (self.current_frame + 1) % self.frames_run
            if self.direct:
                self.image = self.frames_for_run_r[self.current_frame]
            else:
                self.image = self.frames_for_run_l[self.current_frame]
        else:
            if self.direct:
                self.image = self.mario_r
            else:
                self.image = self.mario_l

    def jumpf(self):
        v = Physics.V_mario
        g = Physics.g
        t = self.t_jump

        Y = round(v * t - (g * t ** 2) / 2)
        if Y > 0:
            self.rect.y -= Y
        if Y <= 0:
            self.t_jump = 0
            self.jump = False

    def fall(self, o_g):
        g = Physics.g
        t = self.t_fall

        Y = round((g * (t / 1000) ** 2) / 2)
        self.rect.y += Y


class Dirth(pygame.sprite.Sprite):
    dirth = load_image('dirth.png')

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = Dirth.dirth
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = reformat_coords(x, y)


class Physics():
    V_jump = 23
    g = 100
    V_mario = 6