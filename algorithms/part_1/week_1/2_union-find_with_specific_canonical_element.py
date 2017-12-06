from dynamic_connectivity import WeighterQU

"""
 Union-find with specific canonical element. 
 Add a method find() to the union-find data type so that find(i) returns the largest element in the connected component containing i. 
 The operations, union(), connected(), and find() should all take logarithmic time or better.

For example, if one of the connected components is {1,2,6,9}, 
then the find() method should return 9 for each of the four elements in the connected components.
"""

class WeighterQUWithMax(WeighterQU):
    def __init__(self, N):
        self._max = [x for x in range(N)]
        super(WeighterQUWithMax, self).__init__(N)
        
    def find(self, p):
        p_id = self._root(p)
        return self._max[p_id]
        
    def union(self, p, q):
        """
        link root of smaller tree to root of larger tree. Update sz[]
        """
        p_id = self._root(p)
        q_id = self._root(q)
        if (p_id == q_id):
            return;
        if (self._sz[p_id] < self._sz[q_id]):
            self._id[p_id] = q_id
            self._sz[q_id] += self._sz[p_id]
            self._max[q_id] = max(self._max[q_id], self._max[p_id])
        else:
            self._id[q_id] = p_id
            self._sz[p_id] += self._sz[q_id]    
            self._max[p_id] = max(self._max[q_id], self._max[p_id])
            
    def __str__(self):
        return "ind: {}\r\nval: {}\r\nmax: {}".format(" ".join(str(x) for x in range(len(self._id))), 
                     " ".join(str(x) for x in self._id), 
                     " ".join(str(x) for x in self._max))
      
"""
Test
"""
str_N = input("Prompt N: ")
if str_N:
    N = int(str_N)
    uf = WeighterQUWithMax(N)
    
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
            
        print("max p:", uf.find(p))
        print("max q:", uf.find(q))