#Ԫ�飺
postion = (1,2)
geeks = ('Sheldon','Leonard','Rajesh','Howard')

#Ԫ��(tuple)Ҳ��һ�����У������˺ܶ�ε�list���ơ���list��ͬ������������Ƭ�������Ȳ���
print postion[0]
for g in geeks:
    print g
print geeks[1:3]

print '%s is %d years old' % ('Mike',23)    #print���õ���Ԫ��


#Ԫ����Ϊ��������ֵ������
def get_pos(n):
    return (n/2,n*2)
#�õ���������ķ���ֵ��������ʽ
#1.���ݷ���ֵԪ����Ԫ�صĸ����ṩ����
x,y = get_pos(50)
print x
print y

#2.��һ��������¼���ص�Ԫ��
pos = get_pos(50)
print pos[0]
print pos[1]
