'''
There are n cities connected by some number of flights. You are given an array flights[i] = [fromi, toi, pricei] indicates that there is a flight
from city fromi to city toi with cost pricei. 

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, 
return -1.

Example 1:
Input: n = 4, flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The optimal path with at most 1 stop from city 0 to 3 has cost 100 + 600 = 700. Note that the path through cities [0, 1, 2, 3] is cheaper
but is invalid because it uses 2 stops.
'''

from collections import defaultdict

n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
k = 0

def cheapestPrice(n, flights, src, dst, k):
    adjList = defaultdict(list)
    changed = False
    for i in range(len(flights)):
        fromCity = flights[i][0]
        toCity = flights[i][1]
        price = flights[i][2]
        adjList[fromCity].append((toCity, price))
    
    minPrice = ['inf'] * n
    minPrice[src] = 0
    numStops = [-1] * n
    
    for j in range(n - 1):
        changed = False
        for i in range(n):
            if adjList[i] and minPrice[i] != 'inf':
                for toCity, price in adjList[i]:
                    if minPrice[toCity] == 'inf' and minPrice[i] != 'inf':
                        minPrice[toCity] = price + minPrice[i]                  
                        numStops[toCity] += 1
                        changed = True
                    elif ((price + minPrice[i]) < minPrice[toCity]) and (numStops[i] < k):
                        minPrice[toCity] = price + minPrice[i]                  
                        numStops[toCity] += 1
                        changed = True

        if changed == False:
            return minPrice[dst]
    
    return -1

print(cheapestPrice(n, flights, src, dst, k))
