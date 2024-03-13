from itertools import groupby


def longestBeautifulSubstring(word: str) -> int:
    n = len(word)
    left, right = 0, 0
    max_len = 0
    window = []

    while right < n:
        if len(window) == 0 or word[right] >= window[-1]:
            window.append(word[right])
            if window[-1] - window[0] == 21:
                max_len = max(max_len, right - left + 1)
        else:
            if word[right] < window[-1]:
                left = right
                window = [word[right]]
        right += 1

    return max_len

def longestBeautifulSubstring2(word: str) -> int:
    vowels = 'aeiou'
    n = len(word)
    last_positions = {'a': -1, 'e': -1, 'i': -1, 'o': -1, 'u': -1}
    max_len = 0
    count = 0

    for i in range(n):
        if word[i] in vowels:
            if i > 0 and word[i] < word[i-1]:
                count = 1
            else:
                count += 1
            last_positions[word[i]] = i
            if count == 5:
                max_len = max(max_len, i - min(last_positions.values()) + 1)
        else:
            count = 0

    return max_len


def longestBeautifulSubstring3(word: str) -> int:
    n = len(word)
    ret, length, vowels = 0, 1, 1

    for i in range(1, n):
        if word[i] > word[i - 1]:
            length += 1
            vowels += 1
        elif word[i] == word[i - 1]:
            length += 1
        else:
            length = 1
            vowels = 1
        if vowels == 5:
            ret = max(ret, length)
    return ret


if __name__ == '__main__':
    word1 = "aeiou"
    word2 = "uuuuu"
    word3 = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
    word4 = "aeiaaeioooouu"
    word5 = "aeiouaaaaeeeiiiaeiiooooo"
    word6 = "eauoiouieaaoueiuaieoeauoiaueoiaeoiuieuaoiaeouiaueo"
    print(longestBeautifulSubstring3(word1))
    print(longestBeautifulSubstring3(word2))
    print(longestBeautifulSubstring3(word3))
    print(longestBeautifulSubstring3(word4))
    print(longestBeautifulSubstring3(word5))
    print(longestBeautifulSubstring3(word6))
    print(groupby(word3))
