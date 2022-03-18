# Pizza order
# CTI-110
# P3HW2 - Pizza Order
# Nyamongo Clifford
# 2022/03/06
#Ask a user to enter the number of students and how many students will share pizza

Students_No = int(input('How many students do you want to order pizza for?: '))
Pizza_Number = float(input('How people will be sharing each pizza?: '))
#Condition on when they enter the number of pizza numbers entered
if Pizza_Number == 1.5:
    No_pizza= int(Students_No /Pizza_Number)
    print(str(No_pizza))
elif Pizza_Number == 2:
    No_pizza= Students_No /Pizza_Number

elif Pizza_Number == 3:
    No_pizza= Students_No /Pizza_Number
else:
    print('Invalid Entry!!!')                        #Display if they enter any other number that is not 1.5, 2 or 3
    print('Should have entered 1.5, 2, 3 ')
    No_pizza = 0
print('----Pizza order-----')
Price_beforetax = No_pizza * 5
Tax = Price_beforetax + (0.06 * Price_beforetax)      #Culcutate Tax
Price = Price_beforetax + Tax                         #Culculate price after tax
print('Number of Students :'+str(Students_No))        # print number of students
print('Pizzas Needed:' +str(round(No_pizza)))         #print number of pizza in whole numbers
print('Price:$'+str(round(Price, 2)))                 #Print the totla price
print('--------------------------')







