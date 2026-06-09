class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        ops = operations
        n=len(ops)

        for i in range(n):
            if ops[i] == '+':
                res.append(res[-1]+res[-2])
            elif ops[i] == 'C':
                res.pop()
            elif ops[i] == 'D':
                res.append(res[-1]*2)
            else:
                res.append(int(ops[i]))
        
        val = 0
        for num in res:
            val+=int(num)
        return val


        