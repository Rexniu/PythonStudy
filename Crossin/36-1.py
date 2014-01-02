#把可能引发异常的语句放在try-块中，把处理异常的语句放在except-块中
#try..except语句中，try中引发的异常就像是扔出了一只飞盘，而except就是一只灵敏的狗，
#总能准确地接住飞盘
try:
    f=file('non-exist.txt')
    print 'File opened!'
    f.close()
except:
    print 'File not exists.'
print 'Done'
