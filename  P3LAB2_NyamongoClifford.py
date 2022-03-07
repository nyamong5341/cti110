service = input('Enter desired auto service:\n')
print('You entered: ' + service)
cost = 0
if service =='Oil change':
    cost = 35
elif service =='Tire rotation':
    cost = 19
elif service =='Car wash':
    cost = 7
else:
    print('Error: Requested service is not recognized')
if cost != 0:
    print('Cost of ' + service.lower() + ': $' +str(cost))
