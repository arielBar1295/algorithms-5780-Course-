#question number 5
#By Ariel Bar and Dana Morhaim
from typing import List

class Agent:
    def value(item_index: int) -> float:
        return 5.0

# For each two agents A and B, if we remove from the bundle of B the item most valuable for A, then A does not envy B
def is_EF1(agents: List[Agent], bundles: List[int])->bool:
    for agent1 in agents:
        sumAgent1 = sum_of_items(agents[agent1], bundles[agent1])
        for agent2 in agents:
            if agent1 != agent2:
                sumAgent2 = sum_of_items(agents[agent1], bundles[agent2])
                maxItem = max_item(agents[agent1], bundles[agent2])
                if sumAgent1<sumAgent2-maxItem:
                    return False
    return True

#sum the values of the items in a list
def sum_of_items(agent: Agent, items: List[int])-> float:
    sum = 0
    for item in items:
        sum = sum+ agent.value(item)
    return sum

#find the most valuble item of an agent
def max_item(agent: Agent, items: List[int])-> float:
    max = 0
    for item in items:
        if max < agent.value(item):
            max = agent.value(item)
    return max
