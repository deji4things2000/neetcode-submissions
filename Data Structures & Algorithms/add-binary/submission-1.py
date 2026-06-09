class Solution:
    #XOR, AND with n-1, and bit shifting
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2)

        while num_b:
            carry = (num_a & num_b) << 1
            num_a = num_a ^ num_b
            num_b = carry

        return bin(num_a)[2:]
        
