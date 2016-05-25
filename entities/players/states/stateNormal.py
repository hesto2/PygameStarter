from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from entities.players.states.state import State
from pygame.locals import *
import constants as C
import pygame

class StateNormal(State):
    def __init__(self,player,duration=0):
        from entities.players.player import Player
        self.name = C.P_STATE_NORMAL
        super().__init__(player,duration)

    def tick(self):
        self.player.currentSpeed = self.player.maxSpeed
        super().tick()
