from displays.display import Display
from entities.entity import Entity
from entities.gui import buttons
from tools.eztext import Input
import pygame
import constants as C
import os
class SelectLevel(Display):
    resultsPerPage = 30
    currentPage = 0
    def __init__(self):
        self.levelNames = []
        self.levelTiles = []

        path = os.path.abspath(os.curdir)
        path  += '/levelData'
        if not os.path.exists(path):
            os.makedirs(path)

        for (dirpath, dirnames, filenames) in os.walk(path):
            self.levelNames.extend(filenames)
            break
        title = buttons.Title('Select Level')
        title.rect.centerx = C.GAME.SCREEN.get_rect().centerx
        title.rect.top = 50

        for name in self.levelNames:
            text = name.replace('.json','')
            data = None
            with open('%s/%s'%(path,name),'r') as f:
                data = f.read()
            self.levelTiles.append(buttons.LevelTile(text,data))


        entities = [title]
        startIndex = self.currentPage*self.resultsPerPage-1
        if startIndex < 0: startIndex = 0
        tiles = self.levelTiles[startIndex:startIndex+self.resultsPerPage]
        padding = 10
        topMargin=150
        height = 25
        for i,tile in enumerate(tiles):
            tile.rect.centerx = C.GAME.SCREEN.get_rect().centerx
            tile.rect.top = topMargin + (padding+height)*(i+1)
            entities.append(tile)

        # Main Menu Button
        mainMenu = buttons.MainBackButton()
        mainMenu.rect.x = 30
        mainMenu.rect.y = 30
        entities.append(mainMenu)
        super().__init__(C.GAME.SCREEN,entities)
        self.mouseDown = True

    def tick(self):
        # Handle initial click through so it doesn't click automatically when navigating to menu
        if pygame.mouse.get_pressed()[0] == False:
            self.mouseDown = False
        super().tick()
