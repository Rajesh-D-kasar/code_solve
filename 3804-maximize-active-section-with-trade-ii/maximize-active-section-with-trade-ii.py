class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        total_ones = s.count('1')
        
        # Compress runs: typeArr (0 or 1), start, endIdx
        type_arr = []
        start = []
        end_idx = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            val = 1 if s[i] == '1' else 0
            type_arr.append(val)
            start.append(i)
            end_idx.append(j - 1)
            i = j
        
        N = len(type_arr)
        if N == 0:
            return [0] * len(queries)
        
        # posToSeg: index -> segment id
        pos_to_seg = [-1] * n
        for i in range(N):
            for j in range(start[i], end_idx[i] + 1):
                pos_to_seg[j] = i
        
        # Precompute gain for internal '1' segments
        ans = [0] * N
        for i in range(1, N - 1):
            if type_arr[i] == 1:
                left_len = end_idx[i-1] - start[i-1] + 1
                right_len = end_idx[i+1] - start[i+1] + 1
                ans[i] = left_len + right_len
        
        # Sparse Table
        if N <= 1:
            log_table = [0] * (N + 1)
        else:
            log_table = [0] * (N + 1)
            for i in range(2, N + 1):
                log_table[i] = log_table[i // 2] + 1
        
        K = log_table[N] + 1 if N > 0 else 1
        st = [[0] * N for _ in range(K)]
        for i in range(N):
            st[0][i] = ans[i]
        
        for j in range(1, K):
            for i in range(N - (1 << j) + 1):
                a = st[j-1][i]
                b = st[j-1][i + (1 << (j-1))]
                st[j][i] = max(a, b)
        
        def query_rmq(L: int, R: int) -> int:
            if L > R:
                return 0
            length = R - L + 1
            j = log_table[length]
            a = st[j][L]
            b = st[j][R - (1 << j) + 1]
            return max(a, b)
        
        def eval_func(i: int, L: int, R: int, segL: int, segR: int) -> int:
            if i <= segL or i >= segR or type_arr[i] == 0:
                return 0
            # left zero
            left_len = 0
            if i - 1 == segL:
                left_len = max(0, end_idx[i-1] - L + 1)
            else:
                left_len = end_idx[i-1] - start[i-1] + 1
            # right zero
            right_len = 0
            if i + 1 == segR:
                right_len = max(0, R - start[i+1] + 1)
            else:
                right_len = end_idx[i+1] - start[i+1] + 1
            return left_len + right_len
        
        res = []
        for L, R in queries:
            if L > R:
                res.append(total_ones)
                continue
            segL = pos_to_seg[L]
            segR = pos_to_seg[R]
            
            if segR - segL < 2:
                res.append(total_ones)
                continue
            
            max_gain = 0
            # Boundary
            max_gain = max(max_gain, eval_func(segL + 1, L, R, segL, segR))
            max_gain = max(max_gain, eval_func(segR - 1, L, R, segL, segR))
            # Internal
            if segL + 2 <= segR - 2:
                max_gain = max(max_gain, query_rmq(segL + 2, segR - 2))
            
            res.append(total_ones + max_gain)
        
        return res