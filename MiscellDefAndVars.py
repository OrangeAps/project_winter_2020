import os, pygame


C_BLACK = pygame.Color('black')
C_GREEN_TEXT = pygame.Color(84, 255, 159)
C_BLUE = pygame.Color(31, 174, 233)
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
MarioFrameRate = 128
right = 'r'
left = 'left'


screen = pygame.display.set_mode((XLenWin, YLenWin))
lvl = 1


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


def process_coords(yw, ww, hw, xm, ym, i):
    i += 1
    n = -1
    if ym >= yw and ym <= yw + hw:
        xw = 15
        for _ in range(i):
            if xm >= xw and xm <= xw + ww:
                if _ == i - 1:
                    n = 0
                else:
                    n = _ + 1
            xw += ww + 15
    return n