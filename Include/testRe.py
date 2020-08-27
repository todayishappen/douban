# 正则表达式
import re

# 创建模式对象
pat= re.compile("AA") # 此时的正则表达式，用来验证其他的字符串

m =pat.search("CBA") # search是被校验的内容，
print(m) # None
m =pat.search("CBAA")
print(m) # 因为为左闭右开空间，所以为（2,4）//<re.Match object; span=(2, 4), match='AA'>
m =pat.search("CBAADCCBBAA") # span=(2,4),search只会显示第一个AA的位置

# 无模式对象
m = re.search("asd","ABasd") # 规则，内容
print(m) # <re.Match object; span=(2, 5), match='asd'>

print(re.findall("a","ASDaHUHa")) #['a', 'a'] ,找到所有符合规则的放进列表
print(re.findall("[A-Z]+?","ASDaHUHa")) #['A', 'S', 'D', 'H', 'U', 'H']非贪婪模式
print(re.findall("[A-Z]+","ASDaHUHa")) #['ASD', 'HUH']贪婪模式

# sub
print(re.sub("a","A","asddsafd")) # 在字符串中找到小a，用大A替换

#建议在正则表达式中被比较的字符串中前加上 r ，不用担心转义字符错误
a=r"\aabd-\'"
print(a) # \aabd-\'