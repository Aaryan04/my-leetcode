class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        curSum = 0
        # prefixSum = {0: 1}      # prefixSum : cnt
        prefixSum = defaultdict(int)
        prefixSum[0] += 1

        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefixSum[diff]
            prefixSum[curSum] += 1
        
        return res