import random
OPTIONS=["scissors","paper","stone"]
cpu=random.choice(OPTIONS)
print("type only 1 item from these words: scissors,paper,stone")
player=input("choose from: scissors,paper,stone")

if player == "scissors":
 if cpu == "paper":
     print("You won")
     if cpu == "stone":
      print("You lose")
      if cpu == "scissors" :
       print=("Draw")
      else:
        print("you entered wrong word")
if player == "stone" :  
      if cpu == "paper" :
       print( "You lose")  
      if cpu == "scissors":
       print("You lose")
      if cpu == "stone":
       print("DRAW")  
      else:
       print("you entered wrong word")
if player == "paper":
      if cpu == "paper" :
       print ("DRAW")
       if cpu == "stone":
        print("You won")
      if cpu == "scissors":
       print("You lose")
      else:
       print("you entered wrong word")
print("Rematch?")    
