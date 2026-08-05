class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 1): return 1
        hashSet = set()
        l = 0
        maxRes = 0
        for r in range(len(s)):
            while(s[r] in hashSet):
                hashSet.remove(s[l])
                l += 1
            
            hashSet.add(s[r])
            maxRes = max(maxRes, r - l + 1)
        return maxRes
