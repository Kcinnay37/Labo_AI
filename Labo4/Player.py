# This Python file uses the following encoding: utf-8
from Actor import Actor
import pygame

class Player(Actor):
    dir:int

    def __init__(self, posX:float, posY:float, sizeX:float, sizeY:float, screenSizeX:float, screenSizeY:float, moveSpeed:float):
        super().__init__(posX, posY, sizeX, sizeY, screenSizeX, screenSizeY, moveSpeed)

    def Move(self, dir:int):
        if self.posY <= 0 and dir == -1:
            self.dir = 0
            return
        elif self.posY >= self.screenSizeY - self.sizeY and dir == 1:
            self.dir = 0
            return

        self.dir = dir

    def Start(self):
        self.ResetPos()
        self.dir = 0

    def Update(self, dt:float):
        if self.dir != 0:
            self.posY += self.moveSpeedY * float(self.dir) * dt
