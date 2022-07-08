'''if temperature is greater than 30
    it's a hot day
otherwise if it's less than 10
    it's a cold day
otherwise
    it's neither hot nor cold '''
#comparison operators are:
#>, <, >=, <=, ==, !=
temp = input('What is the temperature today? ')
if int(temp) >= 30:
    print("it's a hot day")
elif int(temp) < 30:
    print("it's a cold day")
else:
    print("it's neither hot nor cold")
   