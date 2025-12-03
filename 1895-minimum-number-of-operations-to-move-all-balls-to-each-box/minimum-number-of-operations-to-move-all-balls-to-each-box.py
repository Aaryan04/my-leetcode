class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        one_idx = set([i for i in range(n) if boxes[i] == '1'])
        print(one_idx)

        ans = []
        for i in range(n):
            cnt = 0
            for idx in one_idx:
                cnt += abs(idx - i)
            ans.append(cnt)
        return ans

