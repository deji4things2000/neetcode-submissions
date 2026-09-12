class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed = []

        for i in range(n):
            indexed.append((tasks[i][0], tasks[i][1], i))
        indexed.sort(key=lambda a:a[0])

        res = []
        heap = []
        time = 0
        i = 0

        while i<n or heap:
            if not heap:
                time = max(time, indexed[i][0])

            while i<n and indexed[i][0] <=time:
                enqueue, processing, idx = indexed[i]
                heapq.heappush(heap, (processing, idx))
                i+=1
            
            processing, idx = heapq.heappop(heap)
            res.append(idx)
            time+=processing
        return res

