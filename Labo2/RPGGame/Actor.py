from abc import abstractmethod
from ast import In
from re import L
from random import Random


class Actor:
    __m_Tag:str

    __m_MaxLife:int
    __m_CurrLife:int

    __m_DamageMelee:int
    __m_DamageRange:int
    __m_Armor:int
    __m_EsquiveChance:int
    __m_EscapeChance:int

    __m_NameAttMelee:str
    __m_NameAttRange:str
    __m_NameClass:str

    __m_IsPlayer:bool
    __m_IsDie:bool
    __m_IsEscape:bool

    def __init__ (self, tag:str):
        self.__m_Tag = tag

    def SetLife(self, life:int):
        self.__m_MaxLife = life

    def SetDamage(self, melee:int, range:int):
        self.__m_DamageMelee = melee
        self.__m_DamageRange = range

    def SetArmor(self, armor:int):
        self.__m_Armor = armor

    def SetNameAtt(self, melee:int, range:int):
        self.__m_NameAttMelee = melee
        self.__m_NameAttRange = range

    def SetClass(self, name:str, isPlayer:bool):
        self.__m_NameClass = name
        self.__m_IsPlayer = isPlayer

    def SetIsDie(self, isDie:bool):
        self.__m_IsDie = isDie

    def SetEsquiveChance(self, chance:int):
        self.__m_EsquiveChance = chance

    def SetEscapeChance(self, chance:int):
        self.__m_EscapeChance = chance

    def GetIsDie(self):
        return self.__m_IsDie

    def GetClassName(self):
        return self.__m_NameClass

    def GetTag(self):
        return self.__m_Tag

    def GetNameAttMelee(self):
        return self.__m_NameAttMelee

    def GetNameAttRange(self):
        return self.__m_NameAttRange

    def GetCurrLife(self):
        return self.__m_CurrLife

    def GetMaxLife(self):
        return self.__m_MaxLife

    def GetMeleeDamage(self):
        return self.__m_DamageMelee

    def GetRangeDamage(self):
        return self.__m_DamageRange

    def GetIsEscape(self):
        return self.__m_IsEscape

    def TakeDamage(self, damage:int):
        if damage < 0:
            damage = 0
        self.__m_CurrLife -= damage
        if self.__m_CurrLife <= 0:
            self.__m_CurrLife = 0
            self.SetIsDie(True)

    def Reset(self):
        self.__m_CurrLife = self.__m_MaxLife
        self.__m_IsEscape = False
        self.SetIsDie(False)

    def Idle(self, damage:int):
        self.TakeDamage(damage)

    def Block(self, damage:int):
        self.TakeDamage(damage - self.__m_Armor)

    def Dodge(self, damage:int):
        rand:Random = Random()
        if(Random.randint(rand, 0, 100) > self.__m_EsquiveChance):
            self.TakeDamage(damage)
            return False
        else:
            return True

    def Escape(self):
        rand:Random = Random()
        if(Random.randint(rand, 0, 100) > self.__m_EscapeChance):
            self.TakeDamage(self.__m_MaxLife)
            return False
        else:
            self.__m_IsEscape = True
            return True

    @abstractmethod
    def ChooseActions(self, damage:int):
        pass

    @abstractmethod
    def ChooseAtt(self):
        pass

    @abstractmethod
    def Start(self):
        pass

    @abstractmethod
    def Update(self):
        pass
