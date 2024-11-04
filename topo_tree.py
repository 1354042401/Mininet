
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
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)

    info('*** Add hosts\n')
    h1 = net.addHost('h1',ip = '10.0.0.1')
    h2 = net.addHost('h2',ip = '10.0.0.2')
    h3 = net.addHost('h3',ip = '10.0.0.3')
    h4 = net.addHost('h4',ip = '10.0.0.4')

    info('*** Add links\n')
    net.addLink(s2, s1)
    net.addLink(s3, s1)
    net.addLink(h1, s2)
    net.addLink(h2, s2)
    net.addLink(h3, s3)
    net.addLink(h4, s3)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    controller.start()
    
    info('*** Starting switches\n')
    for switch in [s1,s2,s3]:
        switch.start([controller])  # Pass the controller to the switch

    CLI(net)

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()



