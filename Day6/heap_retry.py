import random

def heapify(li, idx, n):
    # li : 힙으로 만들고자 하는 배열
    # idx : 선택된 노드
    # n : 힙의 범위
    
    # 자식의 왼쪽 노드를 의미
    left = idx * 2
    # 자식의 오른쪽 노드를 의미
    right = idx * 2 + 1
    s_idx = idx

    # 선택 노드, 선택 노드의 양 자식 중 가장 작은 값을 찾는 과정
    if left <= n and li[s_idx] > li[left]:
        s_idx = left
    if right <= n and li[s_idx] > li[right]:
        s_idx = right
        
    # 선택 노드와 자식 노드의 위치가 바뀌어야 한다면
    if s_idx != idx:
        # 부모 자식 위치 변경
        li[idx], li[s_idx] = li[s_idx], li[idx]
        # 부모가 자식으로 내려간 이후에도, 그 자식과 바뀔 여지가 있는지 재귀로 체크
        return heapify(li, s_idx, n)
    
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
        arr[0], arr[i] = arr[i], arr[0]

    return arr

array=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(array)

for i in range(len(array)//2, 0, -1):
    heapify(array, i, len(array)//2)


res = heap_sort(array)

print(res)

'''
Conclusion
Notion Day6 참고
'''