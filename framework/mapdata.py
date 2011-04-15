# map framework goes here
# april 08 2011

import pygame.image

# a tile object.
class Tile(object):
    def __init__(self, name, attributes, sprite):
        self.name = str(name)
        self.attr = {}
        for x in attributes:
            self.attr[str(x)] = True
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
        return self.tiles[name].is_wall
    def getSprite(self, name):
        return self.tiles[name].sprite

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
        self.size = 64
        self.center = (0, 0)
        print "game map initialized"
    def dumbMap(self):
        self.map[(0, 0)] = 'default'
        self.map[(1, 1)] = 'default'
        self.map[(1, 0)] = 'default'
        print "dumb map created"
    # x and y are the center of the surface that will be drawn onto
    # we need to check that we are only draing inside the area of the
    # surface, although perhaps pygame handles that well?
    def draw(self, surface, (x, y)):
        for loc in self.map:
            sprite_name = self.types.getSprite(self.map[loc])
            xpos = x + (loc[0] - self.center[0])*self.size
            ypos = y + (loc[1] - self.center[1])*self.size
            surface.blit(self.sprites.getSprite(sprite_name),
                         (xpos, ypos))
    # return map data in easily sendable chunks
    def getMap(self):
        lines = []
        for x in self.map:
            line = "TILE %i %i %s" % (x[0], x[1], self.map[x])
            lines.append(line)
        return lines
    def addTile(self, loc, name):
        print 'added tile!'
        self.map[loc] = name

