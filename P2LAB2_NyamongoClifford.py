''' Type your code here. '''
current_price = int(input())
last_months_price = int(input())

#current_price = int(input(x))
#last_months_price = int(input(y))

diff =  current_price - last_months_price
estimate = (current_price * 0.051) / 12

print(f'This house is ${current_price}. The change is ${diff} since last month.')
print(f'The estimated monthly mortgage is ${estimate:.2f}.')