# framework goes here?
# we really shouldn't be udp focused...?

import sys

from twisted.internet import defer
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.protocols.basic import NetstringReceiver
#from twisted.internet.protocol import DatagramProtocol

class GameProtocol(DatagramProtocol):
    strings = ["ohai", "halloes", "hello and goodbye"]
    def __init__(self, reactor, port):
        self.reactor = reactor
        self.port = int(port)
    def addIP(self, ip):
        print 'adding %s %s' % (ip, self.port)
        self.transport.connect(ip, self.port)
    def doStuff(self, _):
        self.sendDatagram()
    #def startProtocol(self):
    #    pass
        #self.transport.connect(self.ip, self.port)
        #self.sendDatagram()
    def sendDatagram(self):
        if len(self.strings):
            datagram = self.strings.pop(0)
            print "sending datagram... " + repr(datagram)
            self.transport.write(datagram)
    def datagramReceived(self, datagram, (host, port)):
        print ("Datagram received from %s %s: %s"
                % (host, port, repr(datagram)))
        self.sendDatagram()

class ServerProtocol(DatagramProtocol):
    def __init__(self, self.port)...
    def datagramReceived(self, datagram, address):
        new_msg = datagram + '~'
        self.transport.write(new_msg, address)

class GameFactory(ClientFactory):
    protocol = GameProtocol
    def __init__(self, deferred):
        self.deferred = deferred
        print "game factory initialized"
    def endCommunication(self):
        if self.deferred is not None:
            d, self.deferred = self.deferred, None
            d.callback(0)

class Game():
    def __init__(self, name):
        self.factory = GameFactory(name)
        print "game initialized"
    def connect(self, host, port):
        from twisted.internet import reactor
        reactor.connectTCP(host, port, self.factory)
        reactor.run()

def main():
    from twisted.internet import reactor
    if sys.argv[1] == 'server':
    	protocol = ServerProtocol()
    	reactor.listenUDP(int(sys.argv[2]), protocol)
    else:
    	#d = defer.Deferred()
    	protocol = GameProtocol(reactor, int(sys.argv[2]))
    	d = reactor.resolve(sys.argv[1])
    	d.addCallback(protocol.addIP)
    	d.addCallback(protocol.doStuff)
        t = reactor.listenUDP(0, protocol)
    reactor.run()

def main2():
    if len(sys.argv) == 4:
    	print 'I am a client'
        name = sys.argv[1]
        ip = sys.argv[2]
        port = int(sys.argv[3])
        lost = Game(name)
        lost.connect(ip, port)
    elif len(sys.argv) == 2:
        print 'I am a server'
        bork = Server()
        port = int(sys.argv[1])
        # ???
    else:
    	print "wrong number of args"
        print "client: [name] [ip] [port]"
        print "server: [port]"

if __name__ == "__main__":
    main()

