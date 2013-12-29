def isEqual(num1,num2):
    if num1<num2:
        print '%d is too small!' %num1
        return False;
    elif num1>num2:
        print '%d is too large!' %num1
        return False;
    elif num1==num2:
        print '%d is the correct answer!' %num1
        return True;

from random import randint
num = randint(1,100)
print 'Guess the number I thought,it\'s a integer'
bingo = False
while bingo == False:
    answer = input()
    bingo = isEqual(answer,num)
    
