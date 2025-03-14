class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0]=0 #base case
        for i in range(1, amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i] = min(dp[i], dp[i-j]+1)
        
        return dp[amount] if dp[amount]!= float('inf') else -1
    
# Time complexity: O(n*m) where n is the amount and m is the number of coins
# Space complexity: O(n) where n is the amount

s= Solution()

case1 = [1,2,5]
amount1 = 11
print(s.coinChange(case1, amount1)) #3

case2 = [2]
amount2 = 3
print(s.coinChange(case2, amount2)) #-1

case3 = [1]
amount3 = 0
print(s.coinChange(case3, amount3)) #0
