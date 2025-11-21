class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s_list = list(s)
        Vowel = set('aeiouAEIOU')
        
        while l < r:
            if s_list[l] not in Vowel:
                l += 1
            elif s_list[r] not in Vowel:
                r -= 1
            else:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            
        return ''.join(s_list)
                
