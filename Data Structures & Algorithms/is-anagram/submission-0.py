
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for ch in s:
            if ch in map1:
                map1[ch] += 1
            else:
                map1[ch] = 0
        for ch in t:
            if ch in map2:
                map2[ch] += 1
            else:
                map2[ch] = 0
        




        return map1 == map2
        