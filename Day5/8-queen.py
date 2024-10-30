# 8퀸 문제 알고리즘 구현

row = [0] * 8
col = [0] * 8
to_right = [0] * 150 
to_left = [0] * 15

def put() -> None:
    for i in range(8):
        print(f'{row[i]:2}', end='')
    print()


def set(i : int) -> None:
    for j in range(8):
        if col[j] != 1 and to_right[i-j+7] != 1 and to_left[i+j] != 1:
            row[i] = j
            if i == 7:
                put()
            else:
                col[j] = to_right[i-j+7] = to_left[i+j] = 1
                set(i + 1)
                col[j] = to_right[i-j+7] = to_left[i+j] = 0
set(0)