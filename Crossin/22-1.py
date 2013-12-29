def isEqual(num1,num2):
    if num1<num2:
        print '%d is too small!' %num1
        return False;
    if num1>num2:
        print '%d is too big!' %num1
        return False;
    if num1==num2:
        print 'Bingo!%d is the right answer!' %num1
        return True;

from random import randint
num = randint(1,100)
print 'Guess the number I think?'
bingo = False
while bingo == False:
    answer = input()
    bingo = isEqual(answer,num)
