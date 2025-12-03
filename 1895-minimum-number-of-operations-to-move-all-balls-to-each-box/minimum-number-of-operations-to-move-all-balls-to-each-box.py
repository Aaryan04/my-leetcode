class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # O(n^2) solution
        # n = len(boxes)
        # one_idx = set([i for i in range(n) if boxes[i] == '1'])

        # ans = []
        # for i in range(n):
        #     cnt = 0
        #     for idx in one_idx:
        #         cnt += abs(idx - i)
        #     ans.append(cnt)
        # return ans

        n = len(boxes)
        ans = [0] * n
        cnt = 0
        ops = 0
        for i in range(n):
            ans[i] += ops
            if boxes[i] == '1':
                cnt += 1
            ops += cnt

        cnt = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            ans[i] += ops
            if boxes[i] == '1':
                cnt += 1
            ops += cnt

        return ans