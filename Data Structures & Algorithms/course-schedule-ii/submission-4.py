class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for courses, prereq in prerequisites:
            adj[prereq].append(courses)
            ind[courses] +=1
        
        q = deque()
        for course in range(numCourses):
            if ind[course] == 0:
                q.append(course)

        res = []
        while q:
            prereq = q.popleft()
            res.append(prereq)

            for next_course in adj[prereq]:
                ind[next_course]-=1
                if ind[next_course] == 0:
                    q.append(next_course)
        return res if len(res) == numCourses else []
