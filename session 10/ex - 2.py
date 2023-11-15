#import keyboard
#import sys

while True:
    try:
        user_input = input('Enter space-separated integers: ').split()

        list_of_integers = [int(item) for item in user_input]

        print(list_of_integers)  # [1, 2, 3]
        print(list_of_integers[-1]+list_of_integers[-2])        
    except ValueError:
        print("Not an integer! Please enter an integer.")

        continue
    else:
        break

#if keyboard.is_pressed("z"):
        print(keyboard.is_pressed("z"))
        sys.exit()

