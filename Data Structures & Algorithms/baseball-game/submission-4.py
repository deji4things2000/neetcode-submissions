class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        n = len(operations)
        ops = operations

        for i in range(n):
            if ops[i] == '+':
                res.append(res[-1] + res[-2])
            elif ops[i] == 'D':
                res.append(res[-1] * 2)
            elif ops[i] == 'C':
                res.pop()
            else:
                res.append(int(ops[i]))
        
        val = 0
        for i in range(len(res)):
            val+=res[i]
        return val
        