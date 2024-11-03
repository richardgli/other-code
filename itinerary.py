""" 
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival curAirports of one flight. Reconstruct the itinerary in order and return it.
All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi 
"""

// Somewhat functioning
d = {}
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
out = [None] * len(tickets)

for i in range(len(tickets)):
    l = []
    for j in range(len(tickets)):
        if tickets[i][0] not in d and tickets[i][0] == tickets[j][0]:
            if out[i] == None:
                out[i] = 1
            else: 
                out[i] += 1
            l.append(tickets[j])
    if tickets[i][0] not in d:
        d[tickets[i][0]] = l, i

curAirport = "JFK"

def dfs(curAirport, path):
    while True:
        ticket, index = d[curAirport]
        if out[index] == 0:
            path.insert(1, curAirport)
            return path
        else:
            cur = ticket.pop()
            d[curAirport] = ticket, index
            out[index] -= 1
            curAirport = cur[1]
            if curAirport not in d:
                path.insert(1, curAirport)
                return path
        dfs(curAirport, path)

print(dfs(curAirport, ["JFK"]))
