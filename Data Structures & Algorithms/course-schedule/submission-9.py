class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            ind[course] +=1
        
        q = deque()

        for course in range(numCourses):
            if ind[course] == 0:
                q.append(course)

        taken = 0

        while q:
            prereq = q.popleft()
            taken += 1

            for course in adj[prereq]:
                ind[course] -=1
                if ind[course] == 0:
                    q.append(course)

        return True if taken == numCourses else False
