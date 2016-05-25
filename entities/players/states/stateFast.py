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
        super().__init__(player,duration)

    def tick(self):
        currentSecond = C.GAME.display.timer.currentLiveTime
        # Fade for the given amount of time for the state
        if self.coolDownStartSecond == None:
            self.coolDownStartSecond = currentSecond
            self.player.image.set_alpha(50)
        if currentSecond >= (self.coolDownStartSecond+self.duration):
            self.player.image.set_alpha(None)
            self.player.state = StateNormal(self.player)

    # Allow players to move through but not obstacles etc.
    def onCollision(self,collider,side):
        if collider.type == C.TYPE_PLAYER:
            return
        else:
            super().onCollision(collider,side)

    # def coolDown(self):
    #     if self.coolDownStartTick == None:
    #         self.coolDownStartTick = pygame.time.get_ticks()
    #         self.currentCooldown = self.taggedCooldown
    #         self.image.set_alpha(50)
    #     else:
    #         elapsed = getSecondsElapsed(pygame.time.get_ticks(),self.coolDownStartTick)
    #         # self.image.set_alpha(40)
    #         self.currentCooldown = self.taggedCooldown - elapsed
    #         if self.currentCooldown <= 0:
    #             self.coolDownStartTick = None
    #             self.image.set_alpha(None)
