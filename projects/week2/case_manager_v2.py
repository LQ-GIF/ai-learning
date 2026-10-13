import json
import os

DATA_FILE = "case_v2.json"

# ========== 全局变量练习 ==========
operation_count = 0

# ========== 功能1：加载数据（有return，返回案例列表）==========
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# ========== 功能2：保存数据（无return，只做保存这件事）==========
def save_data(cases_v2):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cases_v2, f, ensure_ascii=False, indent=2)

# ========== 功能3：添加案例（有return，返回新案例；有默认参数style）==========
def add_case(cases_v2, name, architect, location, year, style="现代主义"):
    """
    添加一个建筑案例
    参数：
        cases_v2: 案例列表
        name: 建筑名称
        architect: 建筑师
        location: 地点
        year: 建成年份
        style: 建筑风格 (默认值"现代主义")
    返回：
        新添加的案例字典
    """
    global operation_count  # 声明要修改全局变量
    operation_count += 1    # 操作次数+1

    case = {
        "名称": name,
        "建筑师": architect,
        "地点": location,
        "建成年份": year,
        "建筑风格": style
    }
    cases_v2.append(case)
    save_data(cases_v2)
    return case  # 返回新添加的案例

# ========== 功能4：查询案例（有return，返回匹配的案例列表）==========
def search_case(cases_v2, keyword):
    """
    按关键词查询建筑案例
    参数：
        cases_v2: 案例列表
        keyword: 搜索关键词
    返回：
        匹配的案例列表（可能是空列表）
    """
    global operation_count
    operation_count += 1

    results = []
    for case in cases_v2:
        if keyword in case["名称"]:
            results.append(case)
    return results  # 返回匹配的案例列表

# ========== 功能5：删除案例（有return，返回被删除的案例或None）==========
def delete_case(cases_v2, index):
    """
    按编号删除案例
    参数：
        cases_v2: 案例列表
        index: 要删除的编号 (从1开始)
    返回：
        被删除的案例字典; 如果编号无效返回None
    """
    global operation_count
    operation_count += 1

    if 1 <= index <= len(cases_v2):
        deleted = cases_v2.pop(index - 1)
        save_data(cases_v2)
        return deleted  # 返回被删除的案例
    return None  # 编号无效，返回None

# ========== 功能6：统计案例数量（有return，返回数量）==========
def count_cases(cases_v2):
    """返回案例总数"""
    return len(cases_v2)

# ========== 主程序 ==========
def main():
    cases_v2 = load_data()
    print("=" * 35)
    print("  建筑案例信息管理系统 v2")
    print("  （函数重构版：返回值+默认参数）")
    print("=" * 35)

    while True:
        print("\n" + "-" * 35)
        print("请选择操作：")
        print("  1. 添加案例")
        print("  2. 查看所有案例")
        print("  3. 查询案例")
        print("  4. 删除案例")
        print("  5. 查看统计")
        print("  6. 退出")
        print("-" * 35)

        choice = input("请输入选项 (1-6): ")

        if choice == "1":
            # 添加案例：用input获取信息，然后调用add_case函数
            print("\n=== 添加建筑案例 ===")
            name = input("请输入建筑名称：")
            architect = input("请输入建筑师：")
            location = input("请输入地点：")
            year = input("请输入建成年份：")
            style_input = input("请输入建筑风格 (直接回车默认'现代主义'): ")

            # 调用add_case，练习默认参数和关键字参数
            if style_input == "":
                # 不传style，用默认值"现代主义"
                new_case = add_case(cases_v2, name, architect, location, year)
            else:
                # 用关键字参数传参（顺序可以随便写）
                new_case = add_case(
                    cases_v2=cases_v2,
                    name=name,
                    architect=architect,
                    location=location,
                    year=year,
                    style=style_input
                )
            print(f"✅ 已添加案例：{new_case['名称']}(风格：{new_case['建筑风格']})")

        elif choice == "2":
            # 查看所有案例
            print("\n=== 所有建筑案例 ===")
            if not cases_v2:
                print("（暂无案例，请先添加）")
            else:
                for i, case in enumerate(cases_v2, 1):
                    print(f"\n[{i}] {case['名称']}")
                    print(f"    建筑师：{case['建筑师']}")
                    print(f"    地点：{case['地点']}")
                    print(f"    建成年份：{case['建成年份']}")
                    print(f"    建筑风格：{case['建筑风格']}")

        elif choice == "3":
            # 查询案例：调用search_case，拿到返回的结果列表再显示
            print("\n=== 查询建筑案例 ===")
            keyword = input("请输入要查询的建筑名称关键词：")
            results = search_case(cases_v2, keyword)  # 函数返回匹配的列表
            if results:
                print(f"找到 {len(results)} 个匹配的案例：")
                for case in results:
                    print(f"  - {case['名称']} ({case['建筑师']}, {case['建成年份']}年)")
            else:
                print(f"❌ 未找到包含'{keyword}'的案例")

        elif choice == "4":
            # 删除案例
            print("\n=== 删除建筑案例 ===")
            if not cases_v2:
                print("（暂无案例）")
                continue
            # 先显示所有案例
            for i, case in enumerate(cases_v2, 1):
                print(f"  [{i}] {case['名称']}")
            try:
                index = int(input("请输入要删除的案例编号："))
                deleted = delete_case(cases_v2, index)  # 函数返回被删除的案例或None
                if deleted:
                    print(f"🗑️ 已删除案例：{deleted['名称']}")
                else:
                    print("❌ 编号无效")
            except ValueError:
                print("❌ 请输入有效的数字编号")

        elif choice == "5":
            # 查看统计：调用count_cases和全局变量operation_count
            print("\n=== 统计信息 ===")
            print(f"  案例总数：{count_cases(cases_v2)} 个")
            print(f"  本次运行操作次数：{operation_count} 次")

        elif choice == "6":
            print("\n👋 感谢使用，再见！")
            break

        else:
            print("❌ 无效选项, 请输入1-6之间的数字")

if __name__ == "__main__":
    main()