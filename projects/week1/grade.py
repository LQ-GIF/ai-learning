# 成绩等级判断
score_input = float(input("请输入你的分数(0-100):"))
if score_input < 0 or score_input > 100:
    print("输入错误! 分数必须在0-100之间")
else:
    if score_input >= 90:
        print("优秀")
    elif score_input >= 80:
        print("良好")
    elif score_input >= 60:
        print("及格")
    elif score_input < 60:
        print("不及格")


# 登陆系统
account_information = {"abc123":123456, "def456":789987, "cab234":135791, "qcq171":456321}
account = input("请输入您的账号")
keys = int(input("请输入您的密码"))

if account in account_information and account_information[account] == keys:
    print("登陆成功! 欢迎使用")
else:
    print("登陆失败! 账号或密码输入错误")

# 三边是否能组成三角形
a = int(input("请输入第一个边的长度"))
b = int(input("请输入第二个边的长度"))
c = int(input("请输入第三个边的长度"))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("该三角形是等边三角形")
    elif a == b or b == c or a == c :
        print("该三角形是等腰三角形")
    else:
        print("该三角形是普通三角形")
else:
    print(f"{a}, {b}, {c}三条边不构成三角形")

# 算数运算符
print("===算数运算符===")
print(5 + 8)
print(5 - 8)
print(5 * 8)
print(5 / 8)
print(5 // 8)
print(5 % 8)
print(5 ** 2)

print("===比较运算符===")
print(5 == 8)
print(5 != 8)
print(5 > 8)
print(5 < 8)
print(5 >= 8)
print(5 <= 8)

print("===逻辑运算符===")
print(5 == 8 and 8 == 8)
print(5 == 8 or 8 == 8)
print(not 5 > 8)

print("===成员运算符===")
print(5 in (5, 6, 7, 8))
print(5 not in (5, 6, 7, 8))
