from countswaps import CountSwaps
#My chosen O(n(log(n))) sorting algorithm. 
def sort(A):

    #This algorithm is not stable, i think? See line 13 etc.
    def merge(A, list1, list2):
        tall1 = 0
        tall2 = 0

        while tall1 < len(list1) and tall2 < len(list2):
            
            if list1[tall1] <= list2[tall2]:
                A[tall1+tall2]= list1[tall1]
                #Se kommentar i 
                #A.incrementSwap()  
                tall1 +=1
            else:
                A[tall1+tall2]= list2[tall2]
                #A.incrementSwap()
                tall2 +=1
        while tall1 < len(list1):
            #### THIS IS WHERE THE PROBLEM OCCURED
            #A.swap(tall1+tall2, A.index(list1[tall1])) , used this to begin with, A.index() is O(n), 
            # so merge sort became O(log(n)*n^2), is this correct to say in O notation?
            A[tall1+tall2]= list1[tall1]
            #A.incrementSwap()
            tall1 +=1

        while tall2 < len(list2):
            A[tall1+tall2]= list2[tall2]
            #A.incrementSwap()
            tall2 +=1

        return A

    if len(A) <= 1:
        return A
    intMidt = int(len(A)/2)
    initialList1 = sort(CountSwaps(A[0:intMidt]))
    initialList2 = sort(CountSwaps(A[intMidt:len(A)]))
    return merge(A, initialList1, initialList2)
    
   