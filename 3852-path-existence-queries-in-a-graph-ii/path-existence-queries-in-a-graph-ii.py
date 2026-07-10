from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        arr = sorted((nums[i], i) for i in range(n))

        pos = [0] * n
        values = [0] * n

        for i, (val, idx) in enumerate(arr):
            values[i] = val
            pos[idx] = i

        comp = [0] * n
        for i in range(1, n):
            comp[i] = comp[i - 1]
            if values[i] - values[i - 1] > maxDiff:
                comp[i] += 1

        nxt = [0] * n
        r = 0

        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = 20
        up = [nxt]

        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            left = pos[u]
            right = pos[v]

            if left == right:
                ans.append(0)
                continue

            if left > right:
                left, right = right, left

            if comp[left] != comp[right]:
                ans.append(-1)
                continue

            cur = left
            dist = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < right:
                    cur = up[k][cur]
                    dist += 1 << k

            ans.append(dist + 1)

        return ans