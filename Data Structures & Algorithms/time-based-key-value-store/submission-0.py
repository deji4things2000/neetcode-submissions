import bisect
class TimeMap:

    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = ([], [])
        self.store[key][0].append(timestamp)
        self.store[key][1].append(value)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''

        timestamps, values = self.store[key]
        idx = bisect.bisect_right(timestamps, timestamp) - 1

        return values[idx] if idx>=0 else ""

        
