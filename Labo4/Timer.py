import pygame

class Timer:
    _clock = None
    _dt:float = 0

    def __init__(self):
        self._clock = pygame.time.Clock()

    def Update(self):
        self._dt = self._clock.tick(60)/1000

    def GetDeltaTime(self):
        return self._dt
