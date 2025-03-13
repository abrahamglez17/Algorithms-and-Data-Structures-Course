class Solution():
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right =0, len(nums)-1
        result=[0]* len(nums)
        insertIdx=len(nums)-1
        
        while left<=right:
            if(abs(nums[left])>abs(nums[right])):
                result[insertIdx]=nums[left]**2
                left +=1
            else:
                result[insertIdx]=nums[right]**2
                right -=1
            insertIdx-=1
        return result
    
    # time complexity: O(n)
    # space complexity: O(n)

class MySolution: # my first solution (not optimal)
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        
        nums= sorted(nums)
        return nums
    # time complexity: O(nlogn)
    # space complexity: O(n)

case1= [-4,-1,0,3,10]
case2= [-7,-3,2,3,11]
s= MySolution()

# print(case1)
# print(s.sortedSquares(case1))
# print(case2)
# print(s.sortedSquares(case2))

s2= Solution()
print("BETTER SOLUTION")
print(case1)
print(s2.sortedSquares(case1))
print(case2)
print(s2.sortedSquares(case2))