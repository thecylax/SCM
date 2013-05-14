import pygame
from GUI.settings import *

class Map():
    def __init__(self, color, screen_size):
        self._color = color
        self._x = screen_size[0]/2
        self._y = screen_size[1]/2
        
    def drawWall(self, surface, pointlist):
        mapped_points = []
        for point in pointlist:
            mapped_points.append([self._x+point[0], self._y-point[1]])
        
        pygame.draw.lines(surface, self._color, False, mapped_points, 4)
        for point in mapped_points:
            pygame.draw.circle(surface, RED, point, 2)