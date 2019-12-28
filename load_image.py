import os, pygame


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