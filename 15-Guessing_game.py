#We have 3 chances to make a guess a number
#if we fail in 3 we get error as "Sorry you failed!"
#if correct "You win!"
'''
number = input('Guess: ')
secret_number = 9
i = 0
while i < 3:
    i = i + 1
    if number == secret_number:
        print('You win!')
    #break
    else:
        print('Sorry you failed!')
'''
secret_num = 9
count = 0
count_limit = 3
while count < count_limit:
    guess = int(input('Guess: '))
    #count = count + 1
    count += 1
    if guess == secret_num:
        print('You win!')
        break
else:
    print('Sorry you failed!')
print('######################################')
print(type(secret_num))
print(type(guess))

