class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        answer = []

        for length in range(2, 10):
            for start in range(10 - length):
                number = int(digits[start:start + length])

                if low <= number <= high:
                    answer.append(number)

        return answer