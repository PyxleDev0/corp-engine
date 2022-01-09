import pygame
from ..coreContent import openErrorWindow

class Assets(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = 'Assets'
        self.type = 'Assets'
        self.images = {
            'player': pygame.image.load('res/images/player.png').convert_alpha(),
            'dev_close': pygame.image.load('res/images/dev_close.png').convert(),
            'test': pygame.image.load('res/images/test.png').convert(),
            'checkbox_true': pygame.image.load('res/images/engine/checkbox_true.png').convert_alpha(),
            'checkbox_false': pygame.image.load('res/images/engine/checkbox_false.png').convert_alpha(),
            'icon': pygame.image.load('res/images/icon.png').convert_alpha()
        }
        self.fonts = {
            'hp_simplified': pygame.font.Font('res/fonts/hp-simplified.ttf', 15),
            'roboto_mono': pygame.font.Font('res/fonts/roboto-mono.ttf', 15)
        }
        self.sounds = {
        }
    
    def getImage(self, name):
        try:
            return self.images[name].copy()
        except KeyError:
            openErrorWindow(f'no asset found named "{name}".', self.parent.parent)
