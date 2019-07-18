#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  limiter = 999999

  for i in recipe:
    if i in ingredients:
      # print ((ingredients[i] // recipe[i]))
      if ingredients[i] // recipe[i] < limiter:
        limiter = ingredients[i] // recipe[i]
    else:
      print(0)
      return 0
  
  return limiter


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))