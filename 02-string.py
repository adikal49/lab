#course = 'Python's Course for Beginners'
#course = "Python's Course for Beginners"
#course = 'Python for "Beginners"'
course = ''' 
Hi John,
Here is our first email to you.
Thank's,
john
'''
#print(course)

##############################
training = 'Python for Beginners'
#           01234
#-1, start from last character
#print(training[0]), print first char
#print(training[-1]), print last 1 char
#print(training[0:3]), first 0-2 chars
#print(training[0:]), 0 to all
#print(training[1:]), first chars will ignore
#print(training[:5]), assuming first 0-5 chars
print(training[:])


####################
name = 'Jennifer'
print(name[1:-1])


print('##############################')

first = 'John'
last  = 'Smith'
#print John [Smith] is a Coder
message = first + ' [' + last + '] is a Coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)