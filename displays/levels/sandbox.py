from displays.display import Display
from entities.entity import Entity
from entities.obstacles.wallStd import WallStd
from entities.players.player import Player
from pygame.locals import *
import constants as C
import pygame
class SandBox(Display):
    def __init__(self):

        screenRect = C.GAME.SCREEN.get_rect()
        obstacles = []
        wallImg = pygame.image.load('lib/obstacles/wall.jpg')
        obstacles.append(WallStd(wallImg,{'x':50,'y':200},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':550,'y':50},moveableSides=[C.SIDE_RIGHT,C.SIDE_TOP,C.SIDE_LEFT,C.SIDE_BOTTOM]))
        obstacles.append(WallStd(wallImg,{'x':300,'y':150},))
        obstacles.append(WallStd(wallImg,{'x':150,'y':350}))
        obstacles.append(WallStd(wallImg,{'x':350,'y':350}))


        ball = pygame.image.load('ball.png')
        masterBall = pygame.image.load('masterBall.png')

        ballrect = ball.get_rect()

        ballrect2 = masterBall.get_rect()
        ballrect2.right = screenRect.width
        ballrect2.bottom = screenRect.height

        boundary = {"width":screenRect.width,"height":screenRect.height}

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
        player1 = Player(ballrect,p1Input,ball,boundary,'billums123')
        player2 = Player(ballrect2,p2Input,masterBall,boundary,'hesto2')
        players = [player1,player2]


        entities = []
        for player in players:
            entities.append(player)
        for obstacle in obstacles:
            entities.append(obstacle)


        super().__init__(C.GAME.SCREEN,entities)
