from cmath import acos
import imp
from tkinter import dialog
from typing import Sequence
from Engine import Engine
from Actor import Actor
from Enemy import Enemy
from Player import Player
from Level import Level
import os


class Logic:

    __m_Engine:Engine
    __m_ListActorPlayer:Player = []
    __m_ListActorEnemy:Enemy = []
    __m_ListLevel:Level = []

    __m_IsInitiate:bool = False

    __m_CurrIndexLevel:int

    __m_NbEnemyToKill:int = 3
    __m_CurrNbEnemyKill:int = 0

    __m_IsPlaying:bool = True

    def __init__(self):
        self.__m_Engine = Engine()

    #initialise les objects du jeu
    def InitiateObjects(self):
        chevalier:Player = Player("player")
        chevalier.SetClass("chevalier", True)
        chevalier.SetArmor(20)
        chevalier.SetDamage(30, 25)
        chevalier.SetLife(100)
        chevalier.SetNameAtt("coup d'épée", "lancer de fleche")
        chevalier.SetEsquiveChance(20)
        chevalier.SetEscapeChance(30)
        self.__m_ListActorPlayer.append(chevalier)

        magicien:Player = Player("player")
        magicien.SetClass("magicien", True)
        magicien.SetArmor(10)
        magicien.SetDamage(25, 30)
        magicien.SetLife(80)
        magicien.SetNameAtt("vomi de lave", "fus ro dah")
        magicien.SetEsquiveChance(20)
        magicien.SetEscapeChance(40)
        self.__m_ListActorPlayer.append(magicien)

        rogue:Player = Player("player")
        rogue.SetClass("rogue", True)
        rogue.SetArmor(15)
        rogue.SetDamage(25, 25)
        rogue.SetLife(90)
        rogue.SetNameAtt("coup de couteau a la gorge", "lancer du couteau")
        rogue.SetEsquiveChance(50)
        rogue.SetEscapeChance(60)
        self.__m_ListActorPlayer.append(rogue)

        gobelin:Enemy = Enemy("enemy")
        gobelin.SetClass("gobelin", False)
        gobelin.SetArmor(10)
        gobelin.SetDamage(25, 25)
        gobelin.SetLife(100)
        gobelin.SetNameAtt("coup de massu", "lancer une roche")
        gobelin.SetEsquiveChance(50)
        gobelin.SetEscapeChance(60)
        gobelin.SetChanceChooseTotalHundred(30, 50, 20)
        gobelin.SetChanceChooseEscapeAndMelee(70, 50)

        self.__m_ListActorEnemy.append(gobelin)

        zombie:Enemy = Enemy("enemy")
        zombie.SetClass("zombie", False)
        zombie.SetArmor(5)
        zombie.SetDamage(35, 22)
        zombie.SetLife(100)
        zombie.SetNameAtt("morsure", "lancer de boue")
        zombie.SetEsquiveChance(15)
        zombie.SetEscapeChance(20)
        zombie.SetChanceChooseTotalHundred(50, 0, 50)
        zombie.SetChanceChooseEscapeAndMelee(20, 70)
        self.__m_ListActorEnemy.append(zombie)

        troll:Enemy = Enemy("enemy")
        troll.SetClass("troll", False)
        troll.SetArmor(25)
        troll.SetDamage(25, 25)
        troll.SetLife(150)
        troll.SetNameAtt("coup de point", "crie")
        troll.SetEsquiveChance(15)
        troll.SetEscapeChance(10)
        troll.SetChanceChooseTotalHundred(75, 5, 20)
        troll.SetChanceChooseEscapeAndMelee(30, 50)
        self.__m_ListActorEnemy.append(troll)

        foret:Level = Level("foret", gobelin)
        self.__m_ListLevel.append(foret)

        marecage:Level = Level("marecage", zombie)
        self.__m_ListLevel.append(marecage)

        caverne:Level = Level("caverne", troll)
        self.__m_ListLevel.append(caverne)

    #fonction pour demander a l'utilisateur de choisir ca class et la mets dans l'engine
    def ChooseClass(self):
        os.system("cls")

        dialogue:str = ["Bienvenue vous devez remporter 3 victoire pour pour recevoir les louange du roi",
                        "choisi votre class : "]

        print(dialogue[0])

        for i in range(len(self.__m_ListActorPlayer)):
            print(self.__m_ListActorPlayer[i].GetClassName() + " : " + str(i))


        nb:int = int(input(dialogue[1]))

        if nb >= 0 and nb < len(self.__m_ListActorPlayer):
            self.__m_Engine.AddActor(self.__m_ListActorPlayer[nb])
        else:
            self.ChooseClass()

    #fontion pour demander a l'utilisateur de choisir sont level et mets l'enemie dans l'engine
    def ChooseLevel(self):
        os.system("cls")

        dialogue:str = ["choisi le level ou vous voulez aller : "]

        for i in range(len(self.__m_ListLevel)):
            print(self.__m_ListLevel[i].GetName() + " : " + str(i))

        nb:int = int(input(dialogue[0]))

        if nb >= 0 and nb < len(self.__m_ListLevel):
            for i in range(len(self.__m_ListActorEnemy)):
                if self.__m_ListLevel[nb].GetEnemyType() == self.__m_ListActorEnemy[i]:
                    self.__m_Engine.AddActor(self.__m_ListActorEnemy[i])
                    self.__m_CurrLevelIndex = nb
        else:
            self.ChooseLevel()

    #la sequence lorsque le joueur arrive dans le level
    def SequenceArriveLevel(self):
        os.system("cls")

        dialogue:str = ["vous venez d'arriver dans le level : ",
                        "oui : 1\nnon : 2\nvous rencontrez un ",
                        " voulez vous l'afronter sinon reparter couver de honte au chateau : "]

        print(dialogue[0] + self.__m_ListLevel[self.__m_CurrLevelIndex].GetName())
        nb:int = int(input(dialogue[1] +
                            self.__m_ListLevel[self.__m_CurrLevelIndex].GetEnemyType().GetClassName() +
                            dialogue[2]))
        if nb == 1 or nb == 2:
            if nb == 1:
                return True
            else:
                return False
        else:
            self.SequenceArriveLevel()

    #la sequence lorsque le joueur arrive au chateau
    def SequenceChateau(self, winer:bool):
        os.system("cls")
        if winer:
            print("vous arriver au chateau avec la tete des creatur tuer le roi pour vous recompencer\n" \
                    "vous offre la main de ca fille et vous vivez heureux")
        else:
            print("vous arriver au chateau couvert de honte le roi n'en revien pas\n" \
                    "il vous prend de force et vous amene sur la gillotine vous executer\n" \
                    "publiquement pour montrer l'exemple")

    #la sequence apres le combas
    def SequenceAfterFight(self):
        os.system("cls")

        dialogue:str = ["le combat est terminer vous etes rendu a ",
                        "oui : 1\nnon : 2\nvoulez vous continuer votre periple ou repartir au chateau comme un lache : ",
                        "aller recolter les louange aupres du roi : 1\n" \
                        "aller vivre modestement dans les bois : 2\n" \
                        "vous avez atteind le nombre de victoir requi voulez vous aller recolter vos louange\n" \
                        "au chateau ou vivre modestement : "]

        if not self.__m_Engine.GetWithTag("player").GetIsDie():
            print(dialogue[0] + str(self.__m_CurrNbEnemyKill) + " victoir")
            if self.__m_CurrNbEnemyKill == self.__m_NbEnemyToKill:
                nb:int = int(input(dialogue[2]))
                if nb == 1:
                    return True
                elif nb == 2:
                    return False
                else:
                    self.SequenceAfterFight()
            else:
                nb:int = int(input(dialogue[1]))
                if nb == 1:
                    self.__m_Engine.RemoveWithTag("enemy")
                    return True
                elif nb == 2:
                    return False
                else:
                    self.SequenceAfterFight()
        else:
            print("loss")

    #la sequence durant le combat ou l'engine est appeler
    def SequenceFight(self):
        os.system("cls")

        self.__m_Engine.GetWithTag("player").SetTarget(self.__m_Engine.GetWithTag("enemy"))
        self.__m_Engine.GetWithTag("enemy").SetTarget(self.__m_Engine.GetWithTag("player"))

        self.__m_Engine.Start()
        while self.__m_Engine.GetIsRunning():
            self.__m_Engine.Update()

        if not self.__m_Engine.GetWithTag("player").GetIsDie():
            if self.__m_Engine.GetWithTag("enemy").GetIsDie():
                self.__m_CurrNbEnemyKill += 1
            return False
        else:
            return True

    #le update de la game
    def UpdateGame(self):
        self.ChooseClass()
        while self.__m_IsPlaying:
            self.ChooseLevel()
            if self.SequenceArriveLevel():
                if self.SequenceFight():
                    os.system("cls")
                    print("vous etes mort nullos")
                    self.__m_IsPlaying = False
                else:
                    if self.SequenceAfterFight():
                        if self.__m_CurrNbEnemyKill == self.__m_NbEnemyToKill:
                            self.SequenceChateau(True)
                            self.__m_IsPlaying = False
                        else:
                            continue
                    else:
                        if self.__m_CurrNbEnemyKill == self.__m_NbEnemyToKill:
                            os.system("cls")
                            print("vous allez vivre dans une petite maison dans les vois et vous vivez une belle vie")
                        else:
                            self.SequenceChateau(False)
                        self.__m_IsPlaying = False
            else:
                self.SequenceChateau(False)
                self.__m_IsPlaying = False

        nb:int = int(input("oui : 1\nnon : 2\nvoulez vous recommencer le jeu : "))
        if nb == 1:
            self.StartGame()

    #le start de la game
    def StartGame(self):
        self.__m_Engine.Reset()
        if not self.__m_IsInitiate:
            self.InitiateObjects()
            self.__m_IsInitiate = True
        self.__m_IsPlaying = True
        self.__m_CurrNbEnemyKill = 0
        self.UpdateGame()
