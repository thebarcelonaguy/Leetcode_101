from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)

        return False


x = Solution()
print(x.containsDuplicate([2, 4, 18, 22, 22]))
