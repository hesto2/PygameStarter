from entities.entity import Entity
from entities.gui import buttons
from displays.levels.level import LevelComponent
from tools.eztext import Input
import constants as C
import pygame
from entities.gui import overlays

class PauseLevel(LevelComponent):
    fadeSpeed = 5
    def __init__(self):
        screen = C.GAME.SCREEN.get_rect()
        super().__init__((screen.width*.4,screen.height*.4),entities=[])
        # Buttons

        # Reset Button
        reset = buttons.ResetButton()
        self.rect.centerx = screen.centerx
        self.rect.centery = screen.centery
        reset.rect.centerx = self.rect.width *.5
        reset.rect.centery = self.rect.height *.5
        reset.abs_pos = (self.rect.x+reset.rect.x,
                             self.rect.y+reset.rect.y)
        self.entities.append(reset)

        # Main Menu Button
        menu = buttons.MainMenuButton()
        menu.rect.centerx = self.rect.width *.5
        menu.rect.centery = self.rect.height *.7
        menu.abs_pos = (self.rect.x+menu.rect.x,
                             self.rect.y+menu.rect.y)
        self.entities.append(menu)

    def tick(self):
        pass
