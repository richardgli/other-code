'''
Problem:
2 House Robber
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the 
maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1, 2, 3, 1]
Output: 4

Example 2:
Input: [2, 7, 9, 3, 1]
Output: 12
'''

def money(houses):
  dp = [houses[0]] * len(houses)
  dp[1] = max(houses[0], houses[1])
  for i in range(2, len(houses)):
    dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])
  return max(dp)
