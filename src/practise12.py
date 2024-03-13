def longest_common_substring(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    end_index = 0

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                if dp[i + 1][j + 1] > max_len:
                    max_len = dp[i + 1][j + 1]
                    end_index = i

    start_index = end_index - max_len + 1
    return a[start_index:end_index + 1]


# 读取输入
a = input().strip()
b = input().strip()

# 确保a是较短的字符串
if len(a) > len(b):
    a, b = b, a

# 输出最长公共子串
print(longest_common_substring(a, b))

if __name__ == '__main__':
    # 读取输入
    a = input().strip()
    b = input().strip()

    # 确保a是较短的字符串
    if len(a) > len(b):
        a, b = b, a

    # 输出最长公共子串
    print(longest_common_substring(a, b))

