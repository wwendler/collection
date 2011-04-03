# map framework goes here
# april 03 2011

class Tile(object):
    def __init__(self):
        pass

class TileTypes(object):
    def __init__(self):
        self.tiles = {}
    def addTile(self, name, attributes):
        if name in self.tiles:
            raise Exception("%s already defined as a tile!" % name)
        attr = {}
        for x in attributes:
            attr[str(x)] = bool(attributes[x])
        if "passable" not in attr:
            attr["passable"] = True
        if "sprite" not in attr:
            attr["sprite"] = 
        self.tiles[x] = attr
    def hasAttribute(self, name):
        return name in self.tiles[name]
    def isTile(self, name, attribute):
        return self.tiles[name][attribute]
    def isPassable(self, name):
        pass
    def getSprite

class GameMap(object):
    def __init__(self):
        self.types = TileTypes()
        
        print "game map initialized"
    
