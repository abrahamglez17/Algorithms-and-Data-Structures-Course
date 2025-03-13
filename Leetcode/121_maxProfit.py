class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy, sell = 0, 1
        mProfit=0
        
        while sell < len(prices):
            if(prices[buy]<prices[sell]): #if there is profit
                mProfit= max(mProfit, prices[sell]-prices[buy])
            else:
                buy=sell
            sell+=1
            
        return mProfit


case1= [7,1,5,3,6,4]
case2= [7,6,4,3,1]
s= Solution()

print(case1)
print(s.maxProfit(case1))
print(case2)
print(s.maxProfit(case2))