from dynamic_connectivity import WeighterQU
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm
    
class Percolation:
    def __init__(self, n): 
        self._n = n
        # n*n - virtual top, n*n+1 - virtual bottom 
        self._qu = WeighterQU(n*n+2) 
        self._opened_matrix = np.full((n,n),0)
        """ 
        create n-by-n grid, with all sites blocked
        """
             
    def open(self, row, col):    
        """ 
        open site (row, col) if it is not open already
        """
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

def process_test_file(path):
    file = open(path, 'r') 
    lines = file.readlines() 
    N =  int(lines[0])
    perc = Percolation(N)
    is_percolates = False
    for i in range(1, len(lines)):
        splited_line = lines[i].replace('\n','').split(sep=" ")
        digits = [int(s) for s in splited_line if s.isdigit()]
        if (len(digits) == 2):
            perc.open(digits[0]-1,digits[1]-1)
            if (perc.percolates()):
                is_percolates = True
    filename, file_extension = os.path.splitext(path)
    result_image_path = filename+'_perc_'+is_percolates.__str__()+'.png'
    plt.imsave(result_image_path, perc._opened_matrix)        
        
if (__name__ == "__main__"):
    test_file = []
    for file in os.listdir("percolation-testing"):
        if file.endswith(".txt"):
            current_file = os.path.join("percolation-testing", file)
            process_test_file(current_file)