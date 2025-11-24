class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use priority queue - maxHeap
        count = Counter(tasks)      # counts distinct tasks
        maxHeap = [-cnt for cnt in count.values()]      # negative to create maxHeap
        heapq.heapify(maxHeap)      


        time = 0
        # to maintain time when to add back the cnt to the maxHeap
        q = deque()     # pairs of [-cnt, idleTime]

        # if anything exists in the maxHeap and q
        while maxHeap or q:
            time += 1       # keep on incrementing time each loop 

            # if maxheap exists then pop and +1 and if cnt != 0 append to q with time to add back 
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time + n])       # 
            
            # if q is non empty and q[0][1] == time, push it back to the maxheap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        # return the final time i.e the minimum num of CPU intervals req to complete all tasks
        return time