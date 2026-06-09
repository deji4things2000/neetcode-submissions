class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l, r = 0, 0
        n = len(word)
        s = word
        a = abbr

        while l < n and r < len(a):
            if s[l] == a[r]:
                l += 1
                r += 1
            elif a[r].isdigit():
                res = self.cd(a, r)

                # FIX: don't allow empty or leading zeros
                if res == "" or res[0] == "0":
                    return False

                l += int(res)
                r += len(res)
            else:
                return False
        
        # FIX: ensure both fully consumed
        return l == n and r == len(a)
    
    def cd(self, a, r):
        res = ""
        # FIX: stop when digits stop
        while r < len(a) and a[r].isdigit():
            res += a[r]
            r += 1
        return res

