from dynamic_connectivity import WeighterQU, QuickUnionUF

"""
 Given a social network containing n members and a log file containing m timestamps at which times pairs of members formed friendships, 
 design an algorithm to determine the earliest time at which all members are connected 
 (i.e., every member is a friend of a friend of a friend ... of a friend). 
 Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. 
 The running time of your algorithm should be mlogn or better and use extra space proportional to n.
"""

class SocialNetworkConnectivity:
    def __init__(self, N):
        self._qu = WeighterQU(N)
        self._friendship_counter = N
        
    def add_friend(self, p, q):        
        if not self._qu.connected(p, q):
            self._friendship_counter -= 1
        self._qu.union(p, q)
        print (self._qu)
    
    def is_connected(self):
        return self._friendship_counter == 1
    
"""
Test
"""
str_N = input("Prompt N: ")
if str_N:
    N = int(str_N)
    sn = SocialNetworkConnectivity(N)
    M = 0    
    while(True):
        input_str = input("p: ")
        if not input_str:
            break
        else:
            p = int(input_str)
        input_str = input("q: ")
        if not input_str:
            break
        else:
            q = int(input_str)
        M += 1
        sn.add_friend(p, q)
        if (sn.is_connected()):
            print('totaly connected at M =', M)
