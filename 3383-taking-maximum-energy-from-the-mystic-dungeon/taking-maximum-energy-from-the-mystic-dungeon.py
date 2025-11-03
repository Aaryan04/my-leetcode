class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        ans = -math.inf

        for i in range(n-k, n):
            total = 0
            j = i
            while j >= 0:
                total += energy[j]
                j = j-k
                ans = max(ans, total)

        return ans
