class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = dict()
        index = 0;
        for x in nums:
            if ((target-x) in pairs):
                return [pairs[target-x], index]
            else:
                pairs[x] = index
            index += 1
