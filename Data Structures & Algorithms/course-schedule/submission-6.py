class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            ind[course]+=1

        q = deque()

        for course in range(numCourses):
            if ind[course] == 0:
                q.append(course)

        taken = 0

        while q:
            prereq = q.popleft()
            taken+=1

            for courses in adj[prereq]:
                ind[courses] -= 1
                if ind[courses] == 0:
                    q.append(courses)

        return taken == numCourses