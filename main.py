import pygame
from game_script import load as load_script
from win_choose_lvl import load as load_choose_lvl
from MiscellDefAndVars import load_image, C_BLACK, XLenWin, YLenWin, C_GREEN_TEXT


pygame.init()
screen = pygame.display.set_mode((XLenWin, YLenWin))
pygame.display.set_caption('Super Mario')
pygame.display.set_icon(load_image('icon.png'))
screen.blit(pygame.transform.scale(load_image('fon_general_win.jpg'), (XLenWin, YLenWin)), (0, 0))
fon = pygame.font.Font(None, 25)
text = fon.render('Press any key to play', 0, C_GREEN_TEXT)
text_x = XLenWin // 2 - text.get_width() // 2
text_y = 400
text_w = text.get_width()
text_h = text.get_height()
start = 0
screen.blit(text, (text_x, text_y))
pygame.draw.rect(screen, C_GREEN_TEXT, (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 2)
while start == 0:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            start = 2
        if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
            start = 1
    pygame.display.flip()
if start == 1:
    screen.fill(C_BLACK)
    lvl = load_choose_lvl(screen)
    load_script(screen, lvl)
elif start == 2:
    pygame.quit()
    exit('закрыт main')