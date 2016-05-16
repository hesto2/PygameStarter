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
        super().__init__((screen.width,screen.height))
        self.surface.set_alpha(0)


    def tick(self):
        if self.surface.get_alpha() < 200:
            self.surface.set_alpha(self.surface.get_alpha() + 10)
