#!/usr/bin/python

import argparse

def find_max_profit(prices):

  lowest = prices[0]
  profit = 0


  for i in range(0, len(prices) - 1):
    # print(i)

    if prices[i] < lowest:
      lowest = prices[i] 
    else:
      if (prices[i] - lowest) > profit:
        profit = prices[i] - lowest
  
  if profit == 0 :
    profit = max(prices[1:]) - prices[0]

  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))