#quuestion number 2
#made by Ariel Bar and Dana Morhaim
import networkx as nx
def addWeight(graph , dict):
  for edge in graph.edges :
    for x in dict:
      flag=False
      #if its an inner edge , its weight is the number of edges.
      if edge in dict[x]:
        graph[edge[0]][edge[1]]['weight']=graph.size()
        flag=True
        break
    if not flag:
      graph[edge[0]][edge[1]]['weight']=1
  return graph

def algo(graph , dict) :
  """
>>> dict={ "hadasa":[('5','6')],"rambam":[('2','3'),('3','4')]}
>>> G=nx.Graph()
>>> G.add_edge('1','5')
>>> G.add_edge('5','6')
>>> G.add_edge('2','6')
>>> G.add_edge('2','3')
>>> G.add_edge('3','4')
>>> G.add_edge('4','7')
>>> algo(G, dict)
{('5', '6'), ('3', '2'), ('7', '4')}
>>> dict1={ "hadasa":[('5','6')],"rambam":[('2','3')]}
>>> G1=nx.Graph()
>>> G1.add_edge('1','5')
>>> G1.add_edge('5','6')
>>> G1.add_edge('2','6')
>>> algo(G1, dict1)
{('6', '5')}
>>> dict2={ "hadasa":[],"ramban":[('2','3'),('3','4')]}
>>> G2=nx.Graph()
>>> G2.add_edge('2','3')
>>> G2.add_edge('3','4')
>>> G2.add_edge('4','7')
>>> algo(G2, dict2)
{('3', '2'), ('7', '4')}
    """
  graph = addWeight(graph , dict)
  max_match=nx.max_weight_matching(graph)
  print(max_match)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
