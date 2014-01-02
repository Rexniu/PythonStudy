#dictionary
#基本格式：key 键，value 值
#1.键必须是唯一的
#2.键只能是简单对象，比如字符串/整数/浮点数/bool值

score = {
    '萧峰':95,
    '段誉':97,
    '虚竹':89
    }


print score['段誉']  #如果键是字符串，通过键访问的时候就需要加引号，如果是数字作为键则不用。


for name in score:
    print score[name]

score['虚竹'] = 91   #改变每一项的值

score['慕容复'] = 88  #增加一项字典项

del score['萧峰']  #必须是字典中的键
