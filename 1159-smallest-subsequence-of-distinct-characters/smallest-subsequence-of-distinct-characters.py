class Solution:
    def smallestSubsequence(self, s: str) -> str:

        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        ans = []
        used = set()

        for i in range(len(s)):
            ch = s[i]

            if ch in used:
                continue

            while ans and ans[-1] > ch and last[ans[-1]] > i:
                used.remove(ans.pop())

            ans.append(ch)
            used.add(ch)

        return "".join(ans)