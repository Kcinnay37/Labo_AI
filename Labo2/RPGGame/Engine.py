from asyncio.windows_events import NULL
from Actor import Actor
import sys


class Engine:

    __m_ListActors:Actor = []
    __m_IsRunning:bool

    def __init__(self):
        self.__m_IsRunning = True

    def AddActor(self, actor:Actor):
        self.__m_ListActors.append(actor)

    def DelActor(self, actor:Actor):
        for i in range(self.__m_ListActors.count):
            if self.__m_ListActors[i] == actor:
                self.__m_ListActors[i].remove

    def SetIsRunning(self, isRunning:bool):
        self.__m_IsRunning = isRunning

    def GetIsRunning(self):
        return self.__m_IsRunning

    def GetNbInList(self):
        return len(self.__m_ListActors)

    def RemoveWithTag(self, tag:str):
        for i in range(len(self.__m_ListActors)):
            if self.__m_ListActors[i].GetTag() == tag:
                self.__m_ListActors.remove(self.__m_ListActors[i])
                i -= 1

    def GetWithTag(self, tag:str):
        for i in range(len(self.__m_ListActors)):
            if self.__m_ListActors[i].GetTag() == tag:
                return self.__m_ListActors[i]
        return NULL

    def Reset(self):
        self.__m_ListActors.clear()

    #lance les start des acteur en jeux
    def Start(self):
        self.SetIsRunning(True)
        for i in range(len(self.__m_ListActors)):
            self.__m_ListActors[i].Start()

    #lance les update de l'enemie et du joueur jusqua que le combat soi fini
    def Update(self):
        for i in range(len(self.__m_ListActors)):
            if self.__m_ListActors[i].GetIsEscape() or self.__m_ListActors[i].GetIsDie():
                self.SetIsRunning(False)
                break

            self.__m_ListActors[i].Update()

            if self.__m_ListActors[i].GetIsEscape() or self.__m_ListActors[i].GetIsDie():
                self.SetIsRunning(False)
                break
