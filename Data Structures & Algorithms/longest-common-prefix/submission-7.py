class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''

        for st in zip(*strs):
            if len(set(st)) == 1:
                s+=st[0]
            else:
                break
        return s