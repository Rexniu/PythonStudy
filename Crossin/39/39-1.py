from random import randint
f = open('E:/Python/Crossin/39/game.txt ')      #或者：E:\\Python\\Crossin\\39\\game.txt
score = f.read().split()
f.close()
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

if game_times>0:
    avg_times = float(total_times)/game_times #在total_times前加上了float，把它转成了浮点数类型再进行除法运算。如果不这样做，两个整数相除的结果会默认为整数，而且不是四舍五入。
else:
    avg_times = 0
print '你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (game_times,min_times,avg_times)

num = randint(1,100)
print 'Guess what I think!'
bingo = False
while bingo == False:
    answer = input()
    if answer < num:
        print 'too small'
    if answer < num:
        print 'too big'
    if answer == num:
        print 'BINGO!'
        bingo = true
