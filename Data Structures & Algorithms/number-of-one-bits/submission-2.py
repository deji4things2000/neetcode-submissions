class Solution:
    def hammingWeight(self, n: int) -> int:
        res = ''

        while n>0:
            res = str(n&1) + res
            n>>=1
        
        hm = {}
        for i in range(len(res)):
            hm[res[i]] = hm.get(res[i], 0) + 1

        for k,v in hm.items():
            if k == '1':
                return v
        return 0