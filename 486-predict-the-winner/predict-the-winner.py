class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
            
        n = len(nums)
        dp = nums[:]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                take_left = nums[i] - dp[i + 1]
                take_right = nums[j] - dp[i]
                dp[i] = max(take_left, take_right)
                
        return dp[0] >= 0