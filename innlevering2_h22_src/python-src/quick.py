#Sorting algorithm sorting using quicksort
#Takes input of countswaps object holding countcompares. Not a list of ints.
def sort(A):
    
    def choosePivot(A, low, high) -> int:
        #given the inputfiles this will be a good selection method
        #for random, this willl giv a random number, for nearly sorted, most probably a number close to the true median number
        return int((high+low)/2)

    def partition(A, low, high):
        
        pivot = choosePivot(A,low,high) 
        A.swap(pivot,high)
        pivot = A[high]

        right_index = high-1
        left_index = low

        while right_index >= left_index:
            
            while right_index >= left_index and A[left_index] <= pivot:
                left_index +=1
            
            while right_index >= left_index and A[right_index] >= pivot:
                right_index -=1
            
            if left_index < right_index:
                A.swap(right_index, left_index)

        A.swap(high, left_index)
        return left_index

    def quicksort(A, low, high):
        if low >= high:
            return A
        p = partition(A,low,high)
        
        quicksort(A,low,p-1)
        quicksort(A, p+1, high)
        return A
    
    return quicksort(A, 0,len(A)-1)