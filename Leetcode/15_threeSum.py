class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        left, right, target = 0, 0, 0
        results = []

        for i in range(len(nums) - 2):
            if (i > 0 and nums[i] == nums[i-1]): #if num is duplicated skip index
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currSum = nums[left] + nums[right]
                if (currSum == target): #found triplet
                    results.append([nums[i], nums[left], nums[right]])
                    #if next value is duplicate we move index
                    while left < right and nums[left] == nums[left+1]: 
                        left +=1
                    while left < right and nums[right] == nums[right-1]: 
                        right -=1
                    
                    left +=1
                    right -=1
                
                elif(currSum<target): #if sum is less than target
                    left +=1 #need to increase the sum
                else: #if sum is greater than target
                    right -=1 #need to decrease the sum
        return results


case1 = [-1, 0, 1, 2, -1, -4]
case2 = [0, 1, 1]
case3 = [0, 0, 0]
s = Solution()

print(case1)
print(s.threeSum(case1))
print(case2)
print(s.threeSum(case2))
print(case3)
print(s.threeSum(case3))


