from entities.entity import Entity
from entities.gui import buttons
from displays.levels.level import LevelComponent
import constants as C
import pygame
from entities.gui import overlays
class EndRoundMenu(LevelComponent):
    fadeSpeed = 5
    def __init__(self):
        screen = C.GAME.SCREEN.get_rect()

        # Buttons
        playAgain = buttons.PlayAgainButton()
        super().__init__((screen.width*.4,screen.height*.4),entities=[])

        self.rect.centerx = screen.centerx
        self.rect.centery = screen.centery

        playAgain.rect.centerx = self.rect.width *.5
        playAgain.rect.centery = self.rect.height *.5
        playAgain.abs_pos = (self.rect.x+playAgain.rect.x,
                             self.rect.y+playAgain.rect.y)
        self.entities.append(playAgain)

        # Main Menu Button
        menu = buttons.MainMenuButton()
        menu.rect.centerx = self.rect.width *.5
        menu.rect.centery = self.rect.height *.7
        menu.abs_pos = (self.rect.x+menu.rect.x,
                             self.rect.y+menu.rect.y)
        self.entities.append(menu)
