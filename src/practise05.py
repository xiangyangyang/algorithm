from collections import Counter


def delete_least_frequent_chars(s):
    if not s:
        return s

    # 统计每个字符的出现次数
    char_count = Counter(s)
    print(char_count)

    # 找出出现次数最少的字符
    min_count = min(char_count.values())
    print(min_count)

    # 删除出现次数最少的字符
    result = ''.join(char for char in s if char_count[char] != min_count)

    return result


def del_least_char(input):
    char_count = {}
    for char in input:
        val = (char_count[char] + 1) if char in char_count.keys() else 1
        char_count[char] = val

    min_count = min(char_count.values())
    result = ''.join(char for char in input if char_count[char] != min_count)
    return result


if __name__ == "__main__":
    # 示例用法
    s = "abaccadeef"
    sorted(s,reverse=False)
    # result = delete_least_frequent_chars(s)
    result = del_least_char(s)
    print(result)  # 输出 "bccdd"，删除了出现次数最少的字符 'a' 和 'e'
