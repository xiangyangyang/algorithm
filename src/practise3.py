

def count_unique_chars(s : str) -> int:
    unique_chars = set()
    for char in s:
        # 只统计 ASCII 码范围内的字符
        if 0 <= ord(char) <= 127 and char != '\n':
            unique_chars.add(char)
    return len(unique_chars)


if __name__ == "__main__":
    # 示例用法
    s = input()
    print(s.__class__)
    print(count_unique_chars(s))  # 输出 7，因为 "hello wrd" 有 7 个不同的字符
