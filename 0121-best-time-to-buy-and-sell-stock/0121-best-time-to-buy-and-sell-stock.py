class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Array solution

#         solution = 0
#         diff = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[i] > prices[j]:
#                     continue
#                 else:
#                     diff = prices[j] - prices[i]
#                     if solution < diff:
#                         solution = diff
                        
#         return solution
    
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit
        