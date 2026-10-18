class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        s = []

        for c in p:
            if c=='' or c=='.':
                continue
            elif c=='..':
                if s:
                    s.pop()
            else:
                s.append(c)
        newpath = '/' + '/'.join(s)
        return newpath
        