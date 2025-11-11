class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        n = len(arr)

        currSum = 0
        l = 0
        for r in range(n):
            currSum += arr[r]

            if r-l+1 == k:
                print(currSum)
                if currSum / k >= threshold:
                    cnt += 1
                currSum -= arr[l]
                l += 1
            
        return cnt


