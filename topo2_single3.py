
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, Host, OVSController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():
    net = Mininet(controller=OVSController, topo=None, build=False)
    info('*** Adding controller\n')
    
    # Create and start the controller
    controller = net.addController('c0')
    
    info('*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info('*** Add hosts\n')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')

    info('*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, h1)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    controller.start()
    
    info('*** Starting switches\n')
    s1.start([controller])  # Pass the controller to the switch

    CLI(net)

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()



