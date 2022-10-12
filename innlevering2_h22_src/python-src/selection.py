#Selection sort sorting algorithm
#Takes in CountSwaps object
def sort(A):

    for i in range(len(A)):
        indeks = i

        for j in range(len(A[i:])):
            if A[j+i] < A[indeks]:
                indeks = j+i

        #Would practically speaking not need this if check, if not for 
        #count swaps function in the .csv file of the output     
        if i != indeks:
            A.swap(i,indeks)
    return A