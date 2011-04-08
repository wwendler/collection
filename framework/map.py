# map framework goes here
# april 08 2011

import pygame.image

# a tile object.
class Tile(object):
    def __init__(self, name, attributes, sprite):
        self.name = str(name)
        attr = {}
        for x in attributes:
            attr[str(x)] = True
        if 'passable' in attr:
            self.is_wall = False
        else:
            self.is_wall = True
        self.sprite = str(sprite)

# holds all tiles, has a bunch of wrapper functions
class TileTypes(object):
    def __init__(self):
        self.tiles = {}
    def newTile(self, name, attributes, sprite):
        self.tiles[str(name)] = Tile(name, attributes, sprite)
    def addTile(self, tile):
        self.tiles[tile.name] = tile
    def hasAttribute(self, name, attribute):
        return attribute in self.tiles[name].attr
    def isTile(self, name):
        return name in self.tile
    def isPassable(self, name):
        return self.tile[name].is_wall
    def getSprite(self, name):
        return self.tile[name].sprite

# old sprites, methods to load them go here
class SpriteList(object):
    def __init__(self):
        self.sprites = {}
    def loadSprite(self, name, filename):
        surface = pygame.image.load(filename)
        self.sprites[str(name)] = surface
    def getSprite(self, name):
        return self.sprites[name]

class GameMap(object):
    def __init__(self):
        self.types = TileTypes()
        self.sprites = SpriteList()
        self.sprites.loadSprite('none', 'img/def.png')
        self.types.newTile('default', ('silly'), 'none')
        self.map = {}
        self.map[(0, 0)] = 'default'
        self.map[(1, 1)] = 'default'
        self.map[(1, 0)] = 'default'
        self.size = 64
        self.center = (0, 0)
        print "game map initialized"
    # x and y are the center of the surface that will be drawn onto
    # we need to check that we are only draing inside the area of the
    # surface, although perhaps pygame handles that well?
    def draw(self, surface, (x, y)):
        for loc in map:
            surface.blit(self.types.getSprite(self.map[loc]),
                         (x + (loc[0] - self.center[0])*self.size,
                          y + (loc[1] - self.center[1])*self.size))


