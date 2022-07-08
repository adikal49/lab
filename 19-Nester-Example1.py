#print like below the "F" using nested loops
'''
*****
**
*****
**
**'''
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    #print('x' * var) , this also works but not preferred
    output = ''
    for count in range(x_count):
        #output = count * 'x' ###### Append count to x
        output += 'x'
    print(output)

