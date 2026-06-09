class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = operations

        for i in range(len(ops)):
            if ops[i] == "+":
                stack.append((stack[-1]) + stack[-2])
            elif ops[i] == "D":
                stack.append(stack[-1]*2)
            elif ops[i] == "C":
                stack.pop()
            else:
                stack.append(int(ops[i]))
        val=0
        for i in stack:
            val+=int(i)
        return val