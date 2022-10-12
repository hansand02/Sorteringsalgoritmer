#Works exactly as intended now, sortingwise
def sort(A):
    for i in range(1, len(A)):
        tmp = i
        while tmp>0 and A[tmp] < A[tmp-1]:
            A.swap(tmp, tmp-1)
            tmp -=1
    return A
