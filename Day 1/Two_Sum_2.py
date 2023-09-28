from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i, x in enumerate(nums):
            expected_diff = target - x
            if expected_diff in dict1:
                return [dict1[expected_diff], i]

            dict1[x] = i


x = Solution()
print(x.twoSum([3, 2, 4], 6))
