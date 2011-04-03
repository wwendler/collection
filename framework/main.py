# framework goes here?
# we really shouldn't be udp focused...?

import sys

# defer.Deferred()
from twisted.internet import defer
from twisted.internet.protocol import Protocol, Factory, ClientFactory
from twisted.protocols.basic import NetstringReceiver

class GameProtocol(NetstringReceiver):
    def stringReceived(self, line):
        if line == "quit":
            print "received disconnect request?"
            self.transport.loseConnection()
        else:
            print "message received: %s" % line

class GameFactory(ClientFactory):
    protocol = GameProtocol
    def __init__(self):
        print "game factory initialized"
    def startFactory(self):
        print "starting client factory"
    def stopFactory(self):
        print "halting client factory"
    def startedConnecting(self):
        print "connecting..."
    def clientConnectionFailed(self):
        print "failed to connect!"
    def clientConnectionLost(self):
        print "lost a connection"

class Game(object):
    def __init__(self):
        self.factory = GameFactory()
        print "game initialized"
    def connect(self, host, port):
        from twisted.internet import reactor
        reactor.connectTCP(host, port, self.factory)
        reactor.run()

class GameServerProtocol(NetstringReceiver):
    def stringReceived(self, line):
        print "message received: %s" % line
        self.num_lines_received += 1
        if (self.num_lines_received > 5):
            self.sendString("quit")
    def connectionMade(self):
        print "connection made."
        self.num_lines_received = 0
        self.sendString("y hello thar\n")
    def connectionLost(self):
        print "connection lost."

class GameServerFactory(Factory):
    protocol = GameServerProtocol
    def __init__(self):
        print "game server factory initialized"
    def startFactory(self):
        print "server factory started"
    def stopFactory(self):
        print "server factory stopped"

class GameServer(object):
    def __init__(self):
        self.factory = GameServerFactory()
        print "game server initialized"
    def listen(self, port):
        from twisted.internet import reactor
        reactor.listenTCP(port, self.factory)
        reactor.run()

def main():
    print "starting up..."
    if len(sys.argv) < 2:
        print "incorrect usage."
        print "for a server: 'server [port]'"
        print "for a client: '[ip] [port]'"
        return
    if sys.argv[1] == 'server':
        print "i am a server"
        server = Server()
        port = int(sys.argv[2])
        protocol = ServerProtocol()
        print "starting server on port %i" % port
        server.listen(port)
    else:
        print "i am a client"
        game = Game()
        ip = sys.argv[1]
        port = int(sys.artv[2])
        print "connecting to %s port %i" % (ip, port)
        game.connect(ip, port)

if __name__ == "__main__":
    main()

