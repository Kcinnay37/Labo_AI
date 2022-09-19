# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_mainwindow import Ui_MainWindow
from Window import Window

def main():
    #cree lapplication
    app = QApplication(sys.argv)
    win = Window()

    #active la fenetre
    app.activeWindow()
    #affiche la fenetre a lecran
    win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
