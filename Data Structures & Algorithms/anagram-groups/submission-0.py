class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res=defaultdict(list)
        for c in strs:
            sl=''.join(sorted(c))
            res[sl].append(c)
        return list(res.values())