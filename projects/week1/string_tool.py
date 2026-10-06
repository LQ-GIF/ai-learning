# 对常用函数的练习
sentence = input("请输入一句话：")
length = len(sentence)
reversed_sentence = sentence[::-1]
intercepted_sentence = sentence[:4]
intercepted_sentence2 = sentence[4:8]
intercepted_sentence3 = sentence[:8:2]
reversed_sentence2 = sentence[-1:-10:-1]
reversed_sentence3 = sentence[-1:-10:-2]
replaced_sentence = sentence.replace("你", "您")
replaced_sentence2 = sentence.replace("Agent", "应用")
upper_sentence = sentence.upper()
lower_sentence = sentence.lower()
split_sentence = sentence.split(",")

print(f"你输入的话是：{sentence}")
print(f"字数统计：{length}个字符")
print(f"反转后：{reversed_sentence}")
print(f"截取前4个字符:{intercepted_sentence}")
print(f"截取第5到8个字符:{intercepted_sentence2}")
print(f"截取前8个字符中的每2个字符:{intercepted_sentence3}")
print(f"截取后10个字符进行反转:{reversed_sentence2}")
print(f"截取后10个字符中的每两个字符进行反转:{reversed_sentence3}")
print(f"把'你'替换成'您'后：{replaced_sentence}")
print(f"把'Agent'替换为'应用'后：{replaced_sentence2}")
print(f"大写后：{upper_sentence}")
print(f"小写后：{lower_sentence}")
print(f"分割后：{split_sentence}")
print("--------------------------------------------------------------------------------")
# 对 + 、占位符以及f-string格式化拼接字符串的练习
a = "你好"
b = "AI"
c = "Agent工程师"
d = 9
print(a + "," + b + " " + c + "! 学习AI" + str(d) + "天了。")
print("%s, %s %s! 学习AI%s天了。" % (a,b,c,d))
print(f"{a},{b} {c}! 学习AI{d}天了。")
print("--------------------------------------------------------------------------------")
# 对字符串定义以及转义字符的练习
s = 'it\'s very good'
s1 = "意思是\"它是非常好的\""
print(f"{s},{s1}")
print(f"{s},\n{s1}")
print(f"\t{s},\n{s1}")
s2 = """it's very good
\t意思是"它是非常好的"
"""
print(s2)