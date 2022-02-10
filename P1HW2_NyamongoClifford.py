# A project to find the number of pizza needed to be bought given the number of students
# 2020/08/2022
# CTI 110 P1HW2- Pizza Orders
# Clifford Nyamongo

print ("Enter the number of students who you would like to order pizza for. \n")
s = int(input())
slices =s * 3      # Number of slices will be equal to *3 because each student gets 3 slices
pizza = slices /6  # Number of pizza slices

print ("----Pizza Order--------")
print("Number of students :" +str(s))       # Display of number of students
print("Pizza slices needed:" +str(slices))  # Display  number of pizza slices needed
print("Pizza needed:" +str(pizza))          # Display pizza number  needed
print("--------------------------")

