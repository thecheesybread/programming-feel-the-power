from random import randint
target = randint(1, 100)
while True:
    guess = int(raw_input('Guess a number between 1 and 100: '))
    if guess == target:
        print 'Congratulations, you guessed it!'
        break
    if guess < target:
        print 'Your guess was too low'
    if guess > target:
        print 'Your guess was too high'

