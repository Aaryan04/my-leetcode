class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt = 1
        grps = []

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                grps.append(cnt)
                cnt = 1
            
        grps.append(cnt)

        ans = 0
        
        for i in range(len(grps)-1):
            ans += min(grps[i], grps[i+1])
        
        return ans





                        