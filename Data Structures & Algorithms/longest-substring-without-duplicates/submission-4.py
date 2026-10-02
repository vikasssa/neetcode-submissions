class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen = {}
        # left = 0
        # maxLen = 0
        # for right in range(len(s)):
        #     if s[right] in seen:
        #         left = max(left, seen[s[right]] + 1)
            
        #     seen[s[right]] = right
        #     maxLen = max(maxLen, right - left + 1)
        # return maxLen


        seen = set()
        left = 0
        maxLen = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen
        