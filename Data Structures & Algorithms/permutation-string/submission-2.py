class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        curr = {}
        expected = Counter(s1)
        left = 0
        for right in range(len(s2)):
            curr[s2[right]] = curr.get(s2[right], 0) + 1
            while right - left + 1 > n:
                curr[s2[left]] -= 1
                if curr[s2[left]] == 0:
                    del curr[s2[left]]
                left += 1
            
            if curr == expected:
                return True
        return False
        