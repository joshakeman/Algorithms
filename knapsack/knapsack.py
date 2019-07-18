#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):

  sack = {'Value': 0, 'Chosen': []}
  picked = []
  value = 0
  total = 0
  # best = [0, 0, 0]
  # print("Sack at start: ", sack)
  # while total < capacity:

  while total < capacity:
    best = items[0]
    for i in items:
      # print (i[2] - i[1])
      if i[2] - i[1] > best[2] - best[1]:
        best = i

    if best[1] + total < capacity:
      picked.append(best[0])
      value += best[2]
      print (picked)
      print (value)
      total += best[1]
      items.remove(best)
    else:
      ordered = sorted(picked)
      sack['Value'] = value
      sack['Chosen'] = ordered
      return sack
    
    best = items[0]
    # print("Sack after: ", sack)
    # print(items)
    # print(total)

    # print(items[best[0] -1 ])
  
  # print(total)
  # print(sack)
  # return sack
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')