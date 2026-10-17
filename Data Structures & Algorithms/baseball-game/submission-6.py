class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops =operations
        n = len(ops)

        for i in range(n):
            if ops[i] == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            elif ops[i] == "C":
                stack.pop()
            elif ops[i] == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(ops[i]))
        
        suma = 0
        for i in range(len(stack)):
            suma+=stack[i]
        return suma


        