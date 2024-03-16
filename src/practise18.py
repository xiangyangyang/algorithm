from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    if n < 2: return n
    dp = [1] * n
    max_n = 1
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                print(dp[i])

        max_n = max(max_n, dp[i])

    return max_n


if __name__ == '__main__':
    nums = [0,1,0,3,2,3]
    print(lengthOfLIS(nums))
