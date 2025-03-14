class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1) 
        dp[0]=1 # reacheable in 1 way
        dp[1]=1 # reacheable in 1 way
        dp[2]=2 # reacheable in 2 ways
        
        # n ways to reach the nth step
        for i in range(3, n+1):
            dp[i]=dp[i-1] + dp[i-2] 
        return dp[n]
    
case1=2
case2=15
s= Solution()

print(case1)
print(s.climbStairs(case1))
print(case2)
print(s.climbStairs(case2))
