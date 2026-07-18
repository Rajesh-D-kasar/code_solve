class Solution:
    def findGCD(self, nums: List[int]) -> int:

        a = min(nums)
        b = max(nums)

        while b % a != 0:
            temp = b % a
            b = a
            a = temp

        return a