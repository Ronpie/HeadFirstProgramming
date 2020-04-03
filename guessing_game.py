import random
import argparse
ap = argparse.ArgumentParser()
ap.add_argument('-f','--from',default=0,type=int,
        help='choosing guessing game from number (default is 0)')
ap.add_argument('-t','--to',default=100,type=int,
        help='choosing guessing game to number (default is 100)')
ap.add_argument('-c','--chance',default=6,type=int,
        help='choosing guessing chance depend of the range of guessing (default is 6)')
args = vars(ap.parse_args())

left = args['from']
right = args['to']
number = random.randint(left,right)
guess = None
chance = args['chance']
guess_number = set()

while 1:
    if guess == None:
        guess_range = range(left,right+1)
        print('Game started, guessing number between {} to {}'.format(left,right))
    elif guess >number:
        if guess <right:
            guess_range = range(left,guess+1)
            right = guess
            print('please guess in ' + str(range(left,right)))
        else:
            pass
    else:
        if guess > left:
            guess_range = range(guess,right+1)
            left = guess
            print('please guess in ' + str(range(guess,right)))
        else:
            pass
    if chance >1:
        print('You have {} chances left'.format(chance))
    elif chance ==1:
        print('You have 1 chance left')
    else:
        pass
    guess = int(input("Guess the number: "))
    if guess not in guess_number:
        guess_number.add(guess)
    else:
        print('You already guess this number')
        continue
    if guess not in guess_range:
        print('please guess in range suggest')
        continue
    else:
        chance -= 1
        print('uhmmmmmm ...')
        if (guess == number):
            print('You guess right')
            break
        else:
            if chance ==0:
                print('Game over')
                break
            else:
                print('Pick another number')
