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
        self.score = 0
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
        self.jumps = 0
        self.m = 1

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

    def update_coords(self, o_g, c_o, b_g, e_g):
        n, turpl = self.chek_collision(o_g)
        enemys = pygame.sprite.spritecollide(self, e_g, False)
        if len(enemys) != 0:
            for i in enemys:
                self.life -= 1
                self.jump = True
                if i.rect.x < self.rect.x:
                    o_g.update(-Physics.V_mario)
                    c_o.update(-Physics.V_mario)
                    b_g.update(-Physics.V_mario)
                    e_g.update(-Physics.V_mario)
                    self.m = 0
                if i.rect.x > self.rect.x:
                    o_g.update(Physics.V_mario)
                    c_o.update(Physics.V_mario)
                    b_g.update(Physics.V_mario)
                    e_g.update(Physics.V_mario)
                    self.m = 2
        if self.down and self.rect.y < self.coords_block + 32:
            n = False
        if self.rect.y >= self.coords_block + 32:
            self.down = False
        if n:
            self.jumps = 0
            if self.left and turpl[2]:
                o_g.update(Physics.V_mario)
                c_o.update(Physics.V_mario)
                b_g.update(Physics.V_mario)
                e_g.update(Physics.V_mario)
            if self.right and turpl[1]:
                o_g.update(-Physics.V_mario)
                c_o.update(-Physics.V_mario)
                b_g.update(-Physics.V_mario)
                e_g.update(-Physics.V_mario)
            if self.jump:
                self.jumpf(self.m, o_g, c_o, b_g, e_g)
            else:
                try:
                    self.rect.y = turpl[0].rect.y - (self.rect.height - 1)
                    self.coords_block = turpl[0].rect.y
                except:
                    self.fall()
        else:
            if self.left:
                o_g.update(Physics.V_mario)
                c_o.update(Physics.V_mario)
                b_g.update(Physics.V_mario)
                e_g.update(Physics.V_mario)
            if self.right:
                o_g.update(-Physics.V_mario)
                c_o.update(-Physics.V_mario)
                b_g.update(-Physics.V_mario)
                e_g.update(-Physics.V_mario)
            if self.jump:
                self.jumpf(self.m, o_g, c_o, b_g, e_g)
            else:
                self.fall()
        coins = pygame.sprite.spritecollide(self, c_o, True)
        self.score += len(coins)

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

    def jumpf(self, n, o_g, c_o, b_g, e_g): # n = 0 - влево, n = 1 - стой, n = 2 - вправо
        self.multipl_fall = 0.0
        self.rect.y -= Physics.V_jump * self.multipl_jump
        self.multipl_jump -= 0.1
        if n == 0:
            o_g.update(-Physics.V_mario)
            c_o.update(-Physics.V_mario)
            b_g.update(-Physics.V_mario)
            e_g.update(-Physics.V_mario)
        if n == 2:
            o_g.update(-Physics.V_mario)
            c_o.update(-Physics.V_mario)
            b_g.update(-Physics.V_mario)
            e_g.update(-Physics.V_mario)
        if self.multipl_jump <= 0:
            self.multipl_jump = 1.0
            self.jump = False
            self.jumps += 1


    def fall(self):
        self.rect.y += Physics.g * self.multipl_fall
        self.multipl_fall += 0.1

    def chek_collision(self, o_g):
        blocks = pygame.sprite.spritecollide(self, o_g, False)
        TrueOrFalse = False
        if len(blocks) != 0:
            TrueOrFalse = True
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
            return TrueOrFalse, (down, right, left)
        else:
            return TrueOrFalse, None


class Dirth(pygame.sprite.Sprite):
    dirth = load_image('dirth.png')

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = Dirth.dirth
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = reformat_coords(x, y)

    def update(self, x):
        self.rect.x += x


class Brick(pygame.sprite.Sprite):
    brick = load_image('brick.png')

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = Brick.brick
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = reformat_coords(x, y)

    def update(self, x):
        self.rect.x += x


class Coin(pygame.sprite.Sprite):
    coin = load_image('coin.png', -1)

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = Coin.coin
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = reformat_coords(x, y)

    def update(self, x):
        self.rect.x += x


class BlockForEnemys(pygame.sprite.Sprite):
    img = load_image('block_invis.png')

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = BlockForEnemys.img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = reformat_coords(x, y)

    def update(self, x):
        self.rect.x += x


class EnemyTurtle(pygame.sprite.Sprite):
    turtle_r = load_image('turtle_r.png', -1)
    turtle_l = load_image('turtle_l.png', -1)

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = EnemyTurtle.turtle_r
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = reformat_coords(x, y)
        self.direct = True  # true - вправо, false - влево

    def update(self, x):
        self.rect.x += x

    def update_coords(self, g):
        n = self.chek_collision(g)
        if n:
            if self.direct:
                self.direct = False
                self.image = EnemyTurtle.turtle_l
            else:
                self.direct = True
                self.image = EnemyTurtle.turtle_r
        if not self.direct:
            self.rect.x -= Physics.V_enemy
        if self.direct:
            self.rect.x += Physics.V_enemy

    def chek_collision(self, g):
        blocks = pygame.sprite.spritecollide(self, g, False)
        n = False
        if len(blocks) != 0:
            n = True
        return n


class EnemyMushrum(pygame.sprite.Sprite):
    img = load_image('angry_mushrum.png', -1)

    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = EnemyMushrum.img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = reformat_coords(x, y)
        self.direct = True  # true - вправо, false - влево

    def update(self, x):
        self.rect.x += x

    def update_coords(self, g):
        n = self.chek_collision(g)
        if n:
            if self.direct:
                self.direct = False
            else:
                self.direct = True
        if not self.direct:
            self.rect.x -= Physics.V_enemy
        if self.direct:
            self.rect.x += Physics.V_enemy

    def chek_collision(self, g):
        blocks = pygame.sprite.spritecollide(self, g, False)
        n = False
        if len(blocks) != 0:
            n = True
        return n


class Physics():
    V_jump = 25
    g = 9 
    V_mario = 6
    V_enemy = 2