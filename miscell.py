import os, pygame


C_BLACK = pygame.Color('black')
sky = pygame.Color(127, 199, 255)
XLenWin = 800
YLenWin = 450
FPS = 100
clock = pygame.time.Clock()


screen = pygame.display.set_mode((XLenWin, YLenWin))


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