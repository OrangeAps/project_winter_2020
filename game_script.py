import pygame
from MiscellDefAndVars import EventMarioRun, MarioFrameRate, lvl, C_BLACK, load_image
from MiscellDefAndVars import sky, XLenWin, YLenWin, clock, FrameRate, EventFps, FPS
from Classes import Mario, Dirth, Brick, Coin, BlockForEnemys, EnemyTurtle, EnemyMushrum


def main(screen, lvl):
    fon = pygame.font.Font(None, 50)
    pygame.time.set_timer(EventFps, FrameRate)
    pygame.time.set_timer(EventMarioRun, MarioFrameRate)
    mario_group = pygame.sprite.Group()
    obstructions_group = pygame.sprite.Group()
    coin_group = pygame.sprite.Group()
    block_for_enemy_group = pygame.sprite.Group()
    enemys_g = pygame.sprite.Group()
    heath = pygame.sprite.Sprite()
    heath.image = load_image('hearth.png', -1)
    heath.rect = heath.image.get_rect()
    heath_g = pygame.sprite.Group(heath)
    heath.rect.x, heath.rect.y = 0, YLenWin - 64
    coin = pygame.sprite.Sprite()
    coin.image = load_image('coin.png', -1)
    coin.rect = coin.image.get_rect()
    coin.rect.x, coin.rect.y = 0, YLenWin - 32
    coin_g = pygame.sprite.Group(coin)
    run = True
    mario = load_lvl(lvl, mario_group, obstructions_group, coin_group, block_for_enemy_group, enemys_g)
    x = mario.rect.x
    mario.rect.x = XLenWin // 2 - mario.rect.width // 2
    obstructions_group.update(mario.rect.x - x)
    coin_group.update(mario.rect.x - x)
    block_for_enemy_group.update(mario.rect.x - x)
    enemys_g.update(mario.rect.x - x)
    h_text_x = 32
    h_text_y = YLenWin - 64
    text_x = 32
    text_y = YLenWin - 32
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
            if event.type == pygame.QUIT or mario.rect.y > YLenWin or mario.life <= 0:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                mario.right = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                mario.left = True
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                if mario.jumps <= 2:
                    mario.jump = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                mario.down = True
            if event.type == EventFps:
                screen.fill(sky)
                t_h = fon.render('X' + str(mario.life), 0, C_BLACK)
                screen.blit(t_h, (h_text_x, h_text_y))
                text = fon.render('Х' + str(mario.score), 0, C_BLACK)
                screen.blit(text, (text_x, text_y))
                coin_g.draw(screen)
                heath_g.draw(screen)
                obstructions_group.draw(screen)
                coin_group.draw(screen)
                enemys_g.draw(screen)
                mario_group.draw(screen)
                pygame.display.flip()
            if event.type == EventMarioRun:
                mario.update()
        mario.update_coords(obstructions_group, coin_group, block_for_enemy_group, enemys_g)
        for _ in enemys_g:
            _.update_coords(block_for_enemy_group)
        clock.tick(FPS)
    if event.type == pygame.QUIT:
        pygame.quit()
        exit('закрыто')
    elif mario.rect.y > YLenWin or mario.life <= 0:
        pygame.quit()
        exit('МАРИО ПОМЕР')




def load(screen, lvl):
    main(screen, lvl)


def load_lvl(lvl, m_g, o_g, c_o, en_b_g, en_g):
    with open('levels/lvl_' + str(lvl) + '.txt', encoding='utf8') as file:
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
            if lines[i][j] == '0':
                Coin(j, i, c_o)
            if lines[i][j] == '+':
                BlockForEnemys(j, i, en_b_g)
            if lines[i][j] == 'T':
                EnemyTurtle(j, i, en_g)
            if lines[i][j] == 'M':
                EnemyMushrum(j, i, en_g)
    return mario


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((XLenWin, YLenWin))
    screen.fill(sky)
    main(screen, lvl)