from typing import List

# 超时
def candy(ratings: List[int]) -> int:
    n = len(ratings)
    carr = [1] * n
    i = 0
    while i < n - 1:
        if ratings[i] > ratings[i + 1]:
            if carr[i] <= carr[i + 1]:
                carr[i] = carr[i + 1] + 1
                i = 0
            else:
                i += 1
        elif ratings[i] < ratings[i + 1]:
            if carr[i] >= carr[i + 1]:
                carr[i + 1] = carr[i] + 1
            i += 1
        else:
            i += 1

    return sum(carr)

# 从左往右遍历一遍，再从右往左遍历一遍。关键是当前的修改不影响上一步的操作
def candy2(ratings: List[int]) -> int:
    n = len(ratings)
    carr = [1] * n
    for i in range(n-1):
        if ratings[i] < ratings[i + 1]:
            if carr[i] >= carr[i + 1]:
                carr[i + 1] = carr[i] + 1
    for j in range(n-1, 0, -1):
        if ratings[j] < ratings[j-1]:
            if carr[j] >= carr[j-1]:
                carr[j-1] = carr[j] + 1

    return sum(carr)


if __name__ == '__main__':
    # ratings = [1, 0, 2, 1, 0, 2, 3, 3, 2, 2, 1, 0]
    ratings = [1, 2, 2]
    # ratings = [1, 0, 2]
    print(candy2(ratings))
