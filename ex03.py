#movies = ["Avatar", "Titanic", "Avengers"]
#movies.append("Alien")
#print(movies[3])
#movies.append("thriller")
#print(movies[4])
#genres = ["SciFi", "Fantasy", "Drama"]

#colors = ["Red", "Blue", "Yellow"]
#colors.insert(2 , "black")
#colors.append("green")
#print(colors[3])
#print(colors)
#colors.pop(4)
#print(colors)

#points = [15 , 36 , 74 , 88]
#points.pop(2)
#points.append(95)
#print(points)

#cars = ["BMW", "Toyota", "Audi"]
#cars.pop(1)
#cars.insert(1,"tesla")
#cars.append("Mazda")
#print(cars)

#def greet():
    #print("Hello from a function")
    #print("Have a great day")
#greet()    

#def personal_greet ():
    #print("Hello")
    #print("Have a great day")

#name=input()
#personal_greet()

def double(number):
    print(number*2)

number=12
double(number)


#def bmi (weight,height):
 #index= weight / (height * height)
 #print(index)
#weight=int(input())
#height=int(input())
#bmi(weight,height)

#def bmi (weight,height):
 #index = weight / (height * height)
 #return index
#weight=int(input())
#height=int(input())
#sh=bmi(weight,height)
#print(sh)


def profile(name,lastname,age):
 S= name,lastname,age
 return S
name=input()
lastname=input()
age=int(input())
pro=name,lastname,age 
print(pro)