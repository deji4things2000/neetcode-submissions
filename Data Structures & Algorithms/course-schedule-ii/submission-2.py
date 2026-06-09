class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        ind = [0] * numCourses

        for a,b in prerequisites:
            adj[b].append(a)
            ind[a]+=1

        q = deque()

        for courses in range(numCourses):
            if ind[courses] == 0:
                q.append(courses)

        res = []


        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in adj[curr]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)

        return res if len(res) == numCourses else []




        