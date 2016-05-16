from entities.entity import Entity
import constants as C
import pygame
import math
from tools.time import getSecondsElapsed
class Timer(Entity):
    font = pygame.font.Font(None, 36)

    def __init__(self):
        text = self.font.render("0:00", 1, (0,255,0))
        textpos = text.get_rect()
        # self.parentRect = parentRect

        super().__init__(textpos,text)

    def tick(self):
        current_time = pygame.time.get_ticks()
        color = C.BLACK
        minutes = 0
        seconds = 0
        if C.GAME.display.state == C.STATE_PRE_START:
            current_time -= C.GAME.display.start_time
            countdown = C.GAME.display.start_countdown
            timeElapsed = getSecondsElapsed(current_time,countdown)
            seconds = countdown - timeElapsed
            color = C.RED
            if seconds <= 0:
                C.GAME.display.state = C.STATE_IN_PROGRESS
                C.GAME.display.start_time = pygame.time.get_ticks()
                color = C.BLACK

        if C.GAME.display.state == C.STATE_IN_PROGRESS:
            start_time = C.GAME.display.start_time
            current_time -= start_time
            time_limit = C.GAME.display.time_limit
            timeElapsed = getSecondsElapsed(current_time,time_limit)
            timeLeft = time_limit - timeElapsed
            minutes = math.modf(timeLeft/60)[1]
            seconds = (minutes * 60) - timeLeft
            seconds *= -1
            if timeLeft <= 15:
                color = C.RED
                if timeLeft <= 0:
                    C.GAME.display.state = C.STATE_FINISHED

            #Handle players being tagged
            incrementTaggedPlayerTime()

        time = '%i:%02d' % (minutes,seconds)
        self.image = self.font.render(time,1,color)

def incrementTaggedPlayerTime():
    C.GAME.display.taggedPlayer.time_tagged +=1
