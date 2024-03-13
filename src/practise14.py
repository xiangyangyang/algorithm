import re
def combine(n: int, k: int):
    def backtrack(start, path):
        if len(path) == k:
            result.append(path)
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(1, [])
    return result


def get_target_str(s, t):
    w = len(t)
    tm = '+'.join([x for x in t])
    while w < len(s):
        for i in range(len(s)):
            if re.match(tm, s[i:w+1]):
                return s[i:w+1]
        w += 1

    return ""


# 测试
if __name__ == '__main__':
    n = 6
    k = 3
    # print(combine(n, k))  # 输出 [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    s = "XDOYEZODEYXNZ"
    t = "XYZ"
    # print(get_target_str(s,t))

    print(re.search(r'X+(\w)+Y+(\w)+Z+(\w)+', 'XDOYEZODEYXNZ'))
