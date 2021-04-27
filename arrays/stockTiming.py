class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        purchaseVal = prices[0]

        for x in prices:
            if x < purchaseVal:
                purchaseVal = x
            else:
                if x - purchaseVal > profit:
                    profit = x - purchaseVal

        return profit
