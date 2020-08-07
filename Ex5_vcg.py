# question number 7
# By Ariel Bar and Dana Morhaim
import networkx as nx
#import math
from typing import List


class Agent:
    def vcg_cheapest_path(graph, source, target):

        shortP = nx.dijkstra_path(graph, source, target)
        pathLen = nx.dijkstra_path_length(graph, source, target)
        allCosts = []
        for i in range(len(shortP[:-1])):
            # get the weight of the edge
            selfVal = graph[i][i + 1]['weight']
            newGraph = graph.copy()
            newGraph.remove_edge(i, i + 1)
            newPathLen = nx.dijkstra_path_length(newGraph, source, target)
            cost = newPathLen - pathLen - selfVal
            allCosts.append(cost)

        for cost in allCosts:
            print(cost)
