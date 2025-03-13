class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False

case1 = [1,2,3,1]
case2 = [1,0,1,1]
case3 = [1,2,3,1,2,3]
k1 = 3
k2 = 1
k3 = 2
s = Solution()

print(case1)
print(s.containsNearbyDuplicate(case1, k1))
print(case2)
print(s.containsNearbyDuplicate(case2, k2))
print(case3)
print(s.containsNearbyDuplicate(case3, k3))
