class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        def gcd(a,b):
            while b > 0:
                a,b = b, a%b
            return a 

        g = functools.reduce(gcd, numsDivide)
        smallest = min([num for num in nums if g%num == 0], default = inf)

        return -1 if smallest == inf else sum(smallest > num for num in nums)