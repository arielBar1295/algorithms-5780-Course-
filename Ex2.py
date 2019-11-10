#Question number 5
#By Ariel bar and Dana Morhaim
#for every agent we check:if option1 value's is less then option2 value's ,we can say that is not Pareto Improvement.
#enough to find one agent that option 2 is better for him and we can say it is not Pareto Improvement.
def isParetoImprovement(agents:List[Agent],option1:int,option2:int)->bool:
 for x in agents:
  if x.value(option1)<x.value(option2):
   return False
 return True
 #for every option we call isParetoImprovement and check if the specific option from the array is a Pareto Improvement of the option we got as a parameter,if it is, we can immediately say that the option we got as a parameter is not Pareto Optimal
 def isParetoOptimal(agents:List[Agent],option:int,allOption:List[int])->bool:
  for x in allOption:
   if isParetoImprovement(agents,x,option):
    return False
  return True
