from entities.entity import Entity
import constants as C
import pygame
import time
import json
import os

class CheckBox(Entity):
    width = 15
    height = 15
    def __init__(self,valueKey,x=0,y=0,centerx=None,centery=None,checked=False,disabled=False):
        self.checked = checked
        self.valueKey = valueKey
        self.disabled = disabled
        surface = pygame.Surface((self.width,self.height))
        if self.disabled:
            surface.fill(C.GREY)
        else:
            surface.fill(C.WHITE)

        self.uncheckedImage = surface
        rect = surface.get_rect()
        if centerx:
            rect.centerx = centerx
        else:
            rect.x = x

        if centery:
            rect.centery = centery
        else:
            rect.y = y


        # Make checkmark
        subsurface = pygame.Surface((self.width-6,self.height-6))
        subsurface.fill(C.BLACK)
        subrect = subsurface.get_rect()
        subrect.centerx = rect.centerx
        subrect.centery = rect.centery
        self.checkMark = Entity(subrect,subsurface)

        super().__init__(rect,surface)
        # Add checkmark value to displays list of check values
        C.GAME.display.checkBoxValues[self.valueKey] = self.checked

    def tick(self):
        if self.checked:
            if self.checkMark not in C.GAME.display.entities:
                C.GAME.display.entities.append(self.checkMark)
        else:
            if self.checkMark in C.GAME.display.entities:
                C.GAME.display.entities.remove(self.checkMark)

        C.GAME.display.checkBoxValues[self.valueKey] = self.checked
        super().tick()

    def onLeftMouseDown(self):
        if self.disabled:
            return
        if C.GAME.display.mouseDown:
            return
        if self.checked:
            self.checked = False
        else:
            self.checked = True
        C.GAME.display.mouseDown = True
        # Pass display object and attribtue it should set to true or false
