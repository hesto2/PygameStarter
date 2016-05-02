import sys, pygame, time
from player import Player
from pygame.locals import *

pygame.init()
width = 700
height = 500
size = [width,height]
# speed = [2,2]
black = 0,0,255

screen = pygame.display.set_mode(size)

ball = pygame.image.load('ball.png')
masterBall = pygame.image.load('masterBall.png')

ballrect = ball.get_rect()

ballrect2 = masterBall.get_rect()
ballrect2.right = width
ballrect2.bottom = height

boundary = {"width":width,"height":height}

# Key config
# ballrect.keyUp = K_w
# ballrect.keyDown = K_s
# ballrect.keyLeft = K_a
# ballrect.keyRight = K_d
# ballrect2.image = ball
#
# ballrect2.keyUp = K_UP
# ballrect2.keyDown = K_DOWN
# ballrect2.keyLeft = K_LEFT
# ballrect2.keyRight = K_RIGHT
# ballrect2.image = masterBall

player1 = Player(ballrect,K_w,K_s,K_a,K_d,ball,'billums123')
player2 = Player(ballrect2,K_UP,K_DOWN,K_LEFT,K_RIGHT,masterBall,'hesto2')
players = [player1,player2]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    for player in players:

        velocityX = 0
        velocityY = 0

        top = False
        bottom = False
        left = False
        right = False

        # Screen edge detection
        if player.rect.top <= 0:
            top = True
        if player.rect.bottom >= height:
            bottom = True
        if player.rect.left <= 0:
            left = True
        if player.rect.right >= width:
            right = True

        # Player collision detection

        for target in players:
            if player.name == target.name:
                continue

            # collisions = player.checkCollsion(target.rect)
            # if collisions['top']:
            #     top = True
            # if collisions['bottom']:
            #     bottom = True
            # if collisions['left']:
            #     left = True
            # if collisions['right']:
            #     right = True

        # Input handling
        keys = pygame.key.get_pressed()
        if keys[player.keyUp]:
            # if top == False:
                velocityY = -1
        if keys[player.keyDown]:
            # if bottom == False:
                velocityY = 1
        if keys[player.keyLeft]:
            if left == False:
                velocityX = -1
        if keys[player.keyRight]:
            # if right == False:
                velocityX = 1

        player.velocityX = velocityX
        player.velocityY = velocityY
        # Drawing
        player.rect = player.move(players,boundary)
        screen.blit(player.image,player.rect)


    position = 'Top: %i, Bottom: %i, Left: %i, Right: %i' % (ballrect.top,ballrect.bottom,ballrect.left,ballrect.right)
    # print(position)


    pygame.display.flip()
    time.sleep(.003)
