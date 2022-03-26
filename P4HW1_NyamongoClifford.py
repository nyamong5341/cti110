# CTI-110
# P4HW2 - Pizza Order
# Nyamongo Clifford
# 2022/03/21
#

Students_No = int(input('How many students do you want to order pizza for?: '))                #ASk user to enter number of students
Pizza_number = float(input('Enter number of people per  pizza(1.5, 2 or 3): '))                #ask user to enter number of people per pizza
while Pizza_number not in [1.5,2,3]:                                                           # program runs a while loop and only 1.5,2 and 3 are true

    print('INVALID ENTRY!!!!!')
    print('Should have entered 1.5, 2 or 3')
    Pizza_number = float(input('Enter number of people per pizza again.(1.5, 2 or 3): '))       # program asks to enter again the number of people per pizza
    print(Pizza_number)
print('----Pizza order-------')

No_pizza = (Pizza_number * Students_No) / 6           # Each pizza has 6 slices
Price_beforetax = No_pizza * 5
Tax = Price_beforetax + (0.06 * Price_beforetax)      #Culcutate Tax
Price = Price_beforetax + Tax                         #Culculate price after tax
print('Number of Students :'+str(Students_No))        # print number of students
print('Pizzas Needed:' +str(round(No_pizza)))         #print number of pizza in whole numbers
print('Price:$'+str(round(Price, 2)))                 #Print the totla price
print('--------------------------')

answer = input('Would you like to run the program again (Y for yes?) ')                            # asks the user if they want to run the program again
while answer == "Y" or "y":


    print()
    print()
    print('---------------------------------------------')
    Students_No = int(input('How many students do you want to order pizza for?: '))                #ASk user to enter number of students
    Pizza_number = float(input('Enter number of people per  pizza(1.5, 2 or 3): '))                #ask user to enter number of people per pizza
while Pizza_number not in [1.5,2,3]:                                                           # program runs a while loop and only 1.5,2 and 3 are true

    print('INVALID ENTRY!!!!!')
    print('Should have entered 1.5, 2 or 3')
    Pizza_number = float(input('Enter number of people per pizza again.(1.5, 2 or 3): '))       # program asks to enter again the number of people per pizza
    print(Pizza_number)
print('----Pizza order-------')

No_pizza = (Pizza_number * Students_No) / 6           # Each pizza has 6 slices
Price_beforetax = No_pizza * 5
Tax = Price_beforetax + (0.06 * Price_beforetax)      #Culcutate Tax
Price = Price_beforetax + Tax                         #Culculate price after tax
print('Number of Students :'+str(Students_No))        # print number of students
print('Pizzas Needed:' +str(round(No_pizza)))         #print number of pizza in whole numbers
print('Price:$'+str(round(Price, 2)))                 #Print the totla price
print('--------------------------')

answer = input('Would you like to run the program again (Y for yes)? ')




