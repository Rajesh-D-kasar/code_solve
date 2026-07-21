class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        totalOnes = 0
        zeroBlocks = []

        i = 0
        n = len(s)

        while i < n:

            j = i

            while j < n and s[j] == s[i]:
                j += 1

            length = j - i

            if s[i] == '1':
                totalOnes += length
            else:
                zeroBlocks.append(length)

            i = j

        bestGain = 0

        for i in range(1, len(zeroBlocks)):
            bestGain = max(bestGain, zeroBlocks[i - 1] + zeroBlocks[i])

        return totalOnes + bestGain