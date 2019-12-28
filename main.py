import pygame
from game_script import load as load_script
from load_image import load_image


# переменные
XLenWin = 800
YLenWin = 450

# дерево кода
screen = pygame.display.set_mode((XLenWin, YLenWin))
screen.blit(pygame.transform.scale(load_image('fon_general_win.jpg'), (XLenWin, YLenWin)), (0, 0))
start = 0
while start == 0:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            start = 2
        if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
            start = 1
    pygame.display.flip()
if start == 1:
    load_script()
elif start == 2:
    pygame.quit()
    exit('закрыто')