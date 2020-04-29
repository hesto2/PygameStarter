from displays.levels.level1 import Level1
from displays.levels.createLevel import CreateLevel
from displays.display import Display
from entities.entity import Entity
from displays.levels.customLevel import CustomLevel
import constants as C
import pygame
import time
import json
import os
class Button(Entity):
    def __init__(self,rect,image):
        super().__init__(rect,image)
        self.clickable = False

    def onLeftMouseDown(self):
        if C.GAME.display.mouseDown:
            self.clickable = False
        else:
            C.GAME.display.mouseDown = True
            self.clickable = True

class PlayButton(Button):
    def __init__(self):
        image = pygame.image.load('lib/gui/buttons/playButton.png')
        super().__init__(image.get_rect(),image)

    def onMouseHover(self):
        pass

    def onLeftMouseDown(self):
        C.GAME.display = Level1()

class PlayAgainButton(Button):
    font = pygame.font.Font(None, 25)
    abs_pos = (0,0)
    def __init__(self):
        text = self.font.render("Play Again", 1, (255,255,255))
        textpos = text.get_rect()
        super().__init__(textpos,text)

    def tick(self):
        self.image = self.font.render("Play Again", 1, (255,255,255))
        super().tick()

    def onLeftMouseDown(self):
        from displays.menus.startMenu import StartMenu
        C.GAME.display.reset()

class CreateLevelButton(Button):
    def __init__(self):
        image = pygame.image.load('lib/gui/buttons/createLevel.png')
        super().__init__(image.get_rect(),image)

    def onLeftMouseDown(self):
        C.GAME.display = CreateLevel()

class SettingsButton(Button):
    def __init__(self):
        image = pygame.image.load('lib/gui/buttons/settings.png')
        super().__init__(image.get_rect(),image)

    def onLeftMouseDown(self):
        super().onLeftMouseDown()
        if self.clickable == False:
            return
        from displays.menus.settingsMenu import SettingsMenu
        C.GAME.display = SettingsMenu()

class ResetButton(Button):
    font = pygame.font.Font(None, 25)
    abs_pos = (0,0)
    def __init__(self):
        text = self.font.render("Reset", 1, (255,255,255))
        textpos = text.get_rect()
        super().__init__(textpos,text)

    def tick(self):
        self.image = self.font.render("Reset", 1, (255,255,255))
        super().tick()

    def onLeftMouseDown(self):
        from displays.menus.startMenu import StartMenu
        C.GAME.display.reset()

class MainMenuButton(Button):
    font = pygame.font.Font(None, 25)
    abs_pos = (0,0)
    def __init__(self):
        text = self.font.render("Main Menu", 1, (255,255,255))
        textpos = text.get_rect()
        super().__init__(textpos,text)

    def tick(self):
        self.image = self.font.render("Main Menu", 1, (255,255,255))
        super().tick()

    def onLeftMouseDown(self):
        from displays.menus.startMenu import StartMenu
        C.GAME.changeDisplay(StartMenu())

class SaveButton(Button):
    font = pygame.font.Font(None, 25)
    abs_pos = (0,0)
    def __init__(self,nameInput):
        self.nameInput = nameInput
        text = self.font.render("Save Level", 1, (255,255,255))
        textpos = text.get_rect()
        super().__init__(textpos,text)

    def tick(self):
        self.image = self.font.render("Save Level", 1, (255,255,255))
        super().tick()

    def onLeftMouseDown(self):
        curpath = os.path.abspath(os.curdir)
        curpath  += '/levelData'
        name = self.nameInput.value
        if not name:
            name = str(time.time())
            name = name.replace('.','')
            self.nameInput.value = name
        if not os.path.exists(curpath):
            os.makedirs(curpath)
        saveItems = {"entities":[]}
        for entity in C.GAME.display.playArea.entities:
            saveItem = {'code':entity.keyCode,'x':entity.rect.x,'y':entity.rect.y}
            saveItems['entities'].append(saveItem)
        data = json.dumps(saveItems)
        with open('%s/%s.json'%(curpath,name),'w') as f:
            f.write(data)

