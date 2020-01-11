from typing import List
import networkx as nx

"""
The example module checks the change shifting function
The example is from: https://www.hamichlol.org.il/%D7%9E%D7%A2%D7%92%D7%9C%D7%99_%D7%A1%D7%97%D7%A8_%D7%A2%D7%9C%D7%99%D7%95%D7%A0%D7%99%D7%9D

>>> a=Worker('a',[3,2,4,1],1)
>>> b= Worker('b', [3,5,6], 2)
>>> c= Worker('c', [3,1], 3)
>>> d= Worker('d', [2,5,6,4], 4)
>>> e= Worker('e', [1,3,2], 5)
>>> f= Worker('f', [2,4,5,6], 6)

>>> workers = [a,b,c,d,e,f]
>>> exchange_shifts(workers)

c moves from shift 3 to Shift 3
a moves from shift 1 to Shift 2
b moves from shift 2 to Shift 5
e moves from shift 5 to Shift 1
d moves from shift 4 to Shift 6
f moves from shift 6 to Shift 4
"""

class Worker:
    name: str
    preferences: list
    current_shift: int

    def __init__(self, name, preferences,current_shift):
        self.name = name
        self.preferences = preferences
        self.current_shift = current_shift

#this method builds the graph for the first time
def build_graph(workers):
    G = nx.DiGraph()
    for worker in workers:
        for shift in worker.preferences:
            G.add_edge(worker.name,shift)
        G.add_edge(worker.current_shift,worker.name)
    return G


def exchange_shifts (workers: List[Worker]):
    G = nx.DiGraph()
    G = build_graph(workers)

    #[(3, 'c', 'forward')]
    while G.edges:
        # find the cycle in the graph
        changes = list(nx.find_cycle(G, orientation='ignore'))
        for change in changes:

            if(type(change[0]) == str):
                currentShift = find_shift(workers, change[0])
                print(str(change[0]) + " moves from shift " +str(currentShift) +" to Shift " + str(change[1]))
            # remove the nodes that were found in the cycle
            if (G.has_node(change[0])):
                G.remove_node(change[0])
            if (G.has_node(change[1])):
                G.remove_node(change[1])

#this function returns the current shift of the worker
def find_shift(workers: List[Worker], workerName):
    for worker in workers:
        if worker.name==workerName:
            return worker.current_shift


if __name__ == "__main__":
    import doctest
    doctest.testmod()
