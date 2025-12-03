class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # thought process thinking of creating a hash table {y: num of x coordinates at this y}
        mod = 10**9 + 7
        point_num = defaultdict(int)

        ans, total_sum = 0, 0 

        # creating hashmap
        for point in points:
            point_num[point[1]] += 1

        for p_num in point_num.values():
            edge = p_num * (p_num - 1) // 2
            ans = (ans + edge * total_sum) % mod
            total_sum = (total_sum + edge) % mod
        
        return ans