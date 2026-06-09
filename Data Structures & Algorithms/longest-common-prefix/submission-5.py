class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        for c in zip(*strs):
            if len(set(c)) == 1:
                res+=c[0]
            else:
                break
        return res


