from random import randint
f = open('E:/Python/Crossin/39/game.txt ')      #���ߣ�E:\\Python\\Crossin\\39\\game.txt
score = f.read().split()
f.close()
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

if game_times>0:
    avg_times = float(total_times)/game_times #��total_timesǰ������float������ת���˸����������ٽ��г������㡣�������������������������Ľ����Ĭ��Ϊ���������Ҳ����������롣
else:
    avg_times = 0
print '���Ѿ�����%d�Σ�����%d�ֲ³��𰸣�ƽ��%.2f�ֲ³���' % (game_times,min_times,avg_times)

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
