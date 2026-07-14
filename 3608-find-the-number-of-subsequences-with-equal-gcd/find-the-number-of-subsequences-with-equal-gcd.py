from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)

        # dp[g1][g2] = ways where
        # first subsequence has gcd g1
        # second subsequence has gcd g2
        dp = [[0] * (max_num + 1) for _ in range(max_num + 1)]
        dp[0][0] = 1

        for num in nums:
            new_dp = [row[:] for row in dp]

            for g1 in range(max_num + 1):
                for g2 in range(max_num + 1):
                    ways = dp[g1][g2]

                    if ways == 0:
                        continue

                    # Put num in first subsequence
                    new_g1 = gcd(g1, num)
                    new_dp[new_g1][g2] = (
                        new_dp[new_g1][g2] + ways
                    ) % MOD

                    # Put num in second subsequence
                    new_g2 = gcd(g2, num)
                    new_dp[g1][new_g2] = (
                        new_dp[g1][new_g2] + ways
                    ) % MOD

            dp = new_dp

        answer = 0

        # Same non-zero GCD means both subsequences are non-empty
        for g in range(1, max_num + 1):
            answer = (answer + dp[g][g]) % MOD

        return answer