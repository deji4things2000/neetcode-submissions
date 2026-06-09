class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''

        for val in zip(*strs):
            if len(set(val)) == 1:
                s+=val[0]
            else:
                break
        return s



