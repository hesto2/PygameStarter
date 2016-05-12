import sys, pygame, time
from entities.players.player import Player
from pygame.locals import *
from entities.obstacles.wallStd import WallStd
from constants import *
from displays.display import Display
from gameMaster import GameMaster
print('Starting Game')
pygame.init()
width = 1200
height = 800
size = [width,height]
black = 0,0,255

screen = pygame.display.set_mode(size)

obstacles = []
wallImg = pygame.image.load('lib/obstacles/wall.jpg')
obstacles.append(WallStd(wallImg,{'x':50,'y':200},moveableSides=[SIDE_RIGHT]))
obstacles.append(WallStd(wallImg,{'x':550,'y':50},moveableSides=[SIDE_RIGHT,SIDE_TOP,SIDE_LEFT,SIDE_BOTTOM]))
obstacles.append(WallStd(wallImg,{'x':300,'y':150},))
obstacles.append(WallStd(wallImg,{'x':150,'y':350}))
obstacles.append(WallStd(wallImg,{'x':350,'y':350}))


ball = pygame.image.load('ball.png')
masterBall = pygame.image.load('masterBall.png')

ballrect = ball.get_rect()

ballrect2 = masterBall.get_rect()
ballrect2.right = width
ballrect2.bottom = height

boundary = {"width":width,"height":height}

p1Input = {
    "keyUp":K_w,
    "keyDown":K_s,
    "keyLeft":K_a,
    "keyRight":K_d,
}
p2Input = {
    "keyUp":K_UP,
    "keyDown":K_DOWN,
    "keyLeft":K_LEFT,
    "keyRight":K_RIGHT,
}
player1 = Player(ballrect,p1Input,ball,'billums123')
player2 = Player(ballrect2,p2Input,masterBall,'hesto2')
players = [player1,player2]


entities = []
for player in players:
    entities.append(player)
for obstacle in obstacles:
    entities.append(obstacle)


GAME = GameMaster()
print('Game Initialized')
print('Starting Game Loop')
GAME.run()
