from Game import Game
from PySide6.QtWidgets import QWidget, QPushButton, QSlider
from PySide6.QtCore import QTimer

class Window(QWidget):
    button:QPushButton
    button1:QPushButton
    slider:QSlider
    game:Game
    timer:QTimer

    difficil:bool = False

    def __init__(self, game:Game):
        super().__init__()
        self.InitUI()
        self.InitPygame(game)

    def InitPygame(self, game:Game):
        self.game = game

        #ce qui permet dappeler la loop tout les 0 second
        self.timer = QTimer()
        self.timer.timeout.connect(self.PygameLoop)
        self.timer.start(0)

    def PygameLoop(self):
        if self.game.Loop():
            self.close()

    def InitUI(self):
        self.setWindowTitle("Interface pong")
        self.setGeometry(10, 10, 300, 200)

        self.button = QPushButton("Change difficulte", self)
        self.button.move(75, 70)
        self.button.clicked.connect(self.OnClick)

        self.button = QPushButton("StartGame", self)
        self.button.move(175, 70)
        self.button.clicked.connect(self.OnClick1)

        self.slider = QSlider(self)
        self.slider.sliderReleased.connect(self.OnSlider)
        self.slider.setRange(500, 1500)

        self.show()

    def OnClick(self):
        if not self.difficil:
            self.difficil = True
            self.game.OnClick(self.difficil)
        else:
            self.difficil = False
            self.game.OnClick(self.difficil)

    def OnClick1(self):
        self.game.StartGame()

    def OnSlider(self):
        slider:QSlider = self.sender()
        self.game.OnSlider(slider.value())
