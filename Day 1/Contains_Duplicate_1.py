from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for x in nums:
            if x not in hash_map:
                hash_map[x] = 1
            else:
                hash_map[x] += 1
        print(hash_map)
        for value in hash_map.values():
            if value > 1:
                return True

        return False


x = Solution()
print(x.containsDuplicate([2, 4, 18, 22, 22]))
