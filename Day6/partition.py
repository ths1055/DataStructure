from typing import MutableSequence

def partition(a : MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n - 1
    x = a[n // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr += 1
    
    print(f'피벗: {x}')

    print('피벗 이하')
    print(*a[0:pl])
    
    if pl > pr + 1:
        print('피벗과 일치')
        print(*a[pr + 1 : pl])

    print('피벗 이상')
    print(*a[pr + 1 : n])

if __name__ == "__main__":
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)