class LoadLevelButton(Button):
    def __init__(self):
        image = pygame.image.load('lib/gui/buttons/selectLevel.png')
        super().__init__(image.get_rect(),image)

    def onMouseHover(self):
        pass

    def onLeftMouseDown(self):
        from displays.menus.selectLevel import SelectLevel
        C.GAME.display = SelectLevel()

class MainBackButton(Button):
    def __init__(self):
        image = pygame.image.load('lib/gui/buttons/mainMenu.png')
        super().__init__(image.get_rect(),image)

    def onLeftMouseDown(self):
        super().onLeftMouseDown()
        if self.clickable == False:
            return
        from displays.menus.startMenu import StartMenu
        C.GAME.display = StartMenu()

class Title(Button):
    font = pygame.font.Font(None, 38)
    abs_pos = (0,0)
    def __init__(self,text,color=(C.WHITE)):
        self.text = text
        self.color = color
        text = self.font.render(self.text, 1, self.color)
        textpos = text.get_rect()
        super().__init__(textpos,text)

    def tick(self):
        self.image = self.font.render(self.text, 1, self.color)
        super().tick()

class LevelTile(Button):
    font = pygame.font.Font(None, 25)
    def __init__(self,text,data,color=(C.WHITE)):
        self.text = text
        self.color = color
        self.data = data
        text = self.font.render(self.text, 1, self.color)
        textpos = text.get_rect()
        super().__init__(textpos,text)

    def tick(self):
        self.image = self.font.render(self.text, 1, self.color)
        super().tick()

    def onLeftMouseDown(self):
        if C.GAME.display.mouseDown:
            return
        C.GAME.display = CustomLevel(self.data)

    def onRightMouseDown(self):
        C.GAME.display = CreateLevel(self.data,self.text)

class KeysButton(Button):
    def __init__(self,title,keyFile):
        image = pygame.image.load('lib/gui/buttons/keys.png')
        self.keyFile = keyFile
        self.title = title
        super().__init__(image.get_rect(),image)

    def onLeftMouseDown(self):
        super().onLeftMouseDown()
        if self.clickable == False:
            return
        from displays.menus.editKeysMenu import EditKeysMenu
        C.GAME.display = EditKeysMenu(self.title,self.keyFile)

class SaveKeysButton(Button):
    def  __init__(self):
        image = pygame.image.load('lib/gui/buttons/save.png')
        super().__init__(image.get_rect(),image)

    def onLeftMouseDown(self):
        super().onLeftMouseDown()
        if self.clickable == False:
            return
        inputs = C.GAME.display.inputs
        # inputs = json.dumps(C.GAME.display.inputs)
        saveData = {}
        for item in inputs:
            value = inputs[item].value
            if len(value) == 1:
                value = value.lower()
            # Don't save if they are missing fields
            elif len(value) < 1:
                return
            saveData[item] = value
        data = json.dumps(saveData)
        with open(C.GAME.display.keyFile,'w') as f:
            f.write(data)

class SaveSettingsButton(Button):
    def  __init__(self):
        image = pygame.image.load('lib/gui/buttons/save.png')
        self.settingsFile = C.SETTINGS_FILE
        super().__init__(image.get_rect(),image)

    def onLeftMouseDown(self):
        super().onLeftMouseDown()
        if self.clickable == False:
            return
        checkBoxValues = C.GAME.display.checkBoxValues
        textInputs = C.GAME.display.textInputs
        inputValues = {}
        for key in textInputs:
            inputValues[key] = textInputs[key].value

        # inputs = json.dumps(C.GAME.display.inputs)
        saveData = {}
        for item in checkBoxValues:
            saveData[item] = checkBoxValues[item]
        for item in inputValues:
            if item:
                saveData[item] = inputValues[item]
            else:
                # return if they are missing an input value
                return

        data = json.dumps(saveData)
        with open(self.settingsFile,'w') as f:
            f.write(data)
