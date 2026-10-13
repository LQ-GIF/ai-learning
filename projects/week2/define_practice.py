# 定义一个函数，根据传入的分数，计算对应的分数等级并返回
def method_level(method):
    if method < 0 or method > 100:
        return "无效分数, 请输入 0-100 范围内的分数"
    else:
        if method >= 90:
            return "A"
        elif method >= 75:
            return "B"
        elif method >= 60:
            return "C"
        elif method < 60:
            return "D"

level = method_level(int(input("请输入你的分数: ")))
print(f"你的成绩等级为{level}")

# 定义一个函数，用于判断一个字符串是否是回文串，返回bool值
def c_string(s):
    if s == s[::-1]:
        return True
    else:
        return False

aba = c_string(input("请输入字符串: "))
print(f"是否为回文串: {aba}")

# 定义一个函数:完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def minute(s):
    min = round(s / 60, 3)
    hour(s)
    print(f"{s}秒为{min}分钟")

def hour(s):
    h = round(s / 3600, 5)
    print(f"{s}秒为{h}小时")

time = minute(int(input("请输入秒数: ")))

# 定义一个函数:根据传入的三角形三个边的边长，判定三角形的类型(等边、等腰、普通，或者不能构成三角形)
def triangle_judgment(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "不能构成三角形"
    else:
        if a == b and b == c:
            return "等边三角形"
        elif a == b or b == c or c == a:
            return "等腰三角形"
        else:
            return "普通三角形"

print(f"该三角形为{triangle_judgment(3, 4, 5)}")
