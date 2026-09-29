class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dd = defaultdict(list)

        for c in strs:
            sig = tuple(sorted(c))
            dd[sig].append(c)
        return list(dd.values())