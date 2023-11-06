for student in range(3):
    student=(input()) # the name of the student
    score=(int(input())) # the score of the student
    if score > 20 :
       print("you typed wrong number")
    if (score >= 10 and score <=20) :
      print(student, "with ","score",score, " is accepted") 
    if score < 10 :
       print(student,"with","score",score,"is failed")
print("end of score table")
    
