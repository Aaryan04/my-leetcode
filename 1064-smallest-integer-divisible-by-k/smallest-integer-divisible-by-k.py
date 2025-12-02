class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem = 0
        for len_n in range(1, k+1):
            rem = (rem*10+1) % k
            if rem == 0:
                return len_n

        return -1