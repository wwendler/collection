# mon.py
# code for characters, monsters, etc

class MonType (object):
    def __init__(self, name, attributes, stats, sprite):
        self.name = str(name)
        self.attr = {}
        for x in attributes:
            self.attr[str(x)] = True
        self.stats = {}
        for x in stats:
            self.stats[str(x)] = int(stats[x])
        self.sprite = str(sprite)
    def makeInstance(self, name):
        pass

class Mon (object):
    def __init__(self, name, mon_type, type_list):
        self.name = str(name)
        self.mon_type = str(mon_type)
        self.current_stats = type_list.getType(self.mon_type).stats
    def isDead(self):
        pass
class MonTypes(object):
    pass
