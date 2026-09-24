class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        i = 0

        while i < len(base):
            for s in strs[1:]:
                if i >= len(s) or base[i] != s[i]: # check invalid state
                    return base[:i]
            i += 1
        
        return base