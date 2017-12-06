from dynamic_connectivity import QuickUnionUF

"""
Successor with delete. Given a set of n integers S={0,1,...,n−1} 
and a sequence of requests of the following form:

 Remove x from S
 Find the successor of x: the smallest y in S such that y≥x.

design a data type so that all operations (except construction) 
take logarithmic time or better in the worst case.
"""

class SuccessorWithDelete:
    def __init__(self, N):
        self._qu = QuickUnionUF(N)
        
    def remove(self, x):
        self._qu.union(x, x+1)
        
    def successor(self, x):
        return self._qu._root(x)
    
    
"""
Test
"""
N = 20
swd = SuccessorWithDelete(N)

print(swd.successor(10)) #10
swd.remove(11)
swd.remove(13)
swd.remove(12)
swd.remove(10)
swd.remove(9)
swd.remove(15)
print(swd.successor(8)) #8
print(swd.successor(9)) #14
print(swd.successor(10)) #14
    