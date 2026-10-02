class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        m = len(word1)
        n = len(word2)
        i, j = 0, 0
        flag = 0
        while i < m and j < n:
            if flag%2 == 0:
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
            flag += 1
        
        while i < m:
            ans.append(word1[i])
            i += 1
        
        while j < n:
            ans.append(word2[j])
            j += 1
        return "".join(ans)