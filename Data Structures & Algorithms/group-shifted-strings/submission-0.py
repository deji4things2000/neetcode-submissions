class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strings:
            sig = tuple((ord(s[i]) - ord(s[i-1])) % 26 for i in range(1, len(s)))
            res[sig].append(s)
        
        return list(res.values())