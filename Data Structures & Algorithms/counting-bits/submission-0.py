from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        def cnt(n):
            res = ''
            if n == 0:
                return 0
            while n>0:
                res = str(n&1) + res
                n>>=1

            hm = {}

            for i in range(len(res)):
                hm[res[i]] = hm.get(res[i],0) + 1

            for k,v in hm.items():
                if k == '1':
                    return v
        
        out = []
        for i in range(n+1):
            ct = cnt(i)
            out.append(ct)
        return out



