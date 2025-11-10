class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i, num1 in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                l, r = j+1, len(nums) - 1

                while l < r: 
                    currSum = nums[l] + nums[r]
                    if currSum < (target - nums[i] - nums[j]):
                        l += 1
                    elif currSum > (target - nums[i] - nums[j]):
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        # while l < r and nums[r] == nums[r+1]:
                        #     r -= 1

        return res




