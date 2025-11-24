class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        n = len(s)
        l = 0
        maxLen = 0

        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen