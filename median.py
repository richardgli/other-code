'''
The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value, and the median is the mean of the two middle values.

addNum() adds the integer num from the data stream to the data structure.
findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer
will be accepted.

Example:
Input:
addNum addNum findMedian addNum findMedian
1 2 0 3 0

Output:
None None 1.5 None 2
'''

import heapq
def addNum(num, median):
    if num < median:
        num = -num
        heapq.heappush(l1, num)
    elif num > median:
        heapq.heappush(l2, num)
    
    if len(l1) - len(l2) > 1:
        n = -heapq.heappop(l1)
        heapq.heappush(l2, n)
    elif len(l2) - len(l1) > 1:
        n = heapq.heappop(l2)
        heapq.heappush(l1, -n)
    return median

def findMedian(median):
    if len(l1) % 2 != 0 and len(l2) % 2 != 0:
        median = (-l1[0] + l2[0]) / 2
    elif len(l1) > len(l2):
        median = l1[0]
    elif len(l2) > len(l1):
        median = l2[0]
    return median

functions = list(input().split())
nums = list(map(int, input().split()))
median = [0]
l1 = []
l2 = []
answer = []
heapq.heapify(l1)
heapq.heapify(l2)

for i in range(len(functions)):
    if functions[i] == "addNum":
        median[0] = addNum(nums[i], median[0])
        answer.append(None)
    elif functions[i] == "findMedian":
        median[0] = findMedian(median[0])
        answer.append(median[0])
print(answer)
