class MyQueue:

    def __init__(self):
        self.inp_s = []
        self.out_s = []

    def push(self, x: int) -> None:
        self.inp_s.append(x)

    def pop(self) -> int:
        if not self.out_s:
            while self.inp_s:
                x = self.inp_s.pop()
                self.out_s.append(x)
            
        return self.out_s.pop()

    def peek(self) -> int:
        if not self.out_s:
            while self.inp_s:
                x = self.inp_s.pop()
                self.out_s.append(x)
            
        return self.out_s[-1]
        
    def empty(self) -> bool:
        if not self.out_s and not self.inp_s:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()