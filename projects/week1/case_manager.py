import json
import os
DATA_FILE = "cases.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open (DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

def save_data(cases):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cases, f, ensure_ascii=False, indent=2)

def add_case(cases):
    name = input("请输入建筑名称：")
    architect = input("请输入建筑师：")
    location = input("请输入地点：")
    year = input("请输入建成年份：")
    style = input("请输入建筑风格：")
    case = {
        "名称":name, 
        "建筑师":architect, 
        "地点":location, 
        "建成年份":year, 
        "建筑风格":style
    }
    cases.append(case)
    save_data(cases)
    print(f"已添加案例：{name}")

def list_cases(cases):
    print("\n===所有建筑案例===")
    if not cases:
        print("(暂无案例, 请先添加)")
        return
    for i, case in enumerate(cases, 1):
        print(f"\n[{i}] {case['名称']}")
        print(f"    建筑师：{case['建筑师']}")
        print(f"    地点：{case['地点']}")
        print(f"    建成年份：{case['建成年份']}")
        print(f"    建筑风格：{case['建筑风格']}")

def search_case(cases):
    print("\n===查询建筑案例===")
    keyword = input("请输入要查询的建筑名称关键词：")
    found = False
    for case in cases:
        if keyword in case["名称"]:
            print(f"\n✅ 找到案例：{case['名称']}")
            print(f"    建筑师：{case['建筑师']}")
            print(f"    地点：{case['地点']}")
            print(f"    建成年份：{case['建成年份']}")
            print(f"    建筑风格：{case['建筑风格']}")
            found = True
    if not found:
        print(f"❌ 未找到包含'{keyword}'的案例")

def delete_cases(cases):
    print("\n=== 删除建筑案例 ===")
    list_cases(cases)
    if not cases:
        return
    try:
        index = int(input("请输入要删除的案例编号："))
        if 1 <= index >= len(cases):
            deleted = cases.pop(index - 1)
            save_data(cases)
            print(f"🗑️ 已删除案例：{deleted['名称']}")
        else:
            print("❌ 编号无效，请输入有效的编号")
    except ValueError:
        print("❌ 请输入有效的数字编号")

def main():
    cases = load_data()
    print("=" * 30)
    print("  建筑案例信息管理系统")
    print("=" * 30)
    while True:
        print("\n" + "-" * 30)
        print("请选择操作：")
        print("  1. 添加案例")
        print("  2. 查看所有案例")
        print("  3. 查询案例")
        print("  4. 删除案例")
        print("  5. 退出")
        print("-" * 30)

        choice = input("请输入选项(1-5): ")
        if choice == "1":
            add_case(cases)
        elif choice == "2":
            list_cases(cases)
        elif choice == "3":
            search_case(cases)
        elif choice == "4":
            delete_cases(cases)
        elif choice == "5":
            print("\n👋 感谢使用，再见！")
            break  # 跳出循环，程序结束
        else:
            print("❌ 无效选项, 请输入1-5之间的数字")

if __name__ == "__main__":
    main()