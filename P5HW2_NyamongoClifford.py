# A brief program used to add and subtract 2 random numbers
# 04/15/2022
# CTI-110 P5HW2 - Math Quiz
# Nyamongo Clifford
#
#def math_addition():
import random
#Adding 2 random numbers
num1 = random.randint(0, 1000)

num2 = random.randint(0, 1000)

#Menu
print('MAIN MENU')
print('-------------------------------')
print('1. Adding random number')
print('2. Subtracting Random Number')
print('3. Exit')





selection = int(input("Please choose one of the menu options: "))


def Math_Addition():

    print(str(num1) + " + " + str(num2) + " = ?")

    result = int(input("Enter the answer: "))

    if result == (num1 + num2):

        print("Congratulations!")

    else:

        print("The correct answer is: " + str(num1 + num2))

#Subtracting random numbers
def Math_subtraction():

    print(str(num1) + " - " + str(num2) + " = ?")

    result = int(input("Enter the answer: "))

    if result == (num1 - num2):
        print("Congratulations!")

    else:
        print("The correct answer is: " + str(num1 - num2))

#If statement that allow the the user to enter eithe 1,2 or 3
if selection == 1:
    Math_Addition()
elif selection == 2:
    Math_subtraction()
elif selection == 3:
    print("You have exited the program")
    print("Thank you for playing")
    print("Bye!!")
else:
    print("Error,Please choose 1, 2 or 3")

#While loop to allow user to enter call the function
while selection != 1 and selection != 2 and selection != 3:
    selection = int(input("Please choose 1, 2 or 3: "))
    if selection == 1:
        Math_Addition()
    elif selection == 2:
        Math_subtraction()
    elif selection == 3:
        print("You have exited the program")
    else:
        print("Error,Please choose 1, 2 or 3")

