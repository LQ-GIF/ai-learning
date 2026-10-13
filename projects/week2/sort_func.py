# ========== 练习1：*args 接收任意多个位置参数 ==========
def sum_years(*args):
    """
    接收任意多个建筑案例，计算它们的建成年份总和
    参数：
        *args: 任意多个建筑案例字典
    返回：
        建成年份总和
    """
    total = 0
    for case in args:
        total += int(case["建成年份"])
    return total


# ========== 练习2：**kwargs 接收任意多个关键字参数 ==========
def print_case_info(**kwargs):
    """
    接收任意多个关键字参数，打印建筑案例信息
    参数：
        **kwargs: 任意多个关键字参数 (如名称=..., 建筑师=...)
    """
    print("案例信息：")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# ========== 练习3：核心任务 - 用*args接收案例，按年份排序返回 ==========
def sort_cases_by_years(*ages, reverse=False):
    """
    接收任意多个建筑案例，按建成年份排序后返回
    参数：
        *args: 任意多个建筑案例字典
        reverse: 是否降序 (默认False=升序，从早到晚)
    返回：
        排序后的案例列表
    """
    sorted_cases = sorted(ages, key=lambda c: int(c["建成年份"]), reverse=reverse)
    return list(sorted_cases)

# ========== 练习4：用lambda写各种排序key ==========
def sort_demo(cases):
    print("\n--- 按建成年份升序（从早到晚）---")
    for c in sorted(cases, key=lambda c: int(c["建成年份"])):
        print(f"{c["建成年份"]}年 - {c["名称"]}")

    print("\n--- 按建成年份降序（从晚到早）---")
    for c in sorted(cases, key=lambda c: int(c["建成年份"]), reverse=True):
        print(f"{c["建成年份"]}年 - {c["名称"]}")

    print("\n--- 按建筑名称长度排序（名字短的在前）---")
    for c in sorted(cases, key=lambda c: len(c["名称"])):
        print(f"{len(c["名称"])}字 - {c["名称"]}")

    print("\n--- 按建筑师名字排序（字符串排序）---")
    for c in sorted(cases, key=lambda c: c["建筑师"]):
        print(f"{c["建筑师"]} - {c["名称"]}")

# ========== 主程序：测试所有功能 ==========
def main():
    print("=" * 45)
    print("  建筑案例排序工具 (可变参数+lambda+sorted)")
    print("=" * 45)
  
    case1 = {
        "名称": "流水别墅",
        "建筑师": "弗兰克·劳埃德·赖特",
        "地点": "美国宾夕法尼亚州",
        "建成年份": "1935",
        "建筑风格": "有机建筑"
    }
    case2 = {
        "名称": "萨伏伊别墅",
        "建筑师": "勒·柯布西耶",
        "地点": "法国巴黎",
        "建成年份": "1929",
        "建筑风格": "现代主义"
    }
    case3 = {
        "名称": "巴塞罗那德国馆",
        "建筑师": "路德维希·密斯·凡德罗",
        "地点": "西班牙巴塞罗那",
        "建成年份": "1929",
        "建筑风格": "现代主义"
    }
    case4 = {
        "名称": "光之教堂",
        "建筑师": "安藤忠雄",
        "地点": "日本大阪",
        "建成年份": "1989",
        "建筑风格": "极简主义"
    }
    case5 = {
        "名称": "苏州博物馆",
        "建筑师": "贝聿铭",
        "地点": "中国苏州",
        "建成年份": "2006",
        "建筑风格": "新中式"
    }
    case6 = {
        "名称": "蓬皮杜中心",
        "建筑师": "伦佐·皮亚特、理查德·罗杰斯",
        "地点": "法国巴黎",
        "建成年份": "1977",
        "建筑风格": "高技派"
    }

    cases_list = [case1, case2, case3, case4, case5, case6]

    # ===== 测试1：*args - 传入不同数量的案例，计算年份总和 =====
    print("\n【测试1】*args - 计算任意多个案例的年份总和")
    print(f"传入 1 个案例, 年份总和为{sum_years(case1)}")
    print(f"传入 2 个案例, 年份总和为{sum_years(case1, case2)}")
    print(f"传入 3 个案例, 年份总和为{sum_years(case1, case2, case3)}")
    print(f"传入 4 个案例, 年份总和为{sum_years(case1, case2, case3, case4)}")
    print(f"传入 5 个案例, 年份总和为{sum_years(case1, case2, case3, case4, case5)}")
    print(f"传入 6 个案例, 年份总和为{sum_years(case1, case2, case3, case4, case5, case6)}")

    # ===== 测试2：**kwargs - 传入任意多个关键字参数 =====
    print("\n【测试2】**kwargs - 打印任意多个关键字参数")
    print_case_info(名称="蓬皮杜中心", 建筑师="伦佐·皮亚特、理查德·罗杰斯", 建成年份="1977")
    print()
    print_case_info(地点="法国巴黎", 建筑风格="高技派")

    # ===== 测试3：核心任务 - *args接收任意多个案例，按年份排序 =====
    print("\n【测试3】核心任务 - 传入不同数量的案例，按建成年份升序排序")

    print("\n--- 传入2个案例 ---")
    result1 = sort_cases_by_years(case1, case2)
    for c in result1:
        print(f"  {c['建成年份']}年 - {c['名称']}")

    print("\n--- 传入4个案例 ---")
    result2 = sort_cases_by_years(case1, case2, case3, case4)
    for c in result2:
        print(f"  {c['建成年份']}年 - {c['名称']}")

    print("\n--- 传入5个案例, 降序 (从晚到早) ---")
    result3 = sort_cases_by_years(case1, case2, case3, case4, case5, reverse=True)
    for c in result3:
        print(f"  {c['建成年份']}年 - {c['名称']}")

    # ===== 测试4：各种排序方式演示 =====
    print("\n【测试4】各种排序方式演示 (lambda作为key)")
    sort_demo(cases_list)

    print("\n" + "=" * 45)
    print("  所有测试完成！")
    print("=" * 45)

if __name__ == "__main__":
    main()

    

def ave_num(*num, **kwargs):
    max_num = max(num)
    min_num = min(num)
    ave_num = sum(num) / len(num)

    if kwargs.get("round") is not None:
        ave_num = round(ave_num, kwargs.get("round"))

    return max_num, min_num, ave_num

def sort_num(*num, reverse=False):
    sorted_num = sorted(num, reverse=reverse)
    return list(sorted_num)


def sort_len_num(*num, reverse=False):
    sorted_len_num = sorted(num, key=lambda a: len(a), reverse=reverse)
    return list(sorted_len_num)

def main():
    print("=" * 25)
    print("  数字求和排序工具")
    print("=" * 25)

    print("\n====求最值/平均值功能====")
    max_result, min_result, ave_result = ave_num(2, 6, 3, 7, 89, 11, 20, 50, 101, round=1)
    print(f"该组数据的最大值为: {max_result}, 最小值为: {min_result}, 平均值为: {ave_result}") 

    print("\n====按数字大小排序功能====")
    num_list = sort_num(2, 6, 3, 7, 89, 11, 20, 50, 101)
    for i in num_list:
        print(i)

    print("\n====按数字长度排序功能====")
    num_list2 = sort_len_num("2", "6", "3", "7", "89", "11", "20", "50", "101", "2345", "123", "44323")
    for j in num_list2:
        print(j)

if __name__ == "__main__":
    main()


print("\n----------------------")
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def calc(x, y, open):
    return open(x, y)

print(calc(20, 30, add))
print(calc(10, 50, sub))

