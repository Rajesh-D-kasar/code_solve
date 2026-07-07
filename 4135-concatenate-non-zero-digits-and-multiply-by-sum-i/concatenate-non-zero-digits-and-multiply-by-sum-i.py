class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        s = 0

        for ch in str(n):
            if ch != '0':
                digit = int(ch)
                x = x * 10 + digit
                s += digit

        return x * s