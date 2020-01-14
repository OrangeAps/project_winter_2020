import pygame, os
from MiscellDefAndVars import load_image, C_BLACK, XLenWin, YLenWin, C_BLUE, process_coords


def load(screen):
    return main(screen)


def main(screen):
    screen.fill(C_BLACK)
    lvl = int()
    run = True
    bg = load_image('fon_chose_lvl.png')
    files = os.listdir('levels')
    font = pygame.font.Font(None, 75)
    while run:
        screen.fill(C_BLACK)
        screen.blit(bg, (0, 0))
        w = 100
        h = 150
        y = 100
        for i in range(len(files)):
            j = files[i].split('.')
            x = w * i + 15 * (i + 1)
            pygame.draw.rect(screen, C_BLUE, (x, y, w, h))
            text = font.render(j[0][4:], 0, C_BLACK)
            tw, th = text.get_width(), text.get_height()
            tx, ty = x + (w // 2) - (tw // 2), y + (h // 2) - (th // 2)
            screen.blit(text, (tx, ty))
        i += 1
        x = w * i + 15 * (i + 1)
        pygame.draw.rect(screen, (160, 160, 164), (x, y, w, h))
        text = font.render('+', 0, C_BLACK)
        tw, th = text.get_width(), text.get_height()
        tx, ty = x + (w // 2) - (tw // 2), y + (h // 2) - (th // 2)
        screen.blit(text, (tx, ty))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                lvl = process_coords(y, w, h, event.pos[0], event.pos[1], i)
                print(lvl)
                if lvl != -1:
                    run = False
        pygame.display.flip()
    if lvl == -1 or lvl == 0:
        pygame.quit()
        exit()
    else:
        return lvl


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((XLenWin, YLenWin))
    screen.fill(C_BLACK)
    main(screen)