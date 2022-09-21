# This Python file uses the following encoding: utf-8
import sys
import pygame
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QSlider
from PySide6.QtCore import QTimer

class Timer:
    _clock = None
    _dt:float = 0

    def __init__(self):
        self._clock = pygame.time.Clock()

    def Update(self):
        self._dt = self._clock.tick(60)/1000

    def GetDeltaTime(self):
        return self._dt

class Game():
    def __init__(self):
        pygame.init()
        self.timer = Timer()
        self.GameInit()
        self.shouldQuit = False
        pass

    def GameInit(self):
        self.size = self.width, self.height = 640, 480
        self.black = [0, 0, 0]

        self.screen = pygame.display.set_mode(self.size)

        self.troll = pygame.image.load("Trollface.png")
        self.trollrect = self.troll.get_rect()

        self.circle = pygame.Surface([111, 111])
        self.circleRect = pygame.draw.circle(self.circle, pygame.Color(255, 0, 0) \
                            , ((self.circle.get_width()/2), self.circle.get_height()/2), 50)

    def Render(self):
        self.screen.fill(self.black)

        self.screen.blit(self.troll, self.trollrect)

        pygame.display.flip() #render

    def ProcessInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.shouldQuit = True
            if event.type == pygame.KEYDOWN:
                if event.key == 119:
                    pass
            if event.type == pygame.KEYUP:
                pass


    def Loop(self):
        self.timer.Update()
        dt = self.timer.GetDeltaTime()

        self.ProcessInput()

        #UpdateActor

        self.Render()
        return self.shouldQuit

class Window(QWidget):
    button:QPushButton
    slider:QSlider
    game:Game

    def __init__(self, game:Game):
        super().__init__()
        self.InitUI()
        self.InitPygame(game)

    def InitPygame(self, game:Game):
        self.game = game
        self.timer = QTimer()
        self.timer.timeout.connect(self.PygameLoop)
        self.timer.start(0)

    def PygameLoop(self):
        if self.game.Loop():
            self.close()

    def InitUI(self):
        self.setWindowTitle("Interface pong")
        self.setGeometry(10, 10, 300, 200)

        self.button = QPushButton("Do not click", self)
        self.button.setToolTip("Don't you dare!")
        self.button.move(100, 70)
        self.button.clicked.connect(self.OnClick)

        self.slider = QSlider(self)
        self.slider.sliderReleased.connect(self.OnSlider)
        self.slider.setRange(500, 1500)

        self.show()

    def OnClick(self):
        pass

    def OnSlider(self):
        slider:QSlider = self.sender()
        print(slider.value())


def Main():
    app = QApplication(sys.argv)
    game = Game()
    exe = Window(game)
    app.setActiveWindow(exe)

    sys.exit(app.exec())

if __name__ == "__main__":
    Main()
