class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()         # nlogn
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                currSum = nums[i] + nums[l] + nums[r]

                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1      # try to find more results
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res

