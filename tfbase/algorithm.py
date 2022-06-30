import json
import random as r
import math
import heapq as hq
from subprocess import CREATE_NEW_CONSOLE
from traceback import print_tb
import finalSolution as fs

def transformGraph():
    G=[]
    Nodes=fs.nodes
    Loc =[]
    for lat_long in Nodes:
     Loc.append(Nodes[lat_long]) 

    for list in fs.ListAds:
      auxlist=[]
      for node in list:
        auxlist.append((node.id,node.Data.getTrafficFactor()))
      G.append(auxlist)
    return G, Loc

def bfs(G, s):
  n = len(G)
  visited = [False]*n
  path = [-1]*n # parent
  queue = [s]
  visited[s] = True
  while queue:
    u = queue.pop(0)
    for v, _ in G[u]:
      if not visited[v]:
        visited[v] = True
        path[v] = u
        queue.append(v)

  return path


def dfs(G, s):
  n = len(G)
  visited = [False]*n
  path = [-1]*n # parent
  queue = [s]
  visited[s] = True
  while queue:
    u = queue.pop()
    for v, _ in G[u]:
      if not visited[v]:
        visited[v] = True
        path[v] = u
        queue.append(v)

  return path
  
def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    cost = [math.inf]*n

    cost[s] = 0
    pqueue = [(0, s)]
    while pqueue:
        g, u = hq.heappop(pqueue)
        if not visited[u]:
            visited[u] = True
            for v, w in G[u]:
                if not visited[v]:
                    f = g + w
                    if f < cost[v]:
                        cost[v] = f
                        path[v] = u
                        hq.heappush(pqueue, (f, v))

    return path, cost

G, Loc = transformGraph()

def graph():
    return json.dumps({"loc": Loc, "g": G})


def paths(s, t):
    bestpath, _ = dijkstra(G, s)
    path1 = bfs(G, s)
    path2 = dfs(G, s)

    return json.dumps({"bestpath": bestpath, "path1": path1, "path2": path2})
