import random
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.pos = defaultdict(list)
        for i, num in enumerate(nums):
            self.pos[num].append(i)

    def pick(self, target: int) -> int:
        print(self.pos)
        return random.choice(self.pos[target])


if __name__ == "__main__":
    # s = Solution([1, 1, 2, 5, 7, 6, 4, 5, 6, 7])
    # print(s.pick(6))
    array = [1, 1, 2, 5, 7, 6, 4, 5, 6, 8]
    print(array[-1])
