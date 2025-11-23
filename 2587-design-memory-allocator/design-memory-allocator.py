class Allocator:

    def __init__(self, n: int):
        self.memory = [-1] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i in range(self.n):
            if self.memory[i] == -1:
                cnt += 1

                # we have found a block big enough to fill up this block with mID
                if cnt == size:
                    start_idx = i - size + 1
                    for j in range(start_idx, i+1):
                        self.memory[j] = mID
                    return start_idx
            
            # we found non empty space so cnt = 0
            else:
                cnt = 0 
        # if no start_idx is found
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