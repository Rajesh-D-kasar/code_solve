from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        count = [[0] * n for _ in range(n)]

        score[n - 1][n - 1] = 0
        count[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or (i == n - 1 and j == n - 1):
                    continue

                best = -1
                ways = 0

                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if ni < n and nj < n and score[ni][nj] != -1:
                        if score[ni][nj] > best:
                            best = score[ni][nj]
                            ways = count[ni][nj]
                        elif score[ni][nj] == best:
                            ways = (ways + count[ni][nj]) % MOD

                if best == -1:
                    continue

                add = 0 if board[i][j] == 'E' else int(board[i][j])
                score[i][j] = best + add
                count[i][j] = ways

        if count[0][0] == 0:
            return [0, 0]

        return [score[0][0], count[0][0] % MOD]