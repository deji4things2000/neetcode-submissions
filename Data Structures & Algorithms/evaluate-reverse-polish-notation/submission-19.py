class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t = tokens
        s = []
        n = len(tokens)

        for i in range(n):
            if t[i] == "+":
                a = s.pop()
                b = s.pop()
                s.append(a+b)
            elif t[i] == "*":
                a = s.pop()
                b = s.pop()
                s.append(a*b)
            elif t[i] == "-":
                a = s.pop()
                b = s.pop()
                s.append(b-a)
            elif t[i] == "/":
                a = s.pop()
                b = s.pop()
                s.append(int(b/a))
            else:
                s.append(int(t[i]))
        return s[-1]




        