# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from ui_mainwindow import Ui_MainWindow
from Calc import Calc

class Window(QMainWindow):
    ui:Ui_MainWindow
    calc:Calc

    def __init__(self, x = 0, y = 0, w = 640, h = 480):
        super().__init__()
        #set la grandeur de la fenetre
        self.setGeometry(x, y, w, h)
        #set le titre de la fenetre
        self.setWindowTitle("Calculator")
        self.InitUI()

    def InitUI(self):
        #set dans ma varible ui le ui de la window cree
        self.ui = Ui_MainWindow()
        #initialise le ui
        self.ui.setupUi(self)
        self.calc = Calc(self.ui)
        self.UICheck()

    #regarde quel bouton a ete appuyer et appele la fonction en consquence
    def UICheck(self):
        for i in range(0, 10):
           getattr(self.ui, "Num_" + str(i)).clicked.connect(self.OnClickNb)

        for i in range(0, 8):
           getattr(self.ui, "Op_" + str(i)).clicked.connect(self.OnClickOp)

        self.ui.Comma.clicked.connect(self.OnClickNb)
        self.ui.PlusOrMinus.clicked.connect(self.OnClickChangeSigne)
        self.ui.Erase.clicked.connect(self.OnClickErase)
        self.ui.ResetCurr.clicked.connect(self.OnClickCurrReset)
        self.ui.Reset.clicked.connect(self.OnClickReset)
        self.ui.Equal.clicked.connect(self.OnClickEqual)

    def OnClickNb(self):
        button = self.sender()
        self.calc.AddText(button.text(), self.ui)

    def OnClickChangeSigne(self):
        self.calc.ChangeSigne(self.ui)

    def OnClickErase(self):
        self.calc.Erase(self.ui)

    def OnClickCurrReset(self):
        self.calc.CurrReset(self.ui)

    def OnClickReset(self):
        self.calc.Reset(self.ui)

    def OnClickEqual(self):
        self.calc.Equal(self.ui)

    def OnClickOp(self):
        button = self.sender()
        self.calc.AddOp(button.text(), self.ui)
