class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        s = ''

        for z in zip(*strs):
            if len(set(z)) == 1:
                s+=z[0]
            else:
                break
        return s
