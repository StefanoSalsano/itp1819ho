#!/usr/bin/python                                                                            
                                                                                             
from mininet.topo import Topo
from mininet.node import Host
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)
def simpleTest():
    "Create and test a simple network"
    #topo = SingleSwitchTopo(n=4)
    #net = Mininet(topo)
    #net.start()
    net = Mininet(ipBase='10.100.5.9/8')   
    #h1 = Host( 'h1' )
    h1 = net.addHost( 'h1' )
    #h2 = Host( 'h2' )
    h2 = net.addHost( 'h2' ) 
    #h3 = Host( 'h3' )
    h3 = net.addHost( 'h3' ) 
    #s1 = net.addSwitch( 's1' )
    #c0 = net.addController( 'c0' )
    net.addLink( h1, h2 )
    net.addLink( h2, h3 )

    net.start()
    #print h1.cmd( 'ping -c1', h2.IP() )

    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    #print "Testing network connectivity"
    #net.pingAll()

    CLI( net ) 
    net.stop() 




if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()