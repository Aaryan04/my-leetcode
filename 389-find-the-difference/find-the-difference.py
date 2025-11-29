class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt_s = Counter(s)
        cnt_t = Counter(t)

        for char, cnt in cnt_t.items():
            if char not in cnt_s or cnt != cnt_s[char]:
                return char
            

