class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        ind = [0] * numCourses

        for courses, prereq in prerequisites:
            adj[prereq].append(courses)
            ind[courses]+=1

            
        queue = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                queue.append(i)

        taken = 0

        while queue:
            courses = queue.popleft()
            taken+=1

            for course in adj[courses]:
                ind[course] -=1
                if ind[course] == 0:
                    queue.append(course)
            
        return True if taken == numCourses else False


        