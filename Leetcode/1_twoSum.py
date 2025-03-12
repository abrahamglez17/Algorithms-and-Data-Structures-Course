class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)): # n1
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i, j]

case1 = [2,7,11,15]
target1 = 9        
case2 = [3,2,4]
target2 = 6
case3 = [3,3]
target3 = target2

s = Solution()

print(s.twoSum(case1, target1))
print(s.twoSum(case2, target2))
print(s.twoSum(case3, target3))
        
# Time complexity: O(n^2)
# Space complexity: O(1)
# NOTES:
# n1: using two loops to iterate through the list

class Solution2:
    def twoSum(self, nums, target):
        solDict = {}
        for i in range(len(nums)):
            complement = target - nums[i] # n1
            if complement in solDict:
                return [solDict[complement], i] # n3
            solDict[nums[i]] = i # n2

s2 = Solution2()
print("SECOND SOLUTION USING HASHTABLES")
print(s2.twoSum(case1, target1))
print(s2.twoSum(case2, target2))
print(s2.twoSum(case3, target3))

# Time complexity: O(n)
# Space complexity: O(n)
# NOTES:
# n1: we are looking for the complement of the current number in the dictionary
# n2: we are storing the number and its index in the dictionary
# n3: if the complement is in the dictionary, we return the index 
# of the complement and the current index