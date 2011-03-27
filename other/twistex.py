# this is the main bit of code, I guess? Includes twisted junk

import sys

from twisted.internet import defer
from twisted.internet.protocol import Protocol, ClientFactor
from twisted.protocols.basic import NetstringReceiver

import pygame

import data
import disp

class GameProtocol(NetstringReceiver):
    def stringReceived(self, line):
        words = line.split()
        if words[0] == 'newasteroid':
            ast = asteroid(int(words[2]), float(words[3]),
                    float(words[4]), float(words[5]), float(words[6]),
                    float(words[7]), float(words[8]), float(words[9]))
            self.factory.makeAsteroid(int(words[1]), ast)
        elif words[0] == 'delasteroid':
            self.factor.delAsteroid(int(words[1]))
        elif words[0] == 'newship':
            ship = ship(float(words[3]), float(words[4]))
            self.factory.makeShip(int(words[1]), ship)
        elif words[0] == 'delship':
            self.factory.delShip(int(words[1]))
        elif words[0] == 'modship':
            self.factory.modShip(int(words[1]), int(words[2]), float(words[3]), float(words[4]), float(words[5]), float(words[6]), float(words[7]))
        elif words[0] == 'turnship':
            self.factory.setShipTurn(int(words[1]), int(words[2]))
        elif words[0] == 'accship':
            self.factory.setShipAcc(int(words[1]), int(words[2]))
        elif words[0] == 'newgame':
            player = playerShip(int(float(words[2]), float(words[3])))
            self.factory.startGame(int(words[1]), player)
    def sendShipData(self, stime, xpos, ypos, xvel, yvel, theta):
        phrase = 'modship %f %f %f %f %f %f' % (stime, xpos, ypos,
                xvel, yvel, theta)
        self.sendString(phrase)
    def sendTurn(self, turn):
        phrase = 'turnship %i' % (turn)
        self.sendString(phrase)
    def sendAcc(self, acc):
        phrase = 'accship %i' % (acc)
        self.sendString(phrase)

class GameFactory(ClientFactory):
    protocol = GameProtocol
    def __init__(self, map, setTime):
        self.map = map
        self.setTime = setTime
    def makeAsteroid(self, astid, ast):
        self.map.addAsteroid(ast, astid)
    def delAsteroid(self, astid):
        self.map.delAsteroid(astid)
    def makeShip(self, shipid, ship):
        self.map.addShip(ship, shipid)
    def delShip(self, shipid):
        self.map.delShip(shipid)
    def modShip(self, shipid, stime, xpos, ypos, xvel, yvel, theta):
        self.map.ships[shipid].update(stime, xpos, ypos, xvel, yvel, theta)
    def setShipTurn(self, shipid, turn):
        self.map.ships[shipid].setTurn(turn)
    def setShipAcc(self, shipid, acc):
        self.map.ships[shipid].setAcc(acc)
    def startGame(self, stime, p):
        self.map.addPlayer(p)
        self.setTime(stime)

class Game():
    def __init__(self):
        self.map = Map(1000,1000)
        self.disp = disp.Display(600, 400)
    def connect(self, host, port):
        from twisted.internet import reactor
        reactor.connectTCP(host, port,
            GameFactory(self.map, self.disp.setTime))
        reactor.run()

def main():
    if len(sys.argv) == 3:
    	print "I am a client."
        twast = Game()
        ip = sys.argv[1]
        port = int(sys.argv[2])
        twast.connect(ip, port)
    elif len(sys.argv) == 2:
        print "I am a server."
    else
    	print "wrong number of args"

if __name__ == '__main__':
    main()
