class CountSwaps(list):
    swaps = 0
    
    def swap(self, i, j):
        self.swaps += 1
        self[i], self[j] = self[j], self[i]
    
    #Had to make this method to do mergesort, without accessing swaps directly. 
    #Later removed method, since merge sort not really swaps any data
    #The data in a higher hierarcial list is refernced to as data in a lower list. And we do not get a full true swap. 
    """ def incrementSwap(self):
        self.swaps +=1 """