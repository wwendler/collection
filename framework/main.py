# framework goes here?
# we really shouldn't be udp focused...?
# april 03 2011

import sys

# defer.Deferred()
from twisted.internet import defer
from twisted.internet.protocol import Protocol, Factory, ClientFactory
from twisted.protocols.basic import NetstringReceiver
from twisted.python import log

from twisted.internet import reactor, threads, task

class InputGetter(object):
    def __init__():
        self.safe = True
    def getInput():
        line = raw_input("what you say? ")
        return line

class GameProtocol(NetstringReceiver):
    def mySendString(self, line):
        print "sending message: %s" % line
        self.sendString(line)
    def stringReceived(self, line):
        if line == "quit":
            print "received disconnect request?"
            self.transport.loseConnection()
            return
        if line == "y hello thar":
            print "server is ready!"
            self.startInputLoop()
            #d = self.factory.getLine()
            #d = threads.deferToThread(getInput)
            #d.addCallback(self.mySendString)
            #d.addErrback(log.err)
            #d.addCallback(self.factory.getLine)
        else:
            print "message received: %s" % line
    def connectionMade(self):
        print "protocol has a connection"
    def connectionLost(self, reason):
        print "protocol lost a connection"
        print "reason: %s" % reason.getErrorMessage()
        reason.printTraceback()
    def startInputLoop(self, _=None):
        d = threads.deferToThread(getInput)
        d.addCallback(self.mySendString)
        d.addErrback(log.err)
        d.addCallback(self.startInputLoop)

class GameFactory(ClientFactory):
    protocol = GameProtocol
    def __init__(self):
        print "game factory initialized"
    def startFactory(self):
        print "starting client factory"
    def stopFactory(self):
        print "halting client factory, and quitting"
        #from twisted.internet import reactor
        reactor.stop()
    def startedConnecting(self, connector):
        print "connecting..."
    # reason is a twisted.python.failure object
    def clientConnectionFailed(self, connector, reason):
        print "factory failed to connect!"
        print "reason: %s" % reason.getErrorMessage()
        #print "traceback: %s" % reason.getTraceback()
        reason.printTraceback()
    def clientConnectionLost(self, connector, reason):
        print "factory lost a connection"
        print "reason: %s" % reason.getErrorMessage()
        reason.printTraceback()
    def getLine(self, _):
        d = threads.deferToThread(getInput)
        return d

class Game(object):
    def __init__(self):
        self.factory = GameFactory()
        print "game initialized"
    def connect(self, host, port):
        #from twisted.internet import reactor
        reactor.connectTCP(host, port, self.factory)

class GameServerProtocol(NetstringReceiver):
    def mySendString(self, line):
        print "sending message: %s" % line
        self.sendString(line)
    def stringReceived(self, line):
        print "message received: %s" % line
        self.num_lines_received += 1
        if (self.num_lines_received > 5):
            self.mySendString("quit")
        else:
            self.mySendString(line + "~")
    def connectionMade(self):
        print "protocol connection made."
        self.num_lines_received = 0
        self.mySendString("y hello thar")
        # this server is very annoyng...
        self.loop = task.LoopingCall(self.mySendString, ("bluh"))
        self.loop.start(10.0, now=False)
    def connectionLost(self, reason):
        self.loop.stop()
        print "protocol connection lost."
        print "reason: %s" % reason.getErrorMessage()
        reason.printTraceback()

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
        reactor.listenTCP(port, self.factory)

def main():
    print "starting up..."
    if len(sys.argv) < 2:
        print "incorrect usage."
        print "for a server: 'server [port]'"
        print "for a client: '[ip] [port]'"
        return
    if sys.argv[1] == 'server':
        print "i am a server"
        server = GameServer()
        port = int(sys.argv[2])
        print "starting server on port %i" % port
        server.listen(port)
    else:
        print "i am a client"
        game = Game()
        ip = sys.argv[1]
        port = int(sys.argv[2])
        print "connecting to %s port %i" % (ip, port)
        game.connect(ip, port)
    reactor.run()

if __name__ == "__main__":
    main()

