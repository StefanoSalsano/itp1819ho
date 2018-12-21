#!/usr/bin/python

import os
import shutil
from mininet.topo import Topo
from mininet.node import Host
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

BASEDIR = "/home/user/mytests/ospfbase/nodeconf/"
PRIVDIR = '/var/priv'

class BaseNode(Host):

    def __init__(self, name, *args, **kwargs):
        dirs = [PRIVDIR]
        Host.__init__(self, name, privateDirs=dirs, *args, **kwargs)
        self.dir = "/tmp/%s" % name
        self.nets = []
        if not os.path.exists(self.dir):
            os.makedirs(self.dir) 

    def config(self, **kwargs):
        # Init steps
        Host.config(self, **kwargs)
        # Iterate over the interfaces
        first = True
        for intf in self.intfs.itervalues():
            # Remove any configured address
            self.cmd('ifconfig %s 0' %intf.name)
            # # For the first one, let's configure the mgmt address
            # if first:
            #   first = False
            #   self.cmd('ip a a %s dev %s' %(kwargs['mgmtip'], intf.name))
        #let's write the hostname in /var/mininet/hostname
        self.cmd("echo '" + self.name + "' > "+PRIVDIR+"/hostname")
        if os.path.isfile(BASEDIR+self.name+"/start.sh") :
            self.cmd('source %s' %BASEDIR+self.name+"/start.sh")

    def cleanup(self):
        Host.cleanup(self)
        # Rm dir
        if os.path.exists(self.dir):
            shutil.rmtree(self.dir)

        if os.path.exists(BASEDIR+self.name+"/zebra.pid"):
            os.remove(BASEDIR+self.name+"/zebra.pid")

        if os.path.exists(BASEDIR+self.name+"/zebra.log"):
            os.remove(BASEDIR+self.name+"/zebra.log")

        if os.path.exists(BASEDIR+self.name+"/zebra.sock"):
            os.remove(BASEDIR+self.name+"/zebra.sock")

        if os.path.exists(BASEDIR+self.name+"/ospfd.pid"):
            os.remove(BASEDIR+self.name+"/ospfd.pid")

        if os.path.exists(BASEDIR+self.name+"/ospfd.log"):
            os.remove(BASEDIR+self.name+"/ospfd.log")




class Router(BaseNode):
    def __init__(self, name, *args, **kwargs):
        BaseNode.__init__(self, name, *args, **kwargs)

class RoutersTopo(Topo):
    def build(self):
        h1 = self.addHost(name='h1', cls=BaseNode)
        h2 = self.addHost(name='h2', cls=BaseNode)
        r1 = self.addHost(name='r1', cls=Router)
        r2 = self.addHost(name='r2', cls=Router)
        # self.addLink( 'h1', 'r1')
        # self.addLink( 'r1', 'r2')
        # self.addLink( 'r2', 'h2')
        self.addLink( h1, r1)
        self.addLink( r1, r2)
        self.addLink( r2, h2)


def stopAll():
    # Clean Mininet emulation environment
    os.system('sudo mn -c')
    # Kill all the started daemons
    os.system('sudo killall sshd zebra ospfd')

    
def simpleTest():
    "Create and test a simple network"

    topo = RoutersTopo()
    net = Mininet(topo=topo, build=False, controller=None)
    net.build()
    net.start()


    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    #print "Testing network connectivity"
    #net.pingAll()

    CLI( net ) 
    net.stop() 
    stopAll()



if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()