def kmp1(S: str, T: str) -> int:
    sn = len(S)
    tn = len(T)
    if sn > tn: return 0

    parts = [T[i: i + sn] for i in range(0, tn - sn + 1)]
    return parts.count(S)

# 计算模板串S在文本串T中出现了多少次
# @param S string字符串 模板串
# @param T string字符串 文本串
# @return int整型
#
def kmp(S: str, T: str) -> int:
    sn = len(S)
    tn = len(T)
    if sn > tn: return 0
    count = 0
    j = 0
    nexts = build_nexts(S, sn)
    for i in range(0, tn):
        # 模式串移动以后还与坏字符不相等的话，还得再移次长子串个位数，直到T[i] == S[j]
        while j > 0 and T[i] != S[j]:
            j = nexts[j - 1] + 1
        if T[i] == S[j]:
            j += 1
        if j == sn:
            count += 1
            j = nexts[j - 1] + 1

    return count

def build_nexts(S: str, n: int):
    nexts = [-1] * n
    k = -1
    for i in range(1, n):
        while k != -1 and S[i] != S[k + 1]:
            # 求次长子串，就是求匹配后缀子串的最长子串，因为前一个S[i-1]不能变。
            # 又因为后缀子串与前缀子串一模一样，所以就是求前缀子串的最长匹配串
            k = nexts[k - 1]
        if S[i] == S[k + 1]:
            # k也要更新，比如aaaaaaa时
            k += 1
        nexts[i] = k

    return nexts

if __name__ == '__main__':
    print(kmp("abcba","abcbabcbabcbaa"))