case1 = [1,2,3,1]
case2 = [1,2,3,4]
case3 = [1,1,1,3,3,4,3,2,4,2]
case4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def containsDuplicate(nums):
    if(len(nums) == len(set(nums))):
        return False
    else:
        return True

    # Time complexity: O(n)

    # Space complexity: O(n)

print(containsDuplicate(case1))
print(containsDuplicate(case2))
print(containsDuplicate(case3))
print(containsDuplicate(case4))