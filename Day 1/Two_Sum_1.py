from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            sums = nums[left_pointer] + nums[right_pointer]
            print(sums)
            if sums > target:
                right_pointer -= 1
            elif target > sums:
                left_pointer += 1
            else:
                return [left_pointer, right_pointer]


x = Solution()
print(x.twoSum([3, 2, 4], 6))
