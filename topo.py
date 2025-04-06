from mininet.topo import Topo 
from mininet.net import Mininet 
from mininet.node import RemoteController 
from mininet.cli import CLI 
from mininet.link import TCLink 
 
class SimpleTopo(Topo): 
  def build(self): 
    h1 = self.addHost('h1', ip='10.0.0.1/24', mac='00:00:00:00:00:01') 
    h2 = self.addHost('h2', ip='10.0.0.2/24', mac='00:00:00:00:00:02') 
    h3 = self.addHost('h3', ip='10.0.0.3/24', mac='00:00:00:00:00:03') 
    s1 = self.addSwitch('s1') 
    self.addLink(h1, s1) 
    self.addLink(h2, s1) 
    self.addLink(h3, s1) 
 
if __name__ == '__main__': 
  topo = SimpleTopo() 
  net = Mininet(topo=topo, controller=None, link=TCLink, autoSetMacs=True) 
  net.start() 
  CLI(net) 
  net.stop() 
