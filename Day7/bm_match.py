#영문 소문자 기준으로 작성 -- 범위 넓힐경우 table length만 넓혀주면 됨

def bm_pattern(pattern : str) -> list:
    len_pattern = len(pattern)
    table = [0] * 26
    for i in range(26):
        table[i] = len(pattern)
    
    for i, idx in enumerate(pattern):
        table[ord(idx) - 97] = len_pattern - i - 1
    
    return table

def bm(txt : str, pattern : str) -> None:
    table = bm_pattern(pattern)

    i = 0
    j = len(pattern) - 1
    while i <= len(txt):
        while pattern[j] == txt[i]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        i += table[ord(txt[i]) - 97]
        j = len(pattern) - 1
    return -1


if __name__ == "__main__":
    print(bm('abcdabeabd', 'abd') + 1)