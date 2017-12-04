
class UF:    
    def __init__(self, N):
        """
        Initialize union-find data structure with N objects (0 to N - 1)
        """
        pass
    
    def union(self, p, q):
        """
        add connection between p and q
        """
        pass
    
    def connected(self, p, q):
        """
        are p and q in the same component?
        return: bool
        """
        pass
    
    def find(self, p):
        """
        component identifier for p(0 to N - 1)
        return int
        """
        pass
    
    def count(self):
        """
        number of components
        """
        pass


class QuickFindUF(UF):
    """
    Quadratic time union. Bad at big N.
    INITIALIZE  | UNION | FIND
    N           | N     | 1
    """    
    def __init__(self, N):
        self._id = [x for x in range(N)]
        
    def connected(self, p, q):
        return self._id[p] == self._id[q]
    
    def union(self, p, q):
        p_id = self._id[p];
        q_id = self._id[q];
        for i in range(len(self._id)):
            if (self._id[i] == p_id):
                self._id[i] = q_id
                
    def __str__(self):
        return "{}\r\n{}".format(" ".join(str(x) for x in range(N)), " ".join(str(x) for x in self._id))


class QuickUnionUF(UF):
    """
    Quadratic time union. Bad at big N.
    INITIALIZE  | UNION | FIND
    N           | N     | N
    Union icludes cost of finding roots
    Find in worst case
    """    
    def __init__(self, N):
        self._id = [x for x in range(N)]
        
    def _root(self, ind):
        """
        chase parent pointers until reach root
        """
        while (ind != self._id[ind]):
            ind = self._id[ind]
        return ind
    
    def connected(self, p, q):
        """
        check if p and q have same root
        """
        return self._root(p) == self._root(q)
    
    def union(self, p, q):
        """
        change root of p to point to root of q
        """
        p_id = self._root(p)
        q_id = self._root(q)
        self._id[p_id] = q_id 
        
    def __str__(self):
        return "{}\r\n{}".format(" ".join(str(x) for x in range(N)), " ".join(str(x) for x in self._id))
                
    
"""
Test
"""
str_N = input("Prompt N: ")
if str_N:
    N = int(str_N)
    uf = QuickUnionUF(N)
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
        
        if (not uf.connected(p, q)):
            uf.union(p, q);
            print (uf)
        else:
            print('{} and {} already connected'.format(p, q))