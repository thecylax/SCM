import pygame
from settings import *

class Robot():
    def __init__(self, screen_size):
        self._center = screen_size[0]/2, screen_size[1]/2
        self._x = self._center[0]
        self._y = self._center[1]
        
    def draw(self, surface):
        pygame.draw.polygon(surface, WHITE, [self._center, [self._x-5, self._y+10], [self._x+5, self._y+10]], 0)