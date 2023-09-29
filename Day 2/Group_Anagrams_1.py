from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs):
        anagram_map = collections.defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())


x = Solution()
print(x.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
