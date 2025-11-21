class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        uniq = set()

        for num in nums:
            if num in uniq:
                res.append(num)
            uniq.add(num)

        return list(res)