from random import randint
num = randint(1,100)

print 'please input a number!'
bingo = False

while bingo == False:
    answer = input()

    if answer < num:
        print '%d is too small!' %answer

    if answer > num:
        print '%d is too big!' %answer

    if answer == num:
        print 'BINGO!%d is the right answer!' %answer
        bingo = True
