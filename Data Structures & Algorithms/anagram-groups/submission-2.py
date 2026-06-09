class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sig = ''.join(sorted(s))
            res[sig].append(s)
        return list(res.values())
