class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        index = 0
        if len(nums) == 1:
            return False

        for x in nums:
            if x == nums[index-1]:
                return True
            index += 1
        return False
