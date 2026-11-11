# 字符串五连
output = input("请输入一句话: ")

# 去掉所有空格后，统计输入字符串的长度
print("-" * 60)
str_count = output.replace(" ", "")  # 用 replace() 替换掉字符串中的空格
print(f"一共输入了 {len(str_count)} 个字")

#把句子里所有 "建筑" 替换成 "设计"
print("-" * 60)
str_replace = output.replace("建筑", "设计")   # # 用 replace() 将字符串中的"建筑"替换为"设计"
print(f"替换后输出: {str_replace}")

# 反转输入的字符串
print("-" * 60)
str_reverse = output[::-1]    # 用切片中的步长来反转字符串
print(f"反转后的结果为: {str_reverse}")

# 按空格 split() 成列表，再用 "-" join() 起来
print("-" * 60)
str_list = output.split()  #把输入的句子按空格拆分为列表
result = "-".join(str_list) # 用 "'-'.join()" 把列表中的字符串用 "-" 连起来
print(f"分隔后的列表为: {str_list}")
print(f"连接后的结果为: {result}")

# 取这句话的前 5 个字和后 5 个字
print("-" * 60)
front = output[:5]    
after = output[-5:]   # ** output[-1:-6:-1] 取出来的数据虽然是最后 5 个，但是输出的是倒序；**
                      # ** 要正序输出最后 5 个数据，应该是 output[-5:],它的含义是从索引位置为 -5 的数据开始，一直取到最后一个数据 **
print(f"输入字符串的前 5 个字为: {front}, 后 5 个字为: {after}")


# 九九乘法表
print("\n", "=" * 60)
print("九九乘法表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} x {j} == {i * j}", end="  ")  # end="  " 意思是输出结果以空格结尾
    print() # 此处 "print()" 起到换行作用

# 循环控制
# A: 求 1 到 100 之间所有能被 3 整除的数的和，但跳过所有能被 5 整除的数（用 continue），打印结果。
print("\n", "=" * 60)
print("循环控制(A)")
num = []  # 创建空列表
for a in range(1, 101):  # 遍历 1 - 100 的所有整数
    if a % 5 == 0:  
        continue
    elif a % 3 == 0:
        num.append(a)
total = sum(num)
print(f"1 到 100 之间所有能被 3 整除的数的和为: {total}")

# B: 从 1 开始往上数，找到第一个同时满足 "能被 7 整除" 且 "大于 50" 的数就立刻停下（用 `break`），打印这个数。
print("-" * 60)
print("循环控制(B)")
for b in range(1, 101):
    if b > 50 and b % 7 == 0:
        print(f"能被 7 整除且大于 50 的数为：{b}")
        break
    else:
        continue

# 字典计数
print("\n", "=" * 60)
print("字典计数")
str_dict = {}
for s in str_count:
    str_dict[s] = str_dict.get(s, 0) + 1  #这里用到了添加/修改字典数据的方法（str_dict["键"] = 值） 
                                          # str_dict.get(s, 0) 的意思为，获取字典 str_dict 中 s 的值，如果 s 不存在，则返回 0 
"""
for s in str_count:
    if s in str_dict:
        str_dict[s] += 1
    else:
        str_dict[s] = 1
"""
for st, count in str_dict.items():  # str_dict.items() 获取该字典中的所有键值对
    if count >= 2:
        print(f" '{st}' 出现了 {count} 次")