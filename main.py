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
        self.size = self.weight, self.height = 800, 600
        self._x = self.size[0]
        self._y = self.size[1]
 
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
        self.load_buttons()
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
#    def on_event(self, event):
#        self.buttonHello.handleEvent(event)
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            self._clock.tick(10)
        self.on_cleanup()

    # Start of UI elements
    def load_buttons(self):
        right = 2
        sensors_btn = Buttons.Button((right, 2, 106, 35), 'Sensors')
        sensors_btn.draw(self._display_surf)
        
        settings_btn = Buttons.Button((right, 39, 106, 35), 'Settings')
        settings_btn.draw(self._display_surf)
        
        quit_btn = Buttons.Button((right, 76, 106, 35), 'Quit')
        quit_btn.draw(self._display_surf)
        
    def load_frame(self):
        self.Frame1 = Frame.Frame((110, 2, self._x - 112, self._y - 4), caption='Frame', font='Courier black', font_size=20)
        self.Frame1.draw(self._display_surf)
        
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
