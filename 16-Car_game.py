#>help
#start - to start the car
#stop - to stop the car
#quit - to exit
#I don't understand that...
#Car started...Ready to go!
#Car Stopped.

#Understand the condition
# we are gonna run this loop untill we quit
command = ""
started = False
#while command != 'quit':
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print("Car already started...!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == 'stop':
        if not started:
            print("Car is already Stopped...!")
        else:
            started = False
            print("Car Stopped.")
    elif command == 'quit':
        break
    elif command == 'help':
        print('''
            start - to start the car
            stop  - to stop the car
            quit  - to exit
            ''')
    else:
        print("I don't understand that...")
