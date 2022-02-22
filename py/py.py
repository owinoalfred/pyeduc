secret_number = 10
numberoftimes = 3
guess_count = 0

while guess_count<numberoftimes:
    guess = int(input("Guess a number!"))
    guess_count = guess_count+1
    if guess == secret_number:
        print("You won!!!")
        break
    else:
        print("Waaa try AGain!")