class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return '###Empty###'
        else:
            return '|||'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '###Empty###':
            return []
        else:
            return list(s.split('|||'))
