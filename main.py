#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from GUI import Buttons, Events, Frame
from GUI.robot import Robot
from GUI.map import Map
from GUI.settings import *
 
class App(Events.SCMEvent):
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self._x = self.size[0]/2
        self._y = self.size[1]/2
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Sophia Console Monitor')
        self._display_surf.fill(MAGENTA_BG)
        self._clock = pygame.time.Clock()
        self._running = True
 
    def on_loop(self):
        pass

    def on_render(self):
        self.LoadButtons()
        self.load_frame()

        r = Robot(self.size)
        r.draw(self._display_surf)
        
        w = Map(GREEN, self.size)
        w.drawWall(self._display_surf, [[10, 0],
                                        [8, 2],
                                        [6, 4],
                                        [4, 6],
                                        [0, 10],
                                        [-10, 14],
                                        [-12, 10],
                                        [-14, 8],
                                        [-15, 0]])
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            self._clock.tick(10)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    # Start of UI elements
    def LoadButtons(self):
        # Sidebar buttons, 40px vertical distance
        self.Button1 = Buttons.Button()
        self.Button1.create_button(self._display_surf, MAGENTA_WIDGET, 10, 5, 100, 30, 0, 'Sensors', WHITE)

        self.Button2 = Buttons.Button()
        self.Button2.create_button(self._display_surf, MAGENTA_WIDGET, 10, 45, 100, 30, 0, 'Settings', WHITE)

        self.Button3 = Buttons.Button()
        self.Button3.create_button(self._display_surf, MAGENTA_WIDGET, 10, 85, 100, 30, 0, 'Quit', WHITE)

    def load_frame(self):
        self.Frame1 = Frame.Frame()
        self.Frame1.create_frame(self._display_surf, MAGENTA_WIDGET, 120, 5, self.size[0]-125, self.size[1]-10, 0, 'Frame', WHITE)
        
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
