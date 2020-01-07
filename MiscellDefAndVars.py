import os, pygame


C_BLACK = pygame.Color('black')
C_GREEN_TEXT = pygame.Color(84, 255, 159)
sky = pygame.Color(127, 199, 255)
XLenWin = 800
YLenWin = 450
XMario = 32
YMario = 64
FrameRate = 10
EventFps = 1
FPS = 50
clock = pygame.time.Clock()
EventMarioRun = 2
MarioFrameRate = 125


screen = pygame.display.set_mode((XLenWin, YLenWin))
lvl = '1'


def load_image(name, ColorKey=None):
    fullname = os.path.join('pictures', name)
    image = pygame.image.load(fullname)
    if ColorKey is not None:
        if ColorKey == -1:
            ColorKey = image.get_at((0, 0))
        image = image.convert()
        image.set_colorkey(ColorKey)
    else:
        image = image.convert_alpha()
    return image


def format_size(ListWithImg):
    for _ in range(len(ListWithImg)):
        ListWithImg[_] = pygame.transform.scale(ListWithImg[_], (XMario, YMario))
    return ListWithImg


def reformat_coords(x, y):
    return x*32, y*32