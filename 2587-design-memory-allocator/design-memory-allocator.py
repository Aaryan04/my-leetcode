class Allocator:

    def __init__(self, n: int):
        self.memory = [-1] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i in range(self.n):
            if self.memory[i] == -1:
                cnt += 1

                # we have found a block big enough
                if cnt == size:
                    start_idx = i - size + 1

                    for j in range(start_idx, i + 1):
                        self.memory[j] = mID
                    
                    return start_idx
                
            else:
                # recent cnt if curr slot is occupied
                cnt = 0
        return -1



    def freeMemory(self, mID: int) -> int:
        cnt = 0
        for i in range(self.n):
            if self.memory[i] == mID:
                self.memory[i] = -1
                cnt += 1
        return cnt
            



# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)