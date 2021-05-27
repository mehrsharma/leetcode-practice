class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        finalArray = []
        numZeros = 0

        product = 1

        for x in range (0, len(nums)):
            if nums[x] == 0:
                numZeros += 1
            else:
                product *= nums[x]

        if numZeros >= 2:
            product = 0

        for x in range (0, len(nums)):
            if nums[x] != 0 and numZeros == 0:
                finalArray.append(product/nums[x])
            if nums[x] != 0 and numZeros != 0:
                finalArray.append (0)
            if nums[x] == 0:
                finalArray.append(product)

        return finalArray
