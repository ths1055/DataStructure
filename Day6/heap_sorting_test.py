import random,time,sys
sys.path.append('C:/')
import MyList

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

def heapSort(array):
    n = len(array)
    
    # 루트노드는 index 1부터 시작하므로, 앞에 0 원소를 추가한 채로 시작.
    array = [0] + array
    
    # 최종 정렬된 원소들이 저장될 배열
    ans = []

    # Min Heap을 만드는 과정
    for i in range(n//2, 0, -1):
        heapify(array, i, n)

    # 루트 노드 원소를 정렬 배열에 저장, heapify 반복
    for i in range(n, 0, -1):
        ans.append(array[1])
        array[i], array[1] = array[1], array[i]
        heapify(array, 1, i-1)
    
    # array[1:]를 얻으면 오름차순 정렬 배열을 얻을 수 있음
    return ans


size=int(input('\nsize of list (0 to terminate)='))

L=[]
MyList.genRandList(L,size)
print('List(size : {}) before merge sorting :'.format(size))
MyList.printListSample(L,10,2)
t1=time.time()
res=heap_sort(L)
t2=time.time()
print('\nList (size : {}) after selection sorting'.format(size))
MyList.printListSample(res,10,2)
print('Selection sorting for list of {} integers took {} sec'.format(size,t2-t1))


t1=time.time()
res=heapSort(L)
t2=time.time()
print('\nList (size : {}) after selection sorting'.format(size))
MyList.printListSample(res,10,2)
print('Selection sorting for list of {} integers took {} sec'.format(size,t2-t1))