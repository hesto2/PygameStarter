from displays.display import Display
from entities.entity import Entity
from entities.gui.timer import Timer
from entities.players.states.state import State
from pygame.locals import *
import constants as C
import pygame

class StateInvincible(State):
    def __init__(self,player,duration):
        self.duration = duration
        self.taggedCooldown = 2
        self.currentCooldown = 0
        self.coolDownStartTick = None
        from entities.players.player import Player
        self.name = C.P_STATE_INVINCIBLE
        super().__init__(player)

    def tick(self):
        super().tick()
        pass

    # Allow players to move through but not obstacles etc.
    def onCollision(self,collider,side):
        if collider.type == C.TYPE_PLAYER:
            return
        moveToEdge(self.player,collider,side)
