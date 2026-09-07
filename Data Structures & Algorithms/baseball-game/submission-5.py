class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        nums = operations
        n = len(nums)

        for i in range(n):
            if nums[i] == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            elif nums[i] == 'C':
                stack.pop()
            elif nums[i] == 'D':
                a = stack[-1]
                stack.append(a*2)
            else:
                a = int(nums[i])
                stack.append(a)

        val = 0
        for i in range(len(stack)):
            val+=stack[i]
        return val

