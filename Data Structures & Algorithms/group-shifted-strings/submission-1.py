class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hd = defaultdict(list)

        for s in strings:
            sig = tuple((ord(s[i]) - ord(s[i-1])) % 26 for i in range(1, len(s)))
            hd[sig].append(s)
        return list(hd.values())