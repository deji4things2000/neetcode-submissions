class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        n = len(strs)

        for i in range(n):
            sig = tuple(sorted(strs[i]))
            dd[sig].append(strs[i])
        return list(dd.values())