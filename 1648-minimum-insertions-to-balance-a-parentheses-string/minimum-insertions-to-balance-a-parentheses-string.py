
class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        left = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                left += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    ans += 1

                if left == 0:
                    ans += 1
                else:
                    left -= 1

            i += 1

        ans += left * 2
        return ans