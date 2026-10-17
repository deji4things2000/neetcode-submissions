class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        ast =  asteroids
        n = len(ast)

        for i in range(n):
            while s and s[-1] > 0 and ast[i] < 0:
                if s[-1] < abs(ast[i]):
                    s.pop()
                    continue
                elif s[-1] == abs(ast[i]):
                    s.pop()
                    break
                else:
                    break
            else:
                s.append(ast[i])
        return s

        