from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        if prices.index(min(prices)) < prices.index(max(prices)):
            return max(prices) - min(prices)
        
        
        buy = 0
        profit = 0

        while buy < len(prices):
            while (buy + 1) < len(prices) and prices[buy] >= prices[buy + 1]:
                buy += 1

            sell = buy + 1

            while sell < len(prices):
                while (sell + 1) < len(prices) and prices[sell] <= prices[sell + 1]:
                    sell += 1

                if prices[sell] - prices[buy] > profit:
                    profit = prices[sell] - prices[buy]
                sell += 1
            buy += 1
        
        return profit

    def amruthaMaxProfit(self, prices: List[int]) -> int:
        maximum = 0
        minimum = max(prices)

        for price in prices:
            minimum = min(price, minimum)
            maximum = max(price - minimum, maximum)

        return maximum

def main():
    sol = Solution()

    input1 = [7, 1, 5, 3, 6, 4]
    input2 = [7, 6, 4, 3, 1]
    input3 = [5, 4, 3, 2, 5]

    #print(sol.maxProfit(input1))
    print(sol.amruthaMaxProfit(input1))


if __name__ == "__main__":
    main()