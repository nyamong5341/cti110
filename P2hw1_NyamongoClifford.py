#This is a project that can be used yo culculate sales tax and determine overall price of things bought from a store
#Date:Feb,19 2022
#CTI-110 P2HW1- Total Purchases
#Nyamongo Clifford
                      #assign x, x1,x2 as an  input
x= float(input())
x1= float(input())
x2= float(input())
x3= float(input())
x4=float(input())
print('Enther the price of item: ' +str(x)+'')
print('Enther the price of item:' +str(x1)+'')
print('Enther the price of item:' +str(x2)+'')
print('Enther the price of item:' +str(x3)+'')
print('Enther the price of item:' +str(x4)+'')
print('-------Results-------')
x5=x+x1+x2+x3+x4

#sum of x,x1,x3,x4
print('Subtotal: '+str(x5)+'')
x6=x5*0.07                   #sales tax( 7% of Subtotal)
x6 = round(x6, 2)
print('Sales tax:  '+str(x6)+'')
x7= x5-x6                     #subtotal less the 7% sales tax
print('Total: '+str(x7)+'')


