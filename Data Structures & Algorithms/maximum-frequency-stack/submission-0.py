class FreqStack:

    def __init__(self):
        self.hm = defaultdict(int)
        self.hm2 = defaultdict(list)
        self.maxi = 0
        
    def push(self, val: int) -> None:
        self.hm[val] += 1
        f = self.hm[val]

        self.maxi = max(self.maxi, f)

        self.hm2[f].append(val)

    def pop(self) -> int:

        val = self.hm2[self.maxi].pop()

        self.hm[val] -=1

        if not self.hm2[self.maxi]:
            self.maxi-=1
        
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()