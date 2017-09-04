def guess_number(secret=42):
    while True:
        # read input from console and parse it as integer
        guess = int(input('Please enter a number: '))
        if guess == secret:
            print('Hooray!')
            break # break out of while loop
        print('Another try')
