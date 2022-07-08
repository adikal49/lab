'''for item in 'Python':
    print(item)
############################
count = [1 , 2 , 3, 4]
for var in count:
    print(var)
############################
name = ['Adi', 'moni', 'daday', 'mummy']
for var in name:
    print(var)
############################
for item in range(5, 10, 2): #start, stop, step
    print(item)
'''
#######################################
'''#shopping cart to add all items in list
list = [10 , 20, 30]
for var in list:
    print(var)
    var += var
print(f'total is', var)'''
#######################################
prices = [10 , 20, 30]
total = 0
for price in prices:
    #total = total + price
    total += price
#print(total)
print(f"total: {total}")

