class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, totalCapacity):
        buses.sort()
        passengers.sort()
        
        i, j = 0, 0
        n, m = len(buses), len(passengers)
        
        while i < n:
            currentCapacity = 0
            while j < m and currentCapacity < totalCapacity and passengers[j] <= buses[i]:
                j += 1
                currentCapacity += 1
            
            # Last Bus
            if i == n - 1:
                j -= 1
                if currentCapacity < totalCapacity:     # if last bus has more seats for you
                    time = buses[i]
                    while j >= 0 and time == passengers[j]:
                        time -= 1
                        j -= 1
                    return time
                else:                                   # if the bus is full
                    time = passengers[j] - 1
                    j -= 1
                    while j >= 0 and time == passengers[j]:
                        time -= 1
                        j -= 1
                    return time
            
            i += 1
        
        return buses[-1]