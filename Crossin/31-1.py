f = file('31-text.txt')
f2 = file('31-text.txt')
f3 = file('31-text.txt')
data = f.read()   
print data
dataline = f2.readline() #��ȡһ������
print dataline
datalines = f3.readlines()   #�����ݰ��ж�ȡ֮һ��list��
print datalines
f.close()
