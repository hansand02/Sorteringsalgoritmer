#Bubble sort sorting algorithm

def sort(A):

    for i in range(len(A)):
        #-i used since last element after inside for loop is always larger than all left of it
        #last element can therefore be "popped"
        #-1 since we access next element with j+1, and dont want index error
        for j in range(len(A)-i-1):
            if A[j+1] < A[j]:
                A.swap(j,j+1)
    return A