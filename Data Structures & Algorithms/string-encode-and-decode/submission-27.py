class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '#EMPTY#'
        else:
            return '|||'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '#EMPTY#':
            return []
        else:
            return list(s.split('|||'))
