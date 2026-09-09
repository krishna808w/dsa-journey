def max_profit(prices):
  lowest_price = prices[0]
  max_profit = 0
  for i in range(len(prices)):
    if(prices[i]<lowest_price):
      lowest_price=prices[i]
    if(prices[i]-lowest_price>max_profit):
      max_profit=prices[i]-lowest_price
  return max_profit


print(max_profit([7, 2, 5, 8, 1, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))  # 0
print(max_profit([2, 4, 1]))  # 2
print(max_profit([1, 2]))  # 1

# Time Complexity: O(n)
# Space Complexity: O(1)