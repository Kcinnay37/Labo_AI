# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from Game import Game
from Window import Window

def Main():
    app = QApplication(sys.argv)
    game = Game()
    exe = Window(game)
    app.setActiveWindow(exe)

    sys.exit(app.exec())

if __name__ == "__main__":
    Main()
