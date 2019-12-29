import pygame
from game_script import load as load_script
from miscell import load_image, C_BLACK, XLenWin, YLenWin

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
    screen.fill(C_BLACK)
    load_script(screen)
elif start == 2:
    pygame.quit()
    exit('закрыто')