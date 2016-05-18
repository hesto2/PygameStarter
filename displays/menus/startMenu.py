from displays.display import Display
from entities.entity import Entity
from entities.gui import buttons
from tools.eztext import Input
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

        createLevelButton = buttons.CreateLevelButton()
        createLevelButton.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        createLevelButton.rect.top = C.GAME.SCREEN.get_rect().centery*.45

        textInput = Input(maxlength=20,color=C.WHITE,prompt='TEST: ')
        textInput.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        textInput.rect.top = C.GAME.SCREEN.get_rect().centery *1.5
        entities = [text,playButton,createLevelButton,textInput]
        super().__init__(C.GAME.SCREEN,entities)
