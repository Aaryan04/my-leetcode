class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n - 1

        while l+1 < n and arr[l] <= arr[l+1] :
            l += 1

        if l == n - 1:
            return 0        # already sorted

        while r - 1 > -1 and arr[r-1] <= arr[r]:
            r -= 1

        ans = min(n - l - 1, r)         # remove one side completely
        i = 0
        j = r
        while i <= l and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j-i-1)
                i += 1
            else:
                j += 1
        return ans
        