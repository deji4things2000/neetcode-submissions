class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        ind = [0] * numCourses

        for a,b in prerequisites:
            adj[b].append(a)
            ind[a] +=1

        q = deque()

        for courses in range(numCourses):
            if ind[courses] == 0:
                q.append(courses)

        taken = 0

        while q:
            curr = q.popleft()
            taken+=1

            for nei in adj[curr]:
                ind[nei]-=1
                if ind[nei] == 0:
                    q.append(nei)

        return taken == numCourses




