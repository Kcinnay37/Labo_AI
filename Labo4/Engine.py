# This Python file uses the following encoding: utf-8
from Actor import Actor

class Engine:
    actors:Actor = []

    def __init__(self):
        pass

    def AddActor(self, actor:Actor):
        self.actors.append(actor)

    def Start(self):
        for i in range(len(self.actors)):
            self.actors[i].Start()

    def Update(self, dt:float):
        for i in range(len(self.actors)):
            self.actors[i].Update(dt)

    def Render(self, screen):
        for i in range(len(self.actors)):
            self.actors[i].Render(screen)

    def CheckCollider(self):
        ball:Actor
        for i in range(len(self.actors)):
            if self.actors[i].GetTag() == "ball":
                ball = self.actors[i]
                break

        for i in range(len(self.actors)):
            if self.actors[i].GetTag() == "ball":
                break
            if ball.CheckCollider(self.actors[i]):
                ball.OnCollider()

