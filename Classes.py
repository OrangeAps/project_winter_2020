import pygame
from MiscellDefAndVars import load_image, format_size, reformat_coords, right, left


class Mario(pygame.sprite.Sprite):
    mario_r = load_image('mario_r.png', -1)
    mario_l = load_image('mario_l.png', -1)
    mario_run_r = load_image('mario_run_r.png', -1)
    mario_run_l = load_image('mario_run_l.png', -1)
    rightv = right
    leftv = left

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
        self.right = True
        self.left = False
        self.down = False
        self.frames_for_run_r = self.cut_sheet(Mario.mario_run_r, 4, 2)
        self.frames_for_run_l = self.cut_sheet(Mario.mario_run_l, 4, 2)
        self.frames_run = 8
        self.current_frame = 0
        self.collision = False
        self.multipl_jump = 1.0
        self.multipl_fall = 0.0
        self.last_direct = Mario.rightv
        self.coords_block = int()

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
        if self.down and self.rect.y < self.coords_block + 32:
            n = False
        if self.rect.y >= self.coords_block + 32:
            self.down = False
        if n:
            if self.left and turpl[3]:
                self.rect.x -= Physics.V_mario
            if self.right and turpl[2]:
                self.rect.x += Physics.V_mario
            if self.jump:
                self.jumpf()
            else:
                self.rect.y = turpl[1].rect.y - (self.rect.height - 1)
                self.coords_block = turpl[1].rect.y
        else:
            if self.left:
                self.rect.x -= Physics.V_mario
            if self.right:
                self.rect.x += Physics.V_mario
            if self.jump:
                self.jumpf()
            else:
                self.fall()

    def update(self):
        if not self.run:
            if self.right:
                self.image = self.mario_r
            elif self.left:
                self.image = self.mario_l
            else:
                if self.last_direct == self.rightv:
                    self.image = self.mario_r
                elif self.last_direct == self.leftv:
                    self.image = self.mario_l
        if self.run:
            self.current_frame = (self.current_frame + 1) % self.frames_run
            if self.right:
                self.image = self.frames_for_run_r[self.current_frame]
            elif self.left:
                self.image = self.frames_for_run_l[self.current_frame]

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
            top = None
            right = True
            left = True
            down = None
            for i in blocks:
                if i.rect.y > self.rect.y + (self.rect.height - 32) and (down is None or down.rect.y > i.rect.y + i.rect.height):
                    down = i
                if i.rect.x + (i.rect.width - 10) < self.rect.x and i.rect.y + i.rect.height <= self.rect.y + (self.rect.height - 3) and left is True:
                    left = False
                if i.rect.x > self.rect.x + (self.rect.width - 10) and i.rect.y + i.rect.height <= self.rect.y + (self.rect.height - 3) and right is True:
                    right = False
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


class Brick(pygame.sprite.Sprite):
    brick = load_image('brick.png')

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = Brick.brick
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = reformat_coords(x, y)


class Physics():
    V_jump = 25
    g = 10
    V_mario = 6