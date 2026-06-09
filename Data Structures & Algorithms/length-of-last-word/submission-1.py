class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.rstrip()
        n=len(a)
        cnt = 0

        for i in range(n-1, -1, -1):
            if a[i]!=" ":
                cnt+=1
            else:
                break
        return cnt



        return s


        
        