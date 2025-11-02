# Best time to buy & sell stocks
# DP - Remembering the past
def stock(prices):
    profit=0
    minimum=prices[0]
    for i in range(1,len(prices)):
        cost=prices[i]-minimum # Calculating cost using the traced minimum element
        profit=max(profit,cost) # Calculating profit using the max of previous profit and current cost
        minimum=min(minimum,prices[i]) # Keeping track of the minimum element
    return profit
prices=[7,1,5,3,6,4]
print(stock(prices))
# Time Complexity - O(N)
# Space Complexity - O(1)