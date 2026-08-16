class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if '0000' in deadends:
            return -1

        if target == '0000':
            return 0

        q = deque([('0000', 0)])
        visited = set(['0000'])

        while q:
            cur, move = q.popleft()

            for i in range(4):
                for direction in [1, -1]:
                    new_digit = (int(cur[i]) + direction) % 10
                    new_state = cur[:i] + str(new_digit) + cur[i+1:]

                    if new_state == target:
                        return move+1
                    
                    if new_state not in deadends and new_state not in visited:
                        visited.add(new_state)
                        q.append((new_state, move+1))

        return -1