import sys, pygame, time
from entities.players.player import Player
from pygame.locals import *
from entities.obstacles.wallStd import WallStd
from constants import *
print('Starting Game')
pygame.init()
width = 700
height = 500
size = [width,height]
black = 0,0,255

screen = pygame.display.set_mode(size)

obstacles = []
wallImg = pygame.image.load('lib/obstacles/wall.jpg')
obstacles.append(WallStd(wallImg,{'x':50,'y':200},moveableSides=[SIDE_RIGHT,SIDE_TOP,SIDE_LEFT,SIDE_BOTTOM]))
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

clock = pygame.time.Clock()
print('Game Initialized')
print('Starting Game Loop')
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    for player in players:
        player.tick(entities,boundary)



    position = 'Top: %i, Bottom: %i, Left: %i, Right: %i' % (ballrect.top,ballrect.bottom,ballrect.left,ballrect.right)
    # print(position)
    # for o in obstacles:
    #     obstascle.tick()
    for entity in entities:
        screen.blit(entity.image,entity.rect)

    pygame.display.flip()
    clock.tick(55)
