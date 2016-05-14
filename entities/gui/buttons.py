from displays.levels.level1 import Level1
from entities.entity import Entity
import constants as C
import pygame
class Button(Entity):
    def __init__(self,rect,image):
        super().__init__(rect,image)


class PlayButton(Button):
    def __init__(self):
        image = pygame.image.load('lib/gui/buttons/play_button.png')
        super().__init__(image.get_rect(),image)

    def onMouseHover(self):
        pass

    def onLeftMouseDown(self):
        C.GAME.display = Level1()
