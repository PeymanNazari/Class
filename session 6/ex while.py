counter = 4
while counter>0:
    student=input() # the name of the student
    score=int(input()) # the score of the student
    if score > 20:
         print("wrong score")
    if score >= 10:
         if score <=20:
             print(student, "with", "score",score,"is accepted")      
    else:
         print(student,"with", "score",score,"is failed")
    counter = counter - 1       
print("end of score table")
