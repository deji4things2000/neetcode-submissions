class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''

        entries = self.store[key]
        
        i, j = 0, len(entries)-1
        result = ''

        while i<=j:

            mid = (i+j)//2

            time, val = entries[mid]

            if time <= timestamp:
                i = mid + 1
                result = val
            else:
                j = mid - 1

        return result
        
        
