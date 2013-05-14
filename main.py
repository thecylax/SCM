import pygame
from pygame.locals import *
import events
from button import *
from GUI.robot import Robot
from GUI.map import Map
from GUI.settings import *
 
class App(events.SCMEvent):
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
        self._clock = pygame.time.Clock()
        self._running = True
 
#    def on_event(self, event):
#        if event.type == pygame.QUIT:
#            self._running = False
    def on_loop(self):
        pass

    def on_render(self):
        self.LoadButtons()
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
        #pass
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

    def LoadButtons(self):
        t1 = Teste(0, 0)
        t1.draw(self._display_surf)
        t2 = Teste(0, 30)
        t2.draw(self._display_surf)
#        self.button = Button()
#        self.button.setCoords(10, 10)
#        self.button_sprites = pygame.sprite.RenderPlain((self.button))
        
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()