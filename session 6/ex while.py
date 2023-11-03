
students = 15
while students>0:
    student=(input()) # the name of student
    score=(int(input()))
    if score >= 10:
      print(student, "with ","score",score, " is accepted")
    else:
       print(student,"with","score",score,"is failed")
       student = students - 1
print("end of score table")


       

