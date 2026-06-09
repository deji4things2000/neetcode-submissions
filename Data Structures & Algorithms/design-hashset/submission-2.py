class MyHashSet:

    def __init__(self):
        setsize = 1000000
        self.table = [False] * setsize
        
    def add(self, key: int) -> None:
        self.table[key] = True
        

    def remove(self, key: int) -> None:
        self.table[key] = False
        

    def contains(self, key: int) -> bool:
        return self.table[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)