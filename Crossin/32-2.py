f = file('output.txt')
data = f.read()
output = open('jieshou.txt','w')
output.write(data)
output.close()
f.close()
out = file('jieshou.txt')
txt = out.read()
print txt
