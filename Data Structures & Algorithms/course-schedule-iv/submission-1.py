class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ind = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prereq, course in prerequisites:
            adj[prereq].append(course)
            ind[course] += 1
        
        q = deque()

        for course in range(numCourses):
            if ind[course] == 0:
                q.append(course)

        indirect = []
        for i in range(numCourses):
            indirect.append(set())

        while q:
            prereq = q.popleft()
            
            for course in adj[prereq]:
                indirect[course]|=indirect[prereq] #all courses are prereq each other
                indirect[course].add(prereq)
                ind[course] -= 1
                if ind[course] == 0:
                    q.append(course)
        
        ans = []
        for u,v in queries:
            ans.append(u in indirect[v])
        return ans



        