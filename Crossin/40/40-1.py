from random import randint
f = open('E:/Python/Crossin/40/game.txt ')      #���ߣ�E:\\Python\\Crossin\\39\\game.txt
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
times = 0 #��¼������Ϸ����
print 'Guess what I think!'
bingo = False
while bingo == False:
    times += 1   #����+1
    answer = input()
    if answer < num:
        print 'too small'
    if answer > num:
        print 'too big'
    if answer == num:
        print 'BINGO!'
        bingo = True

#����ǵ�һ���棬������������С�����٣��������С����
if game_times == 0:
    min_times = times
if game_times == 0 or times < min_times:
    min_times = times
total_times += times #����Ϸ��������
game_times += 1 #��Ϸ��������
print times
print min_times
result = '%d %d %d' %(game_times,min_times,total_times)
f = open('E:/Python/Crossin/40/game.txt','w')
f.write(result)
f.close()
