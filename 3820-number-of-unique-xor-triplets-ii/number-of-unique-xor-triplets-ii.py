from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        maximum_xor_value = 2048

        one_element_xor = [False] * maximum_xor_value
        two_element_xor = [False] * maximum_xor_value
        three_element_xor = [False] * maximum_xor_value

        for current_number in nums:

            new_three_element_xor = three_element_xor[:]
            for xor_value in range(maximum_xor_value):
                if two_element_xor[xor_value]:
                    new_three_element_xor[xor_value ^ current_number] = True

            new_two_element_xor = two_element_xor[:]
            for xor_value in range(maximum_xor_value):
                if one_element_xor[xor_value]:
                    new_two_element_xor[xor_value ^ current_number] = True

            one_element_xor[current_number] = True

            two_element_xor = new_two_element_xor
            three_element_xor = new_three_element_xor

            two_element_xor[current_number ^ current_number] = True
            three_element_xor[current_number] = True

        return sum(three_element_xor)