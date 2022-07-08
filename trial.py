#>help
#start - to start the car
#stop - to stop the car
#quit - to exit
#I don't understand that...
#Car started...Ready to go!
#Car Stopped.

while True:
    help = input('>')
    if help == 'help':
        print('''
            start - to start the car
            stop  - to stop the car
            quit  - to exit
            ''')
        if input('>') == 'start':
            print("Car started...Ready to go!")
        elif input('>') == 'stop':
            print("Car Stopped.")
        else:
            break
    else:
        print("I don't understand that...")
    break

##################################################

#>help
#start - to start the car
#stop - to stop the car
#quit - to exit
#I don't understand that...
#Car started...Ready to go!
#Car Stopped.

#Understand the condition
# we are gonna run this loop untill we quit

from itertools import count


while True:
    help = input('>')
    if help == 'help':
        print('''
            start - to start the car
            stop  - to stop the car
            quit  - to exit
            ''')
        start = 'start'
        stop = 'stop'
        quit = 'quit'
        count = 0
        count_limit = 1
        while input('>') == start:
            print("Car started...Ready to go!")
            if input('>') == 'stop':
                print("Car Stopped.")
            else:
                #exit: 0
                break
    else:
        print("I don't understand that...")
else:
