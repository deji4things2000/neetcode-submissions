class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = ""
        for c in zip(*strs):
            if len(set(c)) == 1:
                st +=c[0]
            else:
                break
        return st
