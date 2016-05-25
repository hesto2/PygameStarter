import sys, pygame, time
pygame.init()
from pygame.locals import *
import constants as C
from displays.display import Display
from displays.menus.startMenu import StartMenu
from displays.levels.sandbox import SandBox
from displays.levels.level1 import Level1
from displays.levels.createLevel import CreateLevel
from gameMaster import GameMaster
print('Starting Game')
path = 'lib/players/tagged.png'
icon = pygame.image.load(path)
pygame.display.set_caption('Tag',path)
pygame.display.set_icon(icon)
width = 1200
height = 800
size = [width,height]
black = 0,0,255

screen = pygame.display.set_mode(size)
C.GAME = GameMaster()
C.GAME.display = Level1()
print('Game Initialized')
print('Starting Game Loop')
C.GAME.run()
