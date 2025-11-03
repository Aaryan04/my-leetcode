class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums = set(nums)
        # unique = list(nums)
        # unique.sort()
        # print(unique)
        # return unique[-3] if len(unique) >= 3 else unique[-1]
        
        # if len(nums) < 3:
        #     return max(nums)
        
        distinct = set(nums)
        if len(distinct) < 3:
            return max(distinct)

        # maintain a minheap of len 3
        min_heap = []
        for num in distinct:
            heapq.heappush(min_heap, num)
            if len(min_heap) > 3:
                heapq.heappop(min_heap)

        return min_heap[0]

            