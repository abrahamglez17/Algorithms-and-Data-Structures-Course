case1 = [3,0,1]
case2 = [0,1]
case3 = [9,6,4,2,3,5,7,0,1]



def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums) #n! = n * (n + 1) // 2

# note: we use the formula for the sum of the first n natural numbers
# Time complexity: O(n)
# Space complexity: O(1)

print(missingNumber(case1))
print(missingNumber(case2))
print(missingNumber(case3))