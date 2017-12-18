from dynamic_connectivity import QuickUnionUF
import numpy as np

    
class Percolation:
    def __init__(self, n): 
        self._n = n
        # n*n - virtual top, n*n+1 - virtual bottom 
        self._qu = QuickUnionUF(n*n+2) 
        for i in range(0, n):
            self._qu.union(n*n, i)
        for i in range(n*(n-1), n):
            self._qu.union(n*n+1, i)
        self._opened_matrix = np.full((n,n),0)
        """ 
        create n-by-n grid, with all sites blocked
        """
             
    def open(self, row, col):    
        """ 
        open site (row, col) if it is not open already
        """
        if (not self.isOpen(row,col)):
            self._opened_matrix[row, col]=1
            curr_pos = row*self._n+col
            #left
            if (col > 0):                
                if (self.isOpen(row, col-1)):
                    left_pos = row*self._n+col-1
                    self._qu.union(curr_pos, left_pos)
            #right
            if (col < self._n-1): 
                if (self.isOpen(row, col+1)):
                    right_pos = row*self._n+col+1
                    self._qu.union(curr_pos, right_pos)
            #top            
            if (row == 0):
                top_pos = self._n*self._n     
                self._qu.union(curr_pos, top_pos)
            elif (self.isOpen(row-1, col)):
                top_pos = (row-1)*self._n+col    
                self._qu.union(curr_pos, top_pos)                
            #bottom           
            if (row == self._n-1):
                bottom_pos = self._n*self._n+1    
                self._qu.union(curr_pos, bottom_pos)
            elif (self.isOpen(row+1, col)):
                bottom_pos = (row+1)*self._n+col    
                self._qu.union(curr_pos, bottom_pos)
       
    def isOpen(self, row, col):  
        """ 
        is site (row, col) open?
        return bool
        """
        return self._opened_matrix[row, col] == 1
       
    def isFull(self, row, col):  
        """ 
        is site (row, col) full?
        return bool
        """
   
    def numberOfOpenSites(self):       
        """ 
        number of open sites
        return int
        """
       
    def percolates(self):
        """
        does the system percolate?
        return bool
        """
        return self._qu.connected(self._n*self._n, self._n*self._n+1)


if (__name__ == "__main__"):
    N = 2
    perc = Percolation(N)
    input_coords = [(0,0),(1,1),(0,1)]
    for i in range(len(input_coords)):
        perc.open(input_coords[i][0],input_coords[i][1])
        if (perc.percolates):
            print('percolate!')