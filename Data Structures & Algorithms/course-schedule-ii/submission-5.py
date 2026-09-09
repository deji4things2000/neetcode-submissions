class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            ind[course] += 1

        q = deque()

        for course in range(numCourses):
            if ind[course] == 0:
                q.append(course)

        res = []

        while q:
            prereq = q.popleft()
            res.append(prereq)
            for course in adj[prereq]:
                ind[course]-=1
                if ind[course] == 0:
                    q.append(course)
        
        return res if len(res) == numCourses else []

        