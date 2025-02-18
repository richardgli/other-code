'''
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where 
edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of sucess of 
traversing that edge succProb[i].
Given two nodes start and end, find the path with the maximum probability of success to go from start 
to end and return its success probability.
If there is no path from start to end, return 0. Your answer will be accepted if it differs from the 
correct answer by at most 1e-5.

Example 1:
Input: n = 3, edges = [[0, 1], [1,2], [0, 2]], succProb = [0.5, 0.5, 0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, on having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25
'''

from collections import defaultdict
import heapq

def findSuccessProbability(n, edges, succProb, start, end):
    adjList = defaultdict(list)

    for i in range(n):
        node1 = edges[i][0]
        node2 = edges[i][1]
        adjList[node1].append((succProb[i], node2))
        adjList[node2].append((succProb[i], node1))

    heap = [(-1, start)]
    heapq.heapify(heap)
    maxProb = [0] * n
    maxProb[start] = 1

    while heap:
        probability, node = heapq.heappop(heap)

        if node == end:
            return probability
        
        if adj_list[node]:
            for prob, adjNode in adj_list[node]:
                if probability * prob > maxProb[adjNode]:
                    maxProb[adjNode] = -probability * prob
                    heapq.heappush(heap, (-maxProb[adjNode], adjNode))
    return 0
