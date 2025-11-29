class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_op = 0
        
        for num in nums:
            if num % 3 != 0:
                num_op += 1
            
        return num_op