class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        mstack = []

        for c in s:
            if c == '':
                continue
            elif c == '..':
                if mstack:
                    mstack.pop()
            elif c == '.':
                continue
            else:
                mstack.append(c)
        newpath = '/' + '/'.join(mstack)
        return newpath
            
        