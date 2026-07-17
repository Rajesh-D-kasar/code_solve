from typing import List
from bisect import bisect_left


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        limit = max(nums)

        count = [0] * (limit + 1)

        for value in nums:
            count[value] += 1

        gcd_count = [0] * (limit + 1)

        # Exact GCD pair count find karna
        for current_gcd in range(limit, 0, -1):

            total_numbers = 0

            # Kitne numbers current_gcd se divide hote hain
            for value in range(current_gcd, limit + 1, current_gcd):
                total_numbers += count[value]

            # In numbers se possible pairs
            total_pairs = total_numbers * (total_numbers - 1) // 2

            # Bigger GCD wale pairs remove karenge
            multiple = current_gcd * 2

            while multiple <= limit:
                total_pairs -= gcd_count[multiple]
                multiple += current_gcd

            gcd_count[current_gcd] = total_pairs

        # Sorted gcdPairs ko directly banane ki jagah
        # cumulative pair count store karenge
        prefix = []

        running_pairs = 0

        for gcd_value in range(1, limit + 1):
            running_pairs += gcd_count[gcd_value]
            prefix.append(running_pairs)

        answer = []

        for query in queries:

            # query zero-based hai, isliye query + 1
            position = bisect_left(prefix, query + 1)

            # Prefix index 0 ka matlab GCD 1
            answer.append(position + 1)

        return answer