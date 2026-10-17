class MinStack:

    def __init__(self):
        self.s = []
        self.mini = []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.mini or val<=self.mini[-1]:
            self.mini.append(val)
        
    def pop(self) -> None:
        if self.s[-1] == self.mini[-1]:
            self.mini.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mini[-1]
