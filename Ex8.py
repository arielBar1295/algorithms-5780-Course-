#By Ariel Bar and Dana Morhaim
import random
import itertools, collections

#dictPlayer = collections.defaultdict(float)
player_dict={"a" : 10,
            "b" : 15,
	    "c" : 25,
	    "ab" : 20,
	    "ac" : 25,
	    "bc" : 30,
	    "abc" : 37
}
player_dict2={ "a" : 10,
               "b" : 15,
	       "c" : 0,
	      "ab" : 20,
	      "ac" : 10,
	      "bc" : 15,
	     "abc" : 20
}

airport_problem= {
   "":	0,
  "a":  1,
  "b":  2,
  "c":  3,
  "d":  4,
  "1":  5,
  "2":  6,
  "3":  7,
  "4":  8,
  "5":  9,
  "6": 10,
  "7": 11,
  "8": 13,
  "e": 12,
  "f": 13,
  "g":  14,
  "h":  15,
  "i":  16,
  "j":  17,
  "k":  18,
  "l":  19,
  "m":  20,
  "n":  21,
  "o":  22,
  "p":  23,
  "q":  24,
  "r":  25,
  "s":  26,
  "t":  27,
  "u":  28,
  "v":  29,
  "w":  30
}
def Shapley_value(num:int,  player_dict:dict):
 """
	Calculate the Shapley values for all players.
	:param num: the number of permutations.
	:param player_dict:a dict where each key is a string representing a subset of players, and its value is the cost of that subset.
	:return: a dict where each key is a single char representing a player, and each value is the player's Shapley value.
  """
 player_margin_dict = collections.defaultdict(float)

 #airport problem
 airProblem=0
 #a string which each char represents a player.
 s=""
 for x, y in player_dict.items():
  if len(x)<2:
   s+=x
  if len(x)>1:
   airProblem=1	
	
 i=0
 while i < num:
  i+=1
  current_permutation=''.join(random.sample(s,len(s)))
  sub=""
  currCost=0
  for x in current_permutation:
   sub+=x
   sub = ''.join(sorted(sub))
   #means this is an airport problem, call costAir function to calculate the cost of the current subset.
   if airProblem == 0:
     Cost=costAir(sub,player_dict)
   else:
    Cost=player_dict[sub]
   marginal=Cost-currCost
   player_margin_dict[x]+=marginal
   currCost=Cost
 for x, y in player_margin_dict.items():
  player_margin_dict[x]=y/i
 return player_margin_dict

#calculate the cost of the subset for the air problem by finding the max value.
def costAir(current_permutation,player_dict:dict):
 mylist=[]
 for x in current_permutation:
  mylist.append(player_dict[x])
 return max(mylist)
  

def test():
 print("test 1:")
 test1=Shapley_value(20, player_dict)
 sum=0
 for x, y in test1.items():
  print(x,y)
  sum+=y
 assert(sum)==37 ,"should be 37"

 print("test 2:")
 test2=Shapley_value(3, player_dict)
 sum=0
 for x, y in test2.items():
  print(x,y)
  sum+=y
 assert(sum)==37 ,"should be 37"

 print("test 3:")
 test3=Shapley_value(20, player_dict2)
 sum=0
 for x, y in test3.items():
  print(x,y)
  sum+=y
 assert(sum)==20 ,"should be 20"

 print("test 4:")
 test4=Shapley_value(100000, airport_problem)
 sum=0
 for x, y in test4.items():
  print(x,y)
  sum+=y
 assert(sum)==30 ,"should be 30"



if __name__ == "__main__":
    test()
    print("Everything passed")
 
