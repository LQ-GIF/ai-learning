print("===九九乘法表===")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}", end="    ")
    print()

print("\n===1 到 100 的偶数和===")
# for + if
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)

# for + 步长
total1 = 0
for i in range(2, 101, 2):
    total1 += i
print(total1)

# while 循环
total2 = 0
num = 2
while num <= 100:
    total2 += num
    num += 2
print(total2)

print("\n===打印等腰直角三角形===")
long = int(input("请输入边长： "))
for i in range(long):
    for j in range(i + 1):
        print("*", end="  ")
    print()

# 数字式
num = int(input("请输入边长："))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end="  ")
    print()


print("\n===打印国际象棋棋盘===")

for i in range(1, 9):
    for j in range(1, 9):
        if i % 2 == 0:
            if j % 2 == 0:
                print("黑", end="  ")
            else:
                print("白", end="  ")
        else:
            if j % 2 == 0:
                print("白", end="  ")
            else:
                print("黑", end="  ")
    print()

print("\n第二种写法")

for i in range(1, 9):
    if i % 2 == 0:
        for j in range(1, 9):
            if j % 2 == 0:
                print("黑", end="  ")
            else:
                print("白", end="  ")
        print()
    else:
        for j in range(1, 9):
            if j % 2 == 0:
                print("白", end="  ")
            else:
                print("黑", end="  ")
        print()

print("\n===登陆系统===")
while True:
    account_information = {"lq123":20030115, "abc123":123456, "def456":789987, "bca234":432567}
    username = input("请输入您的账号：")
    keys = int(input("请输入您的密码："))
    if username in account_information and account_information[username] == keys:
        print("登陆成功")
        break
    else:
        print("登陆失败")

print("\n===登陆系统(加入冻结系统)===")
d = 1
while d <= 5:
    account_information1 = {"lq123":20030115, "abc123":123456, "def456":789987, "bca234":432567}
    username1 = input("请输入您的账号：")
    keys1 = int(input("请输入您的密码："))
    if username1 in account_information1 and account_information1[username1] == keys1:
        print("登陆成功")
        break
    else:
        print("登陆失败")
    d += 1
    continue
print("失败5次, 系统冻结")

print("\n===计算器(match 模式匹配)===")
num1 = float(input("请输入第一个数字： "))
num2 = float(input("请输入第二个数字： "))
oper = input("请输入运算符(+, -, *, /, %, //, **): ")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    case "%":
        print(f"{num1} % {num2} = {num1 % num2}")
    case "//":
        print(f"{num1} // {num2} = {num1 // num2}")
    case "**":
        print(f"{num1} ** {num2} = {num1 ** num2}")
    case _:
        print("操作不支持")