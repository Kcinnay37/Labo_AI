# This Python file uses the following encoding: utf-8
from ui_mainwindow import Ui_MainWindow
import math

class Calc:
    ops = {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        'x' : lambda x, y: x * y,
        '÷' : lambda x, y: x / y,
        "sqrt" : lambda x : math.sqrt(x),
        "x2" : lambda x : x * x,
        "1/x" : lambda x : 1 / x,
        "%" : lambda x , y : x % y
    }

    comma:bool = False
    haveNumber:bool = False
    setEqual:bool = False
    takeOld:bool = False

    currText:str
    currOp:str

    oldNumber:float = 0
    currNumber:float = 0

    def __init__(self, ui:Ui_MainWindow):
        self.currText = "0"
        self.currOp = ""
        self.SetText(ui)

    #ajoute du text dans le text courrant de la calculatrice
    def AddText(self, text:str, ui:Ui_MainWindow):
        if text == "." and self.comma:
            return
        elif text == ".":
            self.comma = True
            if not self.haveNumber:
                self.currText = '0'
            self.haveNumber = True

        if self.haveNumber:
            self.currText += text
        else:
            self.currText = text
            self.haveNumber = True

        self.SetText(ui)

        self.currNumber = float(self.currText)
        self.takeOld = False

    #prend le text courant de la calculatrice et le fais afficher
    def SetText(self, ui:Ui_MainWindow):
        if self.currText[len(self.currText) - 1] == '0' and self.currText[len(self.currText) - 2] == '.':
            self.currText = self.currText[:len(self.currText) - 2]

        ui.Text.setText(self.currText)

    #change le signe de chiffre du text afficher
    def ChangeSigne(self, ui:Ui_MainWindow):
        if self.currText == '0':
            return

        if self.currText[0] == "-":
            self.currText = self.currText[1:]
        else:
            self.currText = "-" + self.currText[0:]

        self.SetText(ui)

        self.currNumber = float(self.currText)

    #efface un caractere
    def Erase(self, ui:Ui_MainWindow):
        if not self.haveNumber:
            return

        if len(self.currText) == 1 or (len(self.currText) == 2 and self.currText[0] == '-') \
            or (len(self.currText) == 2 and self.currText[1] == '.' and self.currText[0] == '0') \
            or (len(self.currText) == 3 and self.currText[0] == '-' and self.currText[1] == '0' and self.currText[2] == '.'):
            self.CurrReset(ui)
        else:
            if self.currText[len(self.currText) - 1] == '.':
                self.comma = False

            self.currText = self.currText[:len(self.currText) - 1]

            self.SetText(ui)

            self.currNumber = float(self.currText)

    #reset la parti courant de la calculatrice
    def CurrReset(self, ui:Ui_MainWindow):
        self.currNumber = 0
        self.currText = '0'
        self.haveNumber = False
        self.comma = False
        self.SetText(ui)

    #reset la calculatice dans sont entiereter
    def Reset(self, ui:Ui_MainWindow):
        self.currOp = ""
        self.oldNumber = 0
        self.setEqual = False
        self.takeOld = False
        self.CurrReset(ui)

    #effectu le calcule demander et l'affiche
    def Equal(self, ui:Ui_MainWindow):
        if self.currOp == "÷" or self.currOp == "1/x":
            dontWorks:bool = False
            if self.currOp == "1/x":
                if self.takeOld:
                    if self.oldNumber == 0:
                        dontWorks = True
                else:
                    if self.currNumber == 0:
                        dontWorks = True
            else:
                if self.currNumber == 0:
                    dontWorks = True
            if dontWorks:
                self.Reset(ui)
                self.currText = "impossible de diviser par 0"
                self.SetText(ui)
                return

        if self.currOp == "sqrt" or self.currOp == "x2" or self.currOp == "1/x":
            if self.takeOld:
                self.oldNumber = self.ops[self.currOp](self.oldNumber)
                self.currText = str(self.oldNumber)
            else:
                self.currNumber = self.ops[self.currOp](self.currNumber)
                self.currText = str(self.currNumber)
            self.SetText(ui)
            return
        else:
            self.oldNumber = self.ops[self.currOp](self.oldNumber, self.currNumber)
            self.currText = str(self.oldNumber)
            self.SetText(ui)
            self.takeOld = True
        self.haveNumber = False
        self.setEqual = False

    #ajoute un opperateur dans l'opperateur courant
    def AddOp(self, currOp:str, ui:Ui_MainWindow):
        temp:str = self.currOp
        self.currOp = currOp
        if self.currOp == "sqrt" or self.currOp == "x2" or self.currOp == "1/x":
            self.Equal(ui)
            self.currOp = temp
            return
        elif self.haveNumber:
            if self.setEqual:
                self.currOp = temp
                self.Equal(ui)
                self.currOp = currOp
                self.setEqual = True
                return
            self.oldNumber = self.currNumber
            self.CurrReset(ui)
        self.setEqual = True




