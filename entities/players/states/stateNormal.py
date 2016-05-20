from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from entities.players.states.state import State
from pygame.locals import *
import constants as C
import pygame

class StateNormal(State):
    def __init__(self,player):
        from entities.players.player import Player
        self.name = C.P_STATE_NORMAL
        super().__init__(player)

    def tick(self):
        super().tick()
        pass
