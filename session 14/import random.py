import random
import numpy as np

OPTIONS=[1,2,3,4,5,6,7,8,9]

while OPTIONS :
  Player1 =int(input("Enter your choice:"))

  if Player1 in OPTIONS:
   OPTIONS.remove(Player1)
   print(OPTIONS)

  if not OPTIONS:
   break
  
  CPU = random.choice(OPTIONS)
  OPTIONS.remove(CPU)
  print(OPTIONS)

  winning_combinations = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [4, 5, 6], [7, 8, 9], [7, 5, 3], [2, 5, 8],  [3, 6, 9], [3, 5, 7], [3, 2, 1], [9, 8, 7], [6, 5, 4], [9, 6, 3], [8, 5, 2],[7, 4, 1], [9, 5, 1]] 
  if any(combination == Player1 for combination in winning_combinations):  
    break
  #print("Player 1 won")
 
  if any(combination == CPU for combination in winning_combinations):
    break
  #print ("CPU won")

else:
  print("Draw")

print("End of the game")  