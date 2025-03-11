case1 = [4,3,2,7,8,2,3,1]
case2 = [1,1]

def findDisappearedNumbers(nums):
    set_nums = set(nums)
    
    missing = []
    for i in range(1, len(nums)+1): # n1
        if i not in set_nums:
            missing.append(i)
    return missing

# Time complexity: O(n)
# Space complexity: O(n)
# n1: +1 because range does not include the last element
print(findDisappearedNumbers(case1))
print(findDisappearedNumbers(case2))
