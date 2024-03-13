from mininet.topo import Topo

class BinaryTree(Topo):
    def __init__(self):
        Topo.__init__(self)
        hosts = [self.addHost(f'h{i}') for i in range(1, 9)]
        switches = [self.addSwitch(f's{i}') for i in range(1, 8)]
        link_pairs = [
            (hosts[0], switches[2]), (hosts[1], switches[2]),
            (hosts[2], switches[3]), (hosts[3], switches[3]),
            (hosts[4], switches[5]), (hosts[5], switches[5]),
            (hosts[6], switches[6]), (hosts[7], switches[6]),
            (switches[2], switches[1]), (switches[3], switches[1]),
            (switches[5], switches[4]), (switches[6], switches[4]),
            (switches[1], switches[0]), (switches[4], switches[0])
        ]
        for link in link_pairs:
            self.addLink(*link)
            
topos = {'binary_tree': (lambda: BinaryTree())}