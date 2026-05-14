class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        # Outer loop: The day we buy
        for i in range(len(prices)):
            # Inner loop: The day we sell (must be after buying)
            for j in range(i + 1, len(prices)):
                # Calculate profit for this specific pair
                profit = prices[j] - prices[i]
                # Update our maximum result
                res = max(res, profit)
                
        return res