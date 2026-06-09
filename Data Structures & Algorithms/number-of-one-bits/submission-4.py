class Solution:
    def hammingWeight(self, n: int) -> int:
        
        def bc(n):
            b = ''
            while n>0:
                odd = n&1
                b=str(odd)+b
                n//=2
            return b
        
        bina = bc(n)
        
        hm = {}

        for i in range(len(bina)):
            hm[bina[i]] = hm.get(bina[i],0) + 1

        for k,v in hm.items():
            if k=='1':
                return v
        return 0