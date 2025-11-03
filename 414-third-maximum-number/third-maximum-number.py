class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        unique = list(nums)
        unique.sort()
        print(unique)
        return unique[-3] if len(unique) >= 3 else unique[-1]
        
        # exist = set()
        # k = 3
        # max_heap = [-num for num in nums]
        # heapq.heapify(max_heap)

        # while k > 0:
        #     val = -(heapq.heappop(max_heap))


