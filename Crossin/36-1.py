#�ѿ��������쳣��������try-���У��Ѵ����쳣��������except-����
#try..except����У�try���������쳣�������ӳ���һֻ���̣���except����һֻ�����Ĺ���
#����׼ȷ�ؽ�ס����
try:
    f=file('non-exist.txt')
    print 'File opened!'
    f.close()
except:
    print 'File not exists.'
print 'Done'
