class Solution:
    def confusingNumber(self, n: int) -> bool:
        hs = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        now=str(n)
        res=""
        fin=""


        for i in now:

            if i not in hs:
                return False

            if i in hs:
                res+=hs[i]
            else:
                res+=i
        
        for i in range(len(res)-1, -1, -1):
            fin+=res[i]

        if int(fin) == n:
            return False
        
        return True