"""
https://leetcode.com/problems/reconstruct-itinerary/?envType=daily-question&envId=2023-09-14

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
"""
total_trips = None
def get_itinerary(src, adj_list, trip_count, itinerary):
  for i, (dest, used) in enumerate(adj_list[src]):
    if not used:
      adj_list[src][i][1] = True
      itinerary.append(dest)
      if trip_count + 1 == total_trips:
        return True
      if get_itinerary(dest, adj_list, trip_count + 1,itinerary):
        return True
      else:
        itinerary.pop()
        adj_list[src][i][1] = False
  return False
  
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        global total_trips
        total_trips = len(tickets)
        
        for s,d in tickets:
          adj_list[s].append([d, False])
        for airport in adj_list:
          adj_list[airport].sort()
        
        itinerary = ['JFK']
        get_itinerary('JFK', adj_list, 0, itinerary)
        return itinerary

