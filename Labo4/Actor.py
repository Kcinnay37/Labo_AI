# This Python file uses the following encoding: utf-8
from abc import abstractmethod
import pygame

class Actor:
    tag:str = ""

    initialPosX:float
    initialPosY:float

    posX:float
    posY:float
    sizeX:float
    sizeY:float
    screenSizeX:float
    screenSizeY:float
    moveSpeedY:float

    white:int = [255, 255, 255]

    rect:pygame.Rect

    def __init__(self, posX:float, posY:float, sizeX:float, sizeY:float, screenSizeX:float, screenSizeY:float, moveSpeed:float):
        self.posX = posX
        self.posY = posY
        self.initialPosX = posX
        self.initialPosY = posY
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.screenSizeX = screenSizeX
        self.screenSizeY = screenSizeY
        self.moveSpeedY = moveSpeed

    def SetTag(self, tag:str):
        self.tag = tag

    def GetTag(self):
        return self.tag

    def ResetPos(self):
        self.posX = self.initialPosX
        self.posY = self.initialPosY

    @abstractmethod
    def OnCollider(self):
        pass

    @abstractmethod
    def CheckCollider(self, actor):
        pass

    @abstractmethod
    def Start(self):
        pass

    @abstractmethod
    def Update(self, dt:float):
        pass

    def Render(self, screen):
        self.rect = pygame.Rect(self.posX, self.posY, self.sizeX, self.sizeY)
        pygame.draw.rect(screen, pygame.Color(self.white), self.rect)
