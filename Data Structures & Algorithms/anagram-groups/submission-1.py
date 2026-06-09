class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for n in strs:
            sl = ''.join(sorted(n))
            res[sl].append(n)
        return list(res.values())
