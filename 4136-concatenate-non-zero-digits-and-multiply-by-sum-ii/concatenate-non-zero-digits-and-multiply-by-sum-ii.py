from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(s)

        nonzero_count = [0] * (n + 1)
        digit_sum = [0] * (n + 1)
        values = [0]

        for i, ch in enumerate(s):
            digit = int(ch)
            nonzero_count[i + 1] = nonzero_count[i]
            digit_sum[i + 1] = digit_sum[i] + digit

            if digit != 0:
                nonzero_count[i + 1] += 1
                values.append((values[-1] * 10 + digit) % MOD)

        max_nonzero = nonzero_count[n]
        power10 = [1] * (max_nonzero + 1)

        for i in range(1, max_nonzero + 1):
            power10[i] = (power10[i - 1] * 10) % MOD

        answer = []

        for left, right in queries:
            start = nonzero_count[left]
            end = nonzero_count[right + 1]
            length = end - start

            x = (values[end] - values[start] * power10[length]) % MOD
            total = digit_sum[right + 1] - digit_sum[left]

            answer.append((x * total) % MOD)

        return answer