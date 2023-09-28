class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map1, hash_map2 = {}, {}
        for i in range(len(s)):
            hash_map1[s[i]] = 1 + hash_map1.get(s[i], 0)
            hash_map2[t[i]] = 1 + hash_map2.get(t[i], 0)

        for x in hash_map1:
            if hash_map1[x] != hash_map2.get(x, 0):
                return False

        return True


x = Solution()
print(x.isAnagram("riten", "eistn"))
