class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0] * (numCourses)
        adj = [[] for _ in range(numCourses)]

        for courses, prereq in prerequisites:
            adj[prereq].append(courses)
            ind[courses]+=1

        q = deque()

        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)

        taken = 0

        while q:
            prereq = q.popleft()
            taken+=1

            for courses in adj[prereq]:
                ind[courses] -=1
                if ind[courses] == 0:
                    q.append(courses)
        return taken == numCourses

    


        
        

        