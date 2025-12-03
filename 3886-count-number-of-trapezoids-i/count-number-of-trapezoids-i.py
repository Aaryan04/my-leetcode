class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Map y-coordinate -> count of points at that height
        points_by_y = defaultdict(int)
        for x, y in points:
            points_by_y[y] += 1
            
        total_trapezoids = 0
        existing_segments = 0 # Accumulates all valid horizontal edges found so far
        
        for count in points_by_y.values():
            # Calculate nC2: Number of horizontal segments possible at this specific Y level
            current_segments = count * (count - 1) // 2
            
            # Every new segment can pair with EVERY existing edges to form a trapezoid
            total_trapezoids = (total_trapezoids + current_segments * existing_segments) % MOD
            
            # Add the segments from this row to the pool for the next rows to use
            existing_segments = (existing_segments + current_segments) % MOD
            
        return total_trapezoids