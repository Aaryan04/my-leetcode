class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.f_idx = 0
        self.cnt = 0 
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[(self.f_idx + self.cnt) % self.capacity] = value
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.f_idx = (self.f_idx + 1) % self.capacity
        self.cnt -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.f_idx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.f_idx + self.cnt - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()