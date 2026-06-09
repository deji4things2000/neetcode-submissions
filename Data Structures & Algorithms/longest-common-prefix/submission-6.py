class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''

        for c in zip(*strs):
            if len(set(c)) == 1:
                s+=c[0]
            else:
                break
        return s