def kmp_pattern(pattern : str) -> list:
    len_pattern = len(pattern)
    table = [0] * len_pattern
    j = 0
    for i in range(1, len_pattern):
        while j > 0 and pattern[j] != pattern[i]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    
    return table


def kmp(word : str, pattern : str) -> None:
    table = kmp_pattern(pattern)
    
    result = []
    j = 0
    
    for i in range(len(word)):
        while j > 0 and word[i] != pattern[j]:
            j = table[i - 1]
        
        if word[i] == pattern[j]:
            if j == len(pattern) - 1:
                result.append(i - len(pattern) + 1)
                j = table[j]
            else:
                j += 1

    return print('패턴이 일치하지 않습니다') if len(result) == 0 else print(f'{result[0]}번 문자부터 일치합니다.')

if __name__ == "__main__":
    kmp('abcdefabgedefg', 'bged')
    print(kmp_pattern('abcdeabeabde'))