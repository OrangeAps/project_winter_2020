import pygame
from MiscellDefAndVars import EventMarioRun, MarioFrameRate, lvl
from MiscellDefAndVars import sky, XLenWin, YLenWin, clock, FrameRate, EventFps, FPS
from Classes import Mario, Dirth, Brick


def main(screen, lvl):
    pygame.time.set_timer(EventFps, FrameRate)
    pygame.time.set_timer(EventMarioRun, MarioFrameRate)
    mario_group = pygame.sprite.Group()
    obstructions_group = pygame.sprite.Group()
    run = True
    mario = load_lvl(lvl, mario_group, obstructions_group)
    while run:
        mario.run = False
        mario.collision = False
        if mario.right:
            mario.last_direct = Mario.rightv
        elif mario.left:
            mario.last_direct = Mario.leftv
        mario.right, mario.left = False, False
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            mario.left = True
            mario.run = True
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            mario.right = True
            if mario.run:
                mario.run = False
            else:
                mario.run = True
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or mario.rect.y > 1000:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                mario.right = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                mario.left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                mario.jump = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                mario.down = True
            if event.type == EventFps:
                obstructions_group.draw(screen)
                mario_group.draw(screen)
                pygame.display.flip()
                screen.fill(sky)
            if event.type == EventMarioRun:
                mario.update()
        mario.update_coords(obstructions_group)
        clock.tick(FPS)
    pygame.quit()
    exit('закрыт код')


def load(screen, lvl):
    main(screen, lvl)


def load_lvl(lvl, m_g, o_g):
    with open('levels/lvl_' + lvl + '.txt', encoding='utf8') as file:
        lines = [_.strip() for _ in file]
    for _ in range(1, len(lines)):
        if len(lines[_]) != int(lines[0]):
            lines[_] = lines[_] + '_' * (int(lines[0]) - len(lines[_]))
    for i in range(1, len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '_':
                pass
            if lines[i][j] == '#':
                Dirth(j, i, o_g)
            if lines[i][j] == '$':
                Brick(j, i, o_g)
            if lines[i][j] == '@':
                mario = Mario(j, i - 1, m_g)
    return mario


if __name__ == '__main__':
    screen = pygame.display.set_mode((XLenWin, YLenWin))
    screen.fill(sky)
    main(screen, lvl)