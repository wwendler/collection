# game.py
# this should hold the display loop and input code
# april 8 2011
import pygame
import mapdata

class Interface:
    def __init__(self):
        pygame.init()
        self.size = (320, 320)
        self.display = pygame.display.set_mode(self.size, pygame.DOUBLEBUF)
        print "display initialized!"
    def on_quit(self):
        pygame.quit()
        print "display uninitialized"
    def do_event(self, event, my_map):
        if event.type == pygame.QUIT:
            print "quitting?"
            return False
        return True
    def handleEvents(self, my_map):
        for event in pygame.event.get():
            try:
                keep_running = self.do_event(event, my_map)
            except Exception, e:
                print "problem with event handling, quitting cleanly"
                self.on_quit()
                raise e
            if not keep_running:
                self.on_quit()
                return False
        return True
    def draw(self, my_map):
        try:
            my_map.draw(self.display,
                        (self.size[0]/2, self.size[1]/2))
        except Exception, e:
            print "problem with display, quitting cleanly"
            self.on_quit()
            raise e
        pygame.display.flip()

def main():
    print "starting test game without twisted..."
    game = Interface()
    game_map = mapdata.GameMap()
    while (game.handleEvents(game_map)):
        game.draw(game_map)
    print "goodbye!"

if __name__ == "__main__":
    main()
