class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ast = asteroids

        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and ast[i] < 0:
                if stack[-1] < abs(ast[i]):
                    stack.pop()
                    continue
                elif stack[-1] == abs(ast[i]):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(ast[i])
        return stack