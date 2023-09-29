from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = collections.defaultdict(list)
        for x in strs:
            sorted_word = "".join(sorted(x))
            dict1[sorted_word].append(x)

        return dict1.values()


x = Solution()
print(x.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
