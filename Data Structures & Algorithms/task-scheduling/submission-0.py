class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}
        heap = []
        for t in tasks:
            hm[t] = hm.get(t, 0) + 1

        for v in hm.values():
            heapq.heappush(heap, -v)
        
        time = 0
        while heap:
            temp = []
            cycle_count = 0

            for _ in range(n+1):
                if heap:
                    count = -heapq.heappop(heap)
                    if count > 1:
                        temp.append(count-1)
                    cycle_count+=1

            for count in temp:
                heapq.heappush(heap, -count)

            time += cycle_count if not heap else n+1

        return time
        