#Price of a house is 10Million =1,00,00,000
#if buyer has good credit,
#    they need to put down 10%
#otherwise
#    they need to put down 20%
#Print the down payment
price = input('What is the price of the house? ')
if_credit = False
if if_credit:
    down_payment = int(price) * 0.1
    print('Need to pay 10% of money')
    print('Down payment is ' , down_payment)
else:
    down_payment = int(price) * 0.2
    print('Need to pay 20% of money')
    print('Down payment is ' , down_payment)

'''
price = 1000000
has_good_credit  = True

if has_good_credit:
    down_payment = 0.1 * price
else:
     down_payment = 0.2 * price
print(f"Down payment: ${down_payment}") #f means formatted string
'''