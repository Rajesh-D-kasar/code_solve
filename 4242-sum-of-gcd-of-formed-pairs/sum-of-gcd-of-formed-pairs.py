from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_values = []
        gcd_values = []

        largest = nums[0]

        # Har position tak ka maximum store karna
        for number in nums:
            if number > largest:
                largest = number

            max_values.append(largest)

        # nums[i] aur max_values[i] ka GCD
        for i in range(len(nums)):
            result = gcd(nums[i], max_values[i])
            gcd_values.append(result)

        gcd_values.sort()

        total = 0
        last = len(gcd_values) - 1

        # Smallest aur largest ko pair karna
        for i in range(len(gcd_values) // 2):
            total += gcd(gcd_values[i], gcd_values[last - i])

        return total