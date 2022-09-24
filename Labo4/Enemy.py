# This Python file uses the following encoding: utf-8
from Actor import Actor
import pygame
from Ball import Ball

class Enemy(Actor):
    ball:Ball
    moveTwoSens:bool = False

    def __init__(self, posX:float, posY:float, sizeX:float, sizeY:float, screenSizeX:float, screenSizeY:float, moveSpeed:float):
        super().__init__(posX, posY, sizeX, sizeY, screenSizeX, screenSizeY, moveSpeed)

    def SetBall(self, ball:Ball):
        self.ball = ball

    def Start(self):
        self.ResetPos()

    def Update(self, dt:float):

        middleBall = self.ball.posY + (self.ball.sizeY / 2)
        middlePaddle = self.posY + (self.sizeY / 2)
        if middlePaddle > middleBall:
            self.Move(-1, dt)
        elif middlePaddle < middleBall:
            self.Move(1, dt)
        else:
            self.Move(0, dt)
            pass


    def Move(self, dir:int, dt:float):
        if self.posY <= 0 and dir == -1:
            self.dir = 0
            return
        elif self.posY >= self.screenSizeY - self.sizeY and dir == 1:
            self.dir = 0
            return

        if self.ball.dirX == -1 and not self.moveTwoSens:
            return

        if dir != 0:
            self.posY += self.moveSpeedY * float(dir) * dt

    def ChangeDifficulte(self, speed:float, moveTwoSens:bool):
        self.moveSpeedY = speed
        self.moveTwoSens = moveTwoSens

