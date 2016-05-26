from displays.display import Display
from entities.entity import Entity
from entities.gui import buttons
from entities.gui.checkbox import CheckBox
from entities.gui.labels import Label
from tools.eztext import Input,InputBox
import json
import pygame
import constants as C
import os
class EditKeysMenu(Display):
    def __init__(self,title,keyFile):
        super().__init__(C.GAME.SCREEN,[])
        self.inputs = {}
        self.keyFile = keyFile
        entities = []
        centerx = C.GAME.SCREEN.get_rect().centerx
        centery = C.GAME.SCREEN.get_rect().centery
        screenHeight = C.GAME.SCREEN.get_rect().height
        screenWidth = C.GAME.SCREEN.get_rect().width
        # Title
        title = Label(title,centerx=centerx,centery=screenHeight*.1)
        entities.append(title)

        column1 = centerx *.8

        upLabel = Label("Key Up:",x=column1,centery=screenHeight *.2)
        entities.append(upLabel)
        upInput = Input(bg=C.WHITE,maxlength=1,color=C.BLACK)
        upInput.rect.x = upLabel.rect.right + 10
        upInput.rect.centery = screenHeight *.2
        entities.append(InputBox(upInput))
        entities.append(upInput)
        self.inputs['up'] = upInput

        downLabel = Label("Key Down:",x=column1,centery=screenHeight *.3)
        entities.append(downLabel)
        downInput = Input(bg=C.WHITE,maxlength=1,color=C.BLACK)
        downInput.rect.x = downLabel.rect.right + 10
        downInput.rect.centery = screenHeight *.3
        entities.append(InputBox(downInput))
        entities.append(downInput)
        self.inputs['down'] = downInput

        leftLabel = Label("Key Left:",x=column1,centery=screenHeight *.4)
        entities.append(leftLabel)
        leftInput = Input(bg=C.WHITE,maxlength=1,color=C.BLACK)
        leftInput.rect.x = leftLabel.rect.right + 10
        leftInput.rect.centery = screenHeight *.4
        entities.append(InputBox(leftInput))
        entities.append(leftInput)
        self.inputs['left'] = leftInput

        rightLabel = Label("Key Right:",x=column1,centery=screenHeight *.5)
        entities.append(rightLabel)
        rightInput = Input(bg=C.WHITE,maxlength=1,color=C.BLACK)
        rightInput.rect.x = rightLabel.rect.right + 10
        rightInput.rect.centery = screenHeight *.5
        entities.append(InputBox(rightInput))
        entities.append(rightInput)
        self.inputs['right'] = rightInput


        with open(self.keyFile,'r') as f:
            data = f.read()
        loadedInputs = json.loads(data)
        for item in loadedInputs:
            self.inputs[item].value = loadedInputs[item]

        # Save Button
        save = buttons.SaveKeysButton()
        save.rect.centerx = centerx
        save.rect.top = screenHeight*.6
        entities.append(save)
        # Back to Main Menu
        settings = buttons.SettingsButton()
        settings.rect.x = 30
        settings.rect.y = 30
        entities.append(settings)
        self.entities = entities

    def tick(self):
        super().tick()
