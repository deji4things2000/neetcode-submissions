class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        cur = ''

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append((cur, num))
                cur = ''
                num = 0
            elif c == ']':
                prev_str, repeat = stack.pop()
                cur = prev_str + cur * repeat
            else:
                cur += c
        return cur
        