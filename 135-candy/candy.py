class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_cnt = 0
        n = len(ratings)

        l2r = [1] * n
        r2l = [1] * n 

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                l2r[i] = l2r[i-1] + 1
            
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                r2l[i] = r2l[i+1] + 1
            
        for i in range(n):
            candy_cnt += max(l2r[i], r2l[i])

        return candy_cnt