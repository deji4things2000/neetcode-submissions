class MinStack:

    def __init__(self):
        self.q = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.q.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
        

    def pop(self) -> None:
        self.q.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.q[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
