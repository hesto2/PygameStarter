from entities.entity import Entity
from displays.levels.level import LevelComponent
import constants as C
import pygame
'''
Fade int:
0 = No Fade
1 = Fade To
-1 = Fade From

fadePoint int:
the point at wich the fade should fade to or from
'''
# class black(Entity):
#     def __init__(self,fade=0,fadePoint=200,fadeSpeed=5,rect=C.GAME.SCREEN.get_rect()):
#         image = pygame.Surface((rect.width,rect.height))
#         self.fadeSpeed = fadeSpeed
#         self.fadeDirection = fade
#         self.fadePoint = fadePoint
#         if fade != 0:
#             if fade == 1:
#                 image.set_alpha(0)
#             elif fade == -1:
#                 image.set_alpha(255)
#         super().__init__(rect,image)
#
#     def tick(self):
#         currentAlpha = self.image.get_alpha()
#         if currentAlpha != self.fadePoint:
#             setAlpha = 0
#             print(currentAlpha)
#             if self.fadeDirection == 1:
#                 if currentAlpha < self.fadePoint:
#                     setAlpha = currentAlpha + self.fadeSpeed
#                 else:
#                      setAlpha = self.fadePoint
#             elif self.fadeDirection == -1:
#                 if currentAlpha > self.fadePoint:
#                     setAlpha = currentAlpha - self.fadeSpeed
#                 else:
#                      setAlpha = self.fadePoint
#             if setAlpha > 255:
#                 setAlpha = 255
#             elif setAlpha < 0:
#                 setAlpha = 0
#             self.image.set_alpha(setAlpha)

class black(LevelComponent):
    def __init__(self):
        self.fadeSpeed = 5
        screen = C.GAME.SCREEN.get_rect()
        super().__init__((screen.width,screen.height))
        self.surface.set_alpha(0)


    def tick(self):
        if self.surface.get_alpha() < 200:
            self.surface.set_alpha(self.surface.get_alpha() + 10)
