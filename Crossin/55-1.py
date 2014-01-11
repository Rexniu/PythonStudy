import re
text = "Hi, I am Shirley Hilton. I am his wife."
m = re.findall(r"hi", text)
if m:
    print m
else:
    print 'not match'

#如果我们只想找到“hi”这个单词，而不把包含它的单词也算在内，那就可以使用“\bhi\b”这个正则表达式。
#“\b”在正则表达式中表示单词的开头或结尾，空格、标点、换行都算是单词的分割。
#而“\b”自身又不会匹配任何字符，它代表的只是一个位置。所以单词前后的空格标点之类不会出现在结果里。
#上面的列子，“\bhi\b”匹配不到任何结果。但“\bhi”的话就可以匹配到1个“hi”，出自“his”。
#在正则表达式中，[]表示满足括号中任一字符。比如“[hi]”，它就不是匹配“hi”了，而是匹配“h”或者“i”。
