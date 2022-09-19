from Enemy import Enemy

class Level:

    __m_Name:str

    __m_EnemyType:Enemy

    def __init__(self, name:str, enemyType:Enemy):
        self.__m_Name = name
        self.__m_EnemyType = enemyType

    def GetName(self):
        return self.__m_Name

    def GetEnemyType(self):
        return self.__m_EnemyType
