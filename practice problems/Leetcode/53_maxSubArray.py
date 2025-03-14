class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0]*len(nums)
        dp[0]=nums[0]
        for i in range(1, len(nums)):
            dp[i]=max(dp[i-1]+nums[i], nums[i])
        return max(dp)
    
class Solution2:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = float("-inf")
        currSum = maxSum
        
        for i in nums:
            currSum = max(i, currSum + i)
            maxSum = max(maxSum, currSum)
        return maxSum