command1 = "start"
command2 = "stop"
command3 = "quit"

user_input  = str(input("input a car command! ")).lower()

while user_input != command3:
    user_input
    if user_input == command1:
        print('car is starting')
        break
    elif user_input == command2:
        print('Car has stopped! ')
        break
    else:
        print('BYE BYE')
        break