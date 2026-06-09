class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        ops = float('inf')

        for i in range(n - k + 1):  # only windows of length k
            cnt = 0
            j = i
            while j < i + k:  # count 'W's in this window
                if blocks[j] == 'W':
                    cnt += 1
                j += 1
            ops = min(ops, cnt)

        return ops

                
            
            
            
