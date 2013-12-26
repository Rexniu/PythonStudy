from random import randint
num = randint(1,100)

print 'please input a number!'
bingo = False

while bingo == False:
    answer = input()

    if answer < num:
        print 'too small!'

    if answer > num:
        print 'too big!'

    if answer == num:
        print 'BINGO!'
        bingo = True
    
