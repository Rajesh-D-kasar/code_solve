class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        rows = len(grid)
        cols = len(grid[0])

        nums = []

        # Store all elements in one list
        for i in range(rows):
            for j in range(cols):
                nums.append(grid[i][j])

        size = len(nums)
        k = k % size

        # Shift elements
        if k != 0:
            nums = nums[size - k:] + nums[:size - k]

        result = []
        pos = 0

        # Make 2D grid again
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(nums[pos])
                pos += 1
            result.append(row)
            
        return result