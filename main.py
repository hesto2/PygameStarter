import sys, pygame, time
from entities.players.player import Player
from pygame.locals import *
from entities.obstacles.wallStd import WallStd

pygame.init()
width = 700
height = 500
size = [width,height]
black = 0,0,255

screen = pygame.display.set_mode(size)

obstacles = []
wallImg = pygame.image.load('lib/obstacles/wall.jpg')
obstacles.append(WallStd(wallImg,{'x':50,'y':200}))
obstacles.append(WallStd(wallImg,{'x':550,'y':50}))
obstacles.append(WallStd(wallImg,{'x':300,'y':150}))
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
    print(obstacle.rect.x)
    print(obstacle.rect.y)
    entities.append(obstacle)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    for player in players:
        velocityY = 0
        velocityX = 0

        # Input handling
        keys = pygame.key.get_pressed()
        if keys[player.keyUp]:
                velocityY = -1
        if keys[player.keyDown]:
                velocityY = 1
        if keys[player.keyLeft]:
                velocityX = -1
        if keys[player.keyRight]:
                velocityX = 1

        player.velocityX = velocityX
        player.velocityY = velocityY
        # Drawing
        player.rect = player.move(entities,boundary)



    position = 'Top: %i, Bottom: %i, Left: %i, Right: %i' % (ballrect.top,ballrect.bottom,ballrect.left,ballrect.right)
    # print(position)
    # for o in obstacles:
    #     obstascle.tick()
    for entity in entities:
        screen.blit(entity.image,entity.rect)

    pygame.display.flip()
    time.sleep(.003)
