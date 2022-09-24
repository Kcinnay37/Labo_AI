# This Python file uses the following encoding: utf-8
from Actor import Actor
import pygame
from random import Random

class Ball(Actor):
    dirX:int
    dirY:int
    moveSpeedX:float

    timeDelay:float = 0.3
    currTime = 0
    isCheckCollide:bool = True

    def __init__(self, posX:float, posY:float, sizeX:float, sizeY:float, screenSizeX:float, screenSizeY:float, moveSpeedY:float, moveSpeedX:float):
        super().__init__(posX, posY, sizeX, sizeY, screenSizeX, screenSizeY, moveSpeedY)
        self.moveSpeedX = moveSpeedX

    def OnCollider(self):
        self.dirX = -self.dirX

    def CheckCollider(self, actor):
        if not self.isCheckCollide:
            return False

        if (self.posX <= actor.posX + actor.sizeX and self.posX + self.sizeX >= actor.posX) \
            and (self.posY + self.sizeY >= actor.posY and self.posY <= actor.posY + actor.sizeY):
            self.isCheckCollide = False
            return True

            return False

    def Start(self):
        self.ResetPos()

        rand:Random = Random()
        self.dirX = Random.randint(rand, 0, 1)
        if self.dirX == 0:
            self.dirX = -1
        self.dirY = Random.randint(rand, 0, 1)
        if self.dirY == 0:
            self.dirY = -1

    def Update(self, dt:float):
        if not self.isCheckCollide:
            self.currTime += dt
            if self.currTime >= self.timeDelay:
                self.currTime = 0
                self.isCheckCollide = True

        self.posY += self.moveSpeedY * float(self.dirY) * dt
        self.posX += self.moveSpeedX * float(self.dirX) * dt

        if self.posY <= 0 or self.posY >= self.screenSizeY - self.sizeY:
            self.dirY = -self.dirY

    def TouchTheWall(self):
        if self.posX <= 0 or self.posX >= self.screenSizeX - self.sizeX:

            return True
        return False

    def SetSpeedX(self, speed:float):
        self.moveSpeedX = speed
