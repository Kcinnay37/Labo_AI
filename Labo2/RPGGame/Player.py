from time import sleep
from Actor import Actor
import os

class Player(Actor):

    __m_Target:Actor

    def __init__(self, tag:str):
        super().__init__(tag)

    def SetTarget(self, target:Actor):
        self.__m_Target = target

    def Start(self):
        self.Reset()

    def Update(self):
        self.ChooseAtt()

    #fontion qui permet au joueur de choisir sont action
    def ChooseActions(self, damage:int):
        nb:int = int(input("bloquer : 1\nesquiver : 2\nidle : 3\nchoisiser votre action : "))

        if nb == 1:
            self.Block(damage)
            print("vous avez bloquer l'attaque de l'enemie")
        elif nb == 2:
            if self.Dodge(damage):
                print("vous avez esquiver l'attaque de l'enemie")
            else:
                print("vous avez tanter d'esquiver l'attaque de l'enemie et ca la echouer")
        elif nb == 3:
            self.Idle(damage)
            print("vous avez rester imobile lors de l'attaque")
        else:
            self.ChooseActions(damage)

        if nb == 1 or nb == 2 or nb == 3:
            sleep(2)

    #fontion qui permet au joueur de choisir sont attaque
    def ChooseAtt(self):
        os.system("cls")
        print("vous etes a " + str(self.GetCurrLife()) + " point de vie")
        print("cest a votre tour d'attaquer")

        pourcentLife = self.GetCurrLife() * 100
        pourcentLife /= self.GetMaxLife()

        nb:int = 0

        if pourcentLife > 25:
            while nb != 1 and nb != 2:
                nb = int(input(self.GetNameAttMelee() + " : 1\n" + self.GetNameAttRange() + " : 2\nchoisiser votre attaque : "))
            if nb == 1:
                self.__m_Target.ChooseActions(self.GetMeleeDamage())
            elif nb == 2:
                self.__m_Target.ChooseActions(self.GetRangeDamage())
        else:
            while nb != 1 and nb != 2 and nb != 3:
                nb = int(input(self.GetNameAttMelee() + " : 1\n" + self.GetNameAttRange() + " : 2\n" + "prendre la fuite : 3\n" + "choisiser votre attaque : "))
            if nb == 1:
                self.__m_Target.ChooseActions(self.GetMeleeDamage())
            elif nb == 2:
                self.__m_Target.ChooseActions(self.GetRangeDamage())
            elif nb == 3:
                if self.Escape():
                    print("vous vous etes achaper de l'enemie")
                else:
                    print("vous avez tanter de vous echaper de l'enemie mais il vous a tuer")
                sleep(2)
