import random

def heap_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i, 0, -1):
            if j % 2 == 0:
                parents = (j - 2) // 2
            else:
                parents = (j - 1) // 2
            
            if arr[j] > arr[parents]:
                arr[j], arr[parents] = arr[parents], arr[j]
            else:
                pass
            print(i, j, arr)
        arr[0], arr[i] = arr[i], arr[0]

    return arr


array=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(array)


print(array)

arr = heap_sort(array)

print(arr)