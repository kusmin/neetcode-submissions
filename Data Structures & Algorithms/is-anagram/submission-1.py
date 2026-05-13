from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lis_s = dict(Counter(s))
        lis_t = dict(Counter(t))

        return lis_s == lis_t