# This Python file uses the following encoding: utf-8
import pygame
from Timer import Timer
from Engine import Engine
from Player import Player
from Enemy import Enemy
from Ball import Ball

class Game():
    timer:Timer
    shouldQuit:bool


    startGame:bool = False

    width:int = 1000
    height:int = 640
    size:int = []

    black:int = [0, 0, 0]

    screen:pygame.display

    engine:Engine

    player:Player
    enemy:Player
    ball:Ball

    def __init__(self):
        self.engine = Engine()
        pygame.init()
        self.timer = Timer()
        self.GameInit()
        self.shouldQuit = False

    def GameInit(self):
        self.size = [self.width, self.height]
        self.screen = pygame.display.set_mode(self.size)

        self.player = Player(10, self.height/2 - (150/2), 25, 125, self.width, self.height, 500)
        self.player.SetTag("player")

        self.enemy = Enemy(self.width - 35, self.height/2 - (150/2), 25, 125, self.width, self.height, 300)
        self.enemy.SetTag("enemy")

        self.ball = Ball(self.width/2 - (25/2), self.height/2 - (25/2), 25, 25, self.width, self.height, 400, 500)
        self.ball.SetTag("ball")

        self.enemy.SetBall(self.ball)

        self.engine.AddActor(self.player)
        self.engine.AddActor(self.enemy)
        self.engine.AddActor(self.ball)

        self.engine.Start()

    def Render(self):
        self.screen.fill(self.black)

        self.engine.Render(self.screen)

        pygame.display.flip() #render

    def ProcessInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.shouldQuit = True
            if event.type == pygame.KEYDOWN:
                if event.key == 32: #space
                    self.startGame = True
            if event.type == pygame.KEYUP:
                pass
        if pygame.key.get_pressed()[pygame.K_w]:
            self.player.Move(-1)
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.player.Move(1)
        else:
            self.player.Move(0)


    def Loop(self):
        self.timer.Update()
        dt = self.timer.GetDeltaTime()

        self.ProcessInput()

        if self.startGame:
            self.engine.Update(dt)

        if self.ball.TouchTheWall():
            self.startGame = False
            self.engine.Start()

        self.engine.CheckCollider()

        self.Render()
        return self.shouldQuit

    def OnSlider(self, speed:float):
        self.ball.SetSpeedX(speed)

    def OnClick(self, difficil:bool):
        if difficil:
            print("hardcore mode")
            self.enemy.ChangeDifficulte(400, True)
        else:
            print("easy mode")
            self.enemy.ChangeDifficulte(300, False)

    def StartGame(self):
        self.startGame = True
