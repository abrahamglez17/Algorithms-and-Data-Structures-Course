class Solution:
    def smallerNumbersThanCurrent(self, nums):
        solDict = {} # value: nums smaller
        sortNums = sorted(nums)
        for i,num in enumerate(sortNums):
            if num not in solDict:
                solDict[num]=i
        solution = []
        for num in nums:
            solution.append(solDict[num])
        return solution
            
        
case1= [8,1,2,2,3]
case2= [6,5,4,8]
case3= [7,7,7,7]
s= Solution()
print(case1)
print(s.smallerNumbersThanCurrent(case1))
print(case2)
print(s.smallerNumbersThanCurrent(case2))
print(case3)
print(s.smallerNumbersThanCurrent(case3))