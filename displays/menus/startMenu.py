from displays.display import Display
from entities.entity import Entity
from entities.gui import buttons
import pygame
import constants as C
class StartMenu(Display):
    def __init__(self):
        # Welcome Text
        font = pygame.font.Font(None, 36)
        text = font.render("Welcome", 1, (255,255,255))
        textpos = text.get_rect()
        textpos.centerx = C.GAME.SCREEN.get_rect().centerx
        textpos.centery = C.GAME.SCREEN.get_rect().centery *.15
        text = Entity(textpos,text)

        # Play Button
        playButton = buttons.PlayButton()
        playButton.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        playButton.rect.top = C.GAME.SCREEN.get_rect().centery * .25

        entities = [text,playButton]
        super().__init__(C.GAME.SCREEN,entities)
