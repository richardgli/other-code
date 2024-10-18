'''
Given an integer array nums and an integer k, return kth.
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.
Solve without sorting.

nums = [3, 2, 1, 5, 6, 4], k = 2
5

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
4
'''

import heapq

nums = list(map(int, input().split()))
k = int(input())

heapq.heapify(nums)
for i in range(len(nums) - k + 1):
    curMax = heapq.heappop(nums)
print(curMax)
