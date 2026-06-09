class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)

        for s in strs:
            sig = tuple(sorted(s))
            dd[sig].append(s)
        return list(dd.values())