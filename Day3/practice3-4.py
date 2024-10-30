#binary search

from typing import Any, Sequence

def binSearch(a : Sequence, key : Any) -> int:
    lt = 0; rt = len(a) - 1

    while True:
        center = (lt + rt) // 2
        if a[center] == key:
            return center
        elif a[center] < key:
            lt = center + 1
        else:
            rt = center - 1
        
        if lt > rt:
            break
    return -1

if __name__ == "__main__":
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    print('배열 데이터를 오름차순으로 입력하세요')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:
                break

    ky = int(input('검색할 값을 입력하세요.: '))

    idx = binSearch(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')

    else:
        print(f'검색값은 x[{idx}]에 있습니다.')

