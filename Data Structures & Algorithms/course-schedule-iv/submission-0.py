class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for i in range(numCourses)]
        ind = [0] * numCourses

        for prereq, courses in prerequisites:
            adj[prereq].append(courses)
            ind[courses] +=1

        queue = deque()

        for i in range(numCourses):
            if ind[i] == 0:
                queue.append(i)

        prereqs = []
        for i in range(numCourses):
            prereqs.append(set())


        while queue:
            course = queue.popleft()
            for nei in adj[course]:
                prereqs[nei] |= prereqs[course] #all prereqs of nei are prereq of courses
                prereqs[nei].add(course) #plus course itself

                ind[nei] -= 1
                if ind[nei] == 0:
                    queue.append(nei)
        
        ans = []

        for u, v in queries:
            ans.append(u in prereqs[v])
        return ans





