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
        self.multipl_jump = 1.0
        self.multipl_fall = 0.0

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
        n, turpl = self.chek_collision(o_g)
        if self.jump:
            self.t_fall = 0
            self.jumpf()
        elif n:
            self.multipl_fall = 0.0
            self.rect.y = turpl[0].rect.y - self.rect[3]
        else:
            self.fall()

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
        self.multipl_fall = 0.0
        self.rect.y -= Physics.V_jump * self.multipl_jump
        self.multipl_jump -= 0.1
        if self.multipl_jump <= 0:
            self.multipl_jump = 1.0
            self.jump = False


    def fall(self):
        self.rect.y += Physics.g * self.multipl_fall
        self.multipl_fall += 0.1

    def chek_collision(self, o_g):
        blocks = pygame.sprite.spritecollide(self, o_g, False)
        TrueOrFalse = False
        if len(blocks) != 0:
            TrueOrFalse = True
            top = blocks[0]
            right = blocks[0]
            left = blocks[0]
            down = blocks[0]
            for i in blocks:
                if i.rect.y > self.rect.y + self.rect[1] and top.rect.y > i.rect.y + i.rect[1]:
                     top = i
        if TrueOrFalse:
            return TrueOrFalse, (top, down, right, left)
        else:
            return TrueOrFalse, None


class Dirth(pygame.sprite.Sprite):
    dirth = load_image('dirth.png')

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = Dirth.dirth
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = reformat_coords(x, y)


class Physics():
    V_jump = 25
    g = 10
    V_mario = 6