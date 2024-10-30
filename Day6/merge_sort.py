def _merge(L_left, L_right):
    L_res= []
    i, j = 0, 0
    len_left, len_right= len(L_left), len(L_right)
    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]:
            L_res.append(L_left[i])
            i+= 1                                     #left index count
        else:
            L_res.append(L_right[j])
            j += 1                                    #right index count
    while (i< len_left):                              #append remains after main merge
        L_res.append(L_left[i])
        i+= 1
    while (j < len_right):                            #append remains after main merge
        L_res.append(L_right[j])
        j += 1
    return L_res

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        L_left= mergeSort(L[:middle])
        L_right= mergeSort(L[middle:])
        return _merge(L_left, L_right)
    

L = [3, 2, 1, 0, 9, 4, 7, 5, 8, 6]
print("L = ", L)
sorted_L= mergeSort(L)
print("sorted_L= ", sorted_L)