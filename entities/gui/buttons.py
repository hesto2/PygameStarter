from displays.levels.level1 import Level1
from displays.display import Display
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
        print('hit')

    def onLeftMouseDown(self):
        C.GAME.display = Level1()

class PlayAgainButton(Button):
    font = pygame.font.Font(None, 25)
    abs_pos = (0,0)
    def __init__(self):
        text = self.font.render("Play Again", 1, (255,255,255))
        textpos = text.get_rect()
        super().__init__(textpos,text)

    def tick(self):
        self.image = self.font.render("Play Again", 1, (255,255,255))
        super().tick()

    def onMouseHover(self):
        pass

    def onLeftMouseDown(self):
        from displays.menus.startMenu import StartMenu
        C.GAME.display.reset()
