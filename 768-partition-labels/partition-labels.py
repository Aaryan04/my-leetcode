class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = dict()
        res = []
        n = len(s)

        for i in range(n):
            last[s[i]] = i
        
        # print(last)
        start, end = 0, 0
    
        for i in range(n):
            end = max(end, last[s[i]])
            if i == end:
                res.append(end-start+1)
                start = i + 1
        return res
