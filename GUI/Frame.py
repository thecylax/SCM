# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from GUI.settings import *

pygame.font.init()

class Frame:
    def __init__(self, rect=None, caption='', bgcolor=MAGENTA_FG, fgcolor=WHITE, font=None, font_size=14):
        if rect is None:
            self._rect = pygame.Rect(0, 0, 30, 60)
        else:
            self._rect = pygame.Rect(rect)
            
        self._caption = caption
        self._bgcolor = bgcolor
        self._fgcolor = fgcolor
        
        if font is None:
            self._font = pygame.font.Font(FONT, FONT_SIZE)
        else:
            self._font = pygame.font.SysFont(font, font_size)
        
        # Create the surface
        self.surface = pygame.Surface(self._rect.size)
        self._update()
            
    def draw(self, surfaceObj):
        """Blit the current frame appearance to the surface object."""
        surfaceObj.blit(self.surface, self._rect)

    def _update(self):
        """Redraw the button's Surface object. Call this method when the button has changed appearance."""
        w = self._rect.width # syntactic sugar
        h = self._rect.height # syntactic sugar
        
        self.surface.fill(self._bgcolor)

        # draw caption text for all frames
        captionSurf = self._font.render(self._caption, True, self._fgcolor, self._bgcolor)
        captionRect = captionSurf.get_rect()
        #captionRect.center = 0, 0
        captionRect.topleft = 5, 4
        self.surface.blit(captionSurf, captionRect)

        # draw frame border
        pygame.draw.rect(self.surface, WHITE, pygame.Rect((3, 3, w - 6, h - 6)), 1)
