from entities.pickups.pickup import Pickup
from pygame.locals import *
import constants as C
import pygame

class PickupInvincible(Pickup):
    def __init__(self):
        from entities.players.states.stateInvincible import StateInvincible
        name = C.PICKUP_INVINCIBLE
        image = pygame.image.load('lib/pickups/invincible.png').convert()
        statusEffect = StateInvincible
        rarity = C.UNCOMMON
        ttl = 10
        duration = 3
        rect = image.get_rect()
        super().__init__(rect,image,name,rarity,statusEffect,ttl=ttl,duration=duration)

    def affectPlayer(self,collider):
        if C.GAME.display.taggedPlayer == collider:
            from entities.players.states.stateFast import StateFast
            collider.state = StateFast(collider)
        else:
            super().affectPlayer(collider)
