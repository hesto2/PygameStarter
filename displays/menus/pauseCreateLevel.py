from entities.entity import Entity
from entities.gui import buttons
from displays.levels.level import LevelComponent
from tools.eztext import Input
import constants as C
import pygame
from entities.gui import overlays

# class fileNameInput(Input):
#     def __init(self,**options):
#         super().__init__(**options)
#
#     def tick(self):
#         super().tick()
#         C.GAME.display.fileName = self.value


class PauseCreateLevel(LevelComponent):
    def __init__(self,name=''):
        self.fadeSpeed = 5
        self.fileName = ''
        self.fileNameInput = None
        self.screen = C.GAME.SCREEN.get_rect()
        screen = self.screen
        super().__init__((self.screen.width*.4,self.screen.height*.4),entities=[])
        self.entities = []
        self.fileName = name
        # Buttons

        # Reset Button
        reset = buttons.ResetButton()
        self.rect.centerx = screen.centerx
        self.rect.centery = screen.centery
        reset.rect.centerx = self.rect.width *.5
        reset.rect.centery = self.rect.height *.5
        reset.abs_pos = (self.rect.x+reset.rect.x,
                             self.rect.y+reset.rect.y)
        self.entities.append(reset)

        # Main Menu Button
        menu = buttons.MainMenuButton()
        menu.rect.centerx = self.rect.width *.5
        menu.rect.centery = self.rect.height *.7
        menu.abs_pos = (self.rect.x+menu.rect.x,
                             self.rect.y+menu.rect.y)
        self.entities.append(menu)

        # File Name Input
        textInput = Input(maxlength=20,color=C.WHITE,prompt='File Name: ')
        textInput.rect.x = 0
        textInput.rect.top = 0
        abs_pos = (self.rect.x+textInput.rect.x,
                             self.rect.y+textInput.rect.y)
        setattr(textInput,'abs_pos',abs_pos)
        self.entities.append(textInput)
        self.fileNameInput = self.entities[len(self.entities)-1]
        self.fileNameInput.value = self.fileName

        # Save Button
        save = buttons.SaveButton(self.fileNameInput)
        save.rect.centerx = self.rect.width *.5
        save.rect.centery = self.rect.height *.9
        save.abs_pos = (self.rect.x+save.rect.x,
                             self.rect.y+save.rect.y)
        self.entities.append(save)


    def tick(self):
        self.fileName = self.fileNameInput.value
        # align dynamic items
        # Align text input
        # menu = self.entities[1]
        # textInput = self.entities[2]
        # textInput.rect = textInput.image.get_rect()
        # textInput.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        # textInput.rect.top = C.GAME.SCREEN.get_rect().centery *.7 + menu.rect.height*.5
        # textInput.abs_pos = (self.rect.x+textInput.rect.x,
        #                      self.rect.y+textInput.rect.y)
