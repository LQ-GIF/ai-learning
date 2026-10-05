name = input("请输入你的名字：")
age = int(input("请输入你的年龄："))
next_year_age = age + 1
print(f"{name}, 你今年{age}岁, 明年{next_year_age}岁")

age = 24
add = 1
print("明年的年龄是：", age + add)
print("后年的年龄是：", age + add + add)

print(type(name))
print(type(age))

a = 3.14
b = True
c = False
d = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(isinstance(a, float))
print(isinstance(b, bool))
print(isinstance(c, bool))
print(isinstance(d, type(None)))
print(isinstance(name, str))
print(isinstance(age, int))

e, f = 20, 60
print("e + f 的值是：", e + f)

video_name = input("请输入视频名称：")
base = float(input("请输入基础播放量："))
incr = float(input("请输入新增播放量："))
next_play_count = base + incr
print(f"{video_name}, 基础播放量是{base}, 新增播放量是{incr}, 下一次播放量是{next_play_count}")