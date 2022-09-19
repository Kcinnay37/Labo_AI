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
    newNumber:bool = False
    isEqual:bool = True
    addOpResetUI = True

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

        self.newNumber = True
        self.SetText(ui)

    #prend le text courant de la calculatrice et le fais afficher
    def SetText(self, ui:Ui_MainWindow):
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
        self.CurrReset(ui)
        self.isEqual = True

    #effectu le calcule demander et l'affiche
    def Equal(self, ui:Ui_MainWindow):
        self.isEqual = True
        self.haveNumber = False

        if self.currOp == "":
            return

        if self.newNumber:
            self.currNumber = float(self.currText)
            self.newNumber = False

        if (self.currOp == "÷" or self.currOp == "1/x") and self.currNumber == 0:
            self.Reset(ui)
            self.currText = "impossible de diviser par 0"
            self.SetText(ui)
            return

        nb:float = 0

        if self.currOp == "1/x" or self.currOp == "x2" or self.currOp == "sqrt":
            nb = self.ops[self.currOp](self.currNumber)
            self.currOp = ""
        else:
            nb = self.ops[self.currOp](self.oldNumber, self.currNumber)
            self.oldNumber = nb

        self.currText = str(nb)

        if self.currText[len(self.currText) - 2] == '.' and self.currText[len(self.currText) - 1] == '0':
            self.currText = self.currText[:len(self.currText) - 2]

        if nb == 0:
            self.haveNumber = False

        self.SetText(ui)

    #ajoute un opperateur dans l'opperateur courant
    def AddOp(self, currOp:str, ui:Ui_MainWindow):
        if self.haveNumber:
            self.addOpResetUI = True
        if not self.isEqual and self.haveNumber:
            self.Equal(ui)
            self.addOpResetUI = False
            self.haveNumber = False
        self.isEqual = False

        self.currOp = currOp
        self.oldNumber = float(self.currText)
        self.newNumber = True

        if self.currOp == "1/x" or self.currOp == "x2" or self.currOp == "sqrt":
            self.Equal(ui)
            return

        if self.addOpResetUI:
            self.CurrReset(ui)


