"""

"""
command = input('>: ').lower()

# This is for identifying car started
already_started = False

# This is for identifying car stopped
already_stopped = False
while command:
    if command == 'help':
        print("""start-to start the car 
stop-to stop the car
quit-to exit""")
    elif command == 'stop':
        if already_stopped:
            print('car is already stopped')
        else:
            print('stop the car')
            already_stopped= True
    elif command == 'start':

        if already_started:
            print('car is already started')
        else:
            print('start the car')
            already_started = True

    elif command == 'quit':
        break
    else:
        print("i don't understand that..")

    command = input('>: ').lower()
else:
    print("i don't understand that..")










