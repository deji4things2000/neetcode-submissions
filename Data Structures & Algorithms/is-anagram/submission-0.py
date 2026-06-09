class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl=list(s)
        sl.sort()
        tl=list(t)
        tl.sort()
        a=len(sl)
        if a == len(tl):
            i=0
        else:
            return False
        while i<len(sl):
            if sl[i]==tl[i]:
                i+=1
            else:
                return False
        return True
            



        