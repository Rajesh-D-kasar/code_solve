from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        arr = sorted(freq.values(), reverse=True)

        ans = 0
        for i, value in enumerate(arr):
            ans += (i // 8 + 1) * value

        return ans