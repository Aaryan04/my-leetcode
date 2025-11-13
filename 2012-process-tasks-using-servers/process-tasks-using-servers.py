class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # two min heaps, one for available servers, one for unavailable
        # available = (weight, index)
        # unavailable = (timeServerBecomesFree, weight, index)

        # res: An array to store the index of the server assigned to each task.
        res = [0] * len(tasks)

        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)
        unavailable = []
        
        # t: Represents the current time.
        t = 0
        
        # Iterate through each task by its index 'i', which is also its arrival time.
        for i in range(len(tasks)):
            # The current time 't' must be at least the task's arrival time 'i'.
            t = max(t, i)
            
            # If no servers are available, we must advance time.
            if len(available) == 0:
                # Jump time forward to the earliest moment a server becomes free.
                # unavailable[0][0] is the smallest 'timeServerBecomesFree' in the min-heap.
                t = unavailable[0][0]
                
            # Now, move all servers that have become free by the current time 't'
            # from the 'unavailable' heap back to the 'available' heap.
            while unavailable and t >= unavailable[0][0]:
                # Pop the server that's been free the longest (or earliest).
                timefree, weight, index = heapq.heappop(unavailable)
                # Add it back to the pool of available servers.
                heapq.heappush(available, (weight, index))
                
            # At this point, 'available' heap has the best server for the current time 't'.
            # Pop the best available server (lowest weight, then lowest index).
            weight, index = heapq.heappop(available)
            
            # Assign this server's index to the current task 'i'.
            res[i] = index
            
            # Add this server to the 'unavailable' heap.
            # It will become free at time 't' + task_duration.
            heapq.heappush(unavailable, (t + tasks[i], weight, index))
            
        # Return the final list of server assignments.
        return res