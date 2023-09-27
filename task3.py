#!python3

"""
Write a python script display the values of the dictionary
  1. that are sorted by their keys (ascending values) 
  2. that are sorted by their values (ascending) 
  
(3 points)
"""
sortMe = {1: -2,   2: 6,   4: 0,   6: 1,   9: 2,   10: 3,  11: 0,  13: 3,  14: 4,   15: -2,  17: 0,   18: -1,   20: 3}
sort=[]



a=1
l=sor
for j in sortMe:



for k in sortMe:
  if a==1:
    sort.append(sortMe[k])
    a+=1
  else:
    for i in sort:
      if sortMe[k]<sort[i]:
        sort.append(sortMe[k],i)
      elif sortMe[k]>=sort[i]:
        sort.append(sortMe[k])
      break



  """
  else:
    for i in sort:
      if sortMe[k]<sort[i]:
        sort.append(sortMe[k],i)
        break
      elif sortMe[k]>=sort[i]:
        sort.append(sortMe[k])
        break
print(sort)"""