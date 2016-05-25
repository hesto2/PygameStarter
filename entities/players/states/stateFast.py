from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from entities.players.states.state import State
from pygame.locals import *
import constants as C
import pygame

class StateFast(State):
    def __init__(self,player,duration=2):
        from entities.players.player import Player
        self.name = C.P_STATE_INVINCIBLE
        # The number by which to multiply the player's max speed
        self.speedBoost = 1.5
        super().__init__(player,duration)

    def tick(self):
        self.player.currentSpeed = self.player.maxSpeed * self.speedBoost
        super().tick()
