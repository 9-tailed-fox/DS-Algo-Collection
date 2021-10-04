def linearSearch(A,key):
    position = 0
    flag = False
    while position < len(A) and not flag:
        if A[position] == key:
            flag = True
        else:
            postiion = position + 1
    return flag


A = [56,32,78,87,98]
found = linearSearch(A,32)
print('Element 32 is present: ' , found)
