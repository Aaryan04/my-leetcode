class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []

        for i, (x,y) in enumerate(points):
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))

        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        return res