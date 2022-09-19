from random import Random
from time import sleep
from Actor import Actor
import os

class Enemy(Actor):
    def __init__(self, tag:str):
        super().__init__(tag)

    __m_ChanceChooseBlock:int
    __m_ChanceChooseDodge:int
    __m_ChanceChooseIdle:int
    __m_ChanceChooseEscape:int
    __m_ChanceChooseMelee:int

    __m_Target:Actor

    def SetTarget(self, target:Actor):
        self.__m_Target = target

    def SetChanceChooseTotalHundred(self, block:int, dodge:int, idle:int):
        self.__m_ChanceChooseBlock = block
        self.__m_ChanceChooseDodge = dodge
        self.__m_ChanceChooseIdle = idle

    def SetChanceChooseEscapeAndMelee(self, escape:int, melee:int):
        self.__m_ChanceChooseEscape = escape
        self.__m_ChanceChooseMelee = melee

    #lancer au debut du combat
    def Start(self):
        self.Reset()

    #l'update du combat
    def Update(self):
        os.system("cls")
        print("l'enemie est a " + str(self.GetCurrLife()) + " point de vie")
        print("cest au tour de l'enemie d'attaquer")
        self.ChooseAtt()

    #fonction qui permet a l'enemie de choisir sont action
    def ChooseActions(self, damage:int):
        rand:Random = Random()
        chance:int = Random.randint(rand, 0, 100)
        if chance <= self.__m_ChanceChooseBlock:
            self.Block(damage)
            print("l'enemie a bloquer votre attaque")
        elif chance <= self.__m_ChanceChooseBlock + self.__m_ChanceChooseDodge:
            if self.Dodge(damage):
                print("l'enemie a esquiver votre attaque")
            else:
                print("l'enemie a tenter une esquive qui a echouer")
        else:
            self.Idle(damage)
            print("l'enemie est rester immobile durant l'attaque")
        sleep(2)


    #fonction qui permet a l'enemie de choisir sont attaque
    def ChooseAtt(self):
        pourcentLife = self.GetCurrLife() * 100
        pourcentLife /= self.GetMaxLife()

        rand:Random = Random()

        if pourcentLife < 25:
            nb:int = Random.randint(rand, 0, 100)
            if nb <= self.__m_ChanceChooseEscape:
                if self.Escape():
                    print("l'enemie c'est echaper et vous n'avez rien pu faire")
                else:
                    print("l'enemi a tanter de s'echaper mais vous l'aver tuer")
                sleep(2)
                return

        nb:int = Random.randint(rand, 0, 100)
        if nb <= self.__m_ChanceChooseMelee:
            print("l'enemie vous fais sont attaque " + self.GetNameAttMelee())
            self.__m_Target.ChooseActions(self.GetMeleeDamage())
        else:
            print("l'enemie vous fais sont attaque " + self.GetNameAttRange())
            self.__m_Target.ChooseActions(self.GetRangeDamage())
