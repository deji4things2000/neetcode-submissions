class StockSpanner:

    def __init__(self):
        self.mstack = []
        
    def next(self, price: int) -> int:
        span = 1

        while self.mstack and self.mstack[-1][0] <= price:
            span+=self.mstack.pop()[1]

        self.mstack.append((price, span))

        return span
        


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)