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
kl = nums[:k]

heapq.heapify(kl)
for i in range(k, len(nums)):
    if nums[i] > min(kl):
        cur = heapq.heapreplace(kl, nums[i])
print(kl[0])
