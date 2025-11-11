class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        l = 0
        cnt = 0
        target = threshold * k
        curSum = 0

        for r in range(n):
            curSum += arr[r]

            if r-l+1 == k:
                if curSum >= target:
                    cnt +=1
                curSum -= arr[l]
                l += 1
        return cnt