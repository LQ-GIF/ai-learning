import json
import os
import logging

# ========== 日志配置 ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("projects/week2/case_manager.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

DATA_FILE = "projects/week2/cases_v3.json"

# ========== 数据加载和保存 ==========
def load_data():
    if not os.path.exists(DATA_FILE):
        logging.warning(f"数据文件{DATA_FILE}不存在, 将创建新文件")
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            cases = json.load(f)
        logging.info(f"成功加载{len(cases)}条案例数据")
        return cases
    except json.JSONDecodeError:
        logging.error(f"数据文件{DATA_FILE}格式损坏, 将返回空列表")
        return []
    except Exception as e:
        logging.error(f"数据文件发生未知错误, 错误信息为: {e}")
        return []

def save_data(cases):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(cases, f, ensure_ascii=False, indent=2)
        logging.info(f"成功保存{len(cases)}条案例信息")
        return True
    except PermissionError:
        logging.error(f"保存失败, 没有权限写入文件{DATA_FILE}")
        return False
    except Exception as e:
        logging.error(f"保存数据时发生未知错误, 错误信息为: {e}")
        return False

# ========== 案例操作函数 ==========
def add_case(cases):
    print("\n--- 添加案例 ---")
    name = input("请输入建筑名称: ").strip()
    if not name:
        print("建筑名称不能为空")
        logging.warning("案例添加失败: 建筑名称为空")
        return cases
    else:
        architect = input("请输入建筑师: ").strip()
        year = input("请输入建成年份: ").strip()
        location = input("请输入地点: ").strip()
        style = input("请输入建筑风格: ").strip()

    new_case = {
        "名称": name,
        "建筑师": architect,
        "建成年份": year,
        "地点": location,
        "建筑风格": style
    }

    cases.append(new_case)
    logging.info(f"添加了新案例: {name}")
    print(f"案例「{name}」添加成功！")
    save_data(cases)
    return cases

def list_cases(cases):
    print("\n--- 案例列表 ---")
    if not cases:
        print("暂无案例数据！！！")
        return
    else:
        for i, case in enumerate(cases, 1):
            print(f"[{i}] {case['名称']} | 建筑师：{case['建筑师']} | 年份：{case['建成年份']} | 地点：{case['地点']} | 风格：{case['建筑风格']}")

def search_case(cases):
    print("\n--- 搜索案例 ---")
    keyword = input("请输入要搜索的建筑名称关键词: ").strip()
    if not keyword:
        logging.info("搜索失败: 关键词为空!!!")
        print("搜索关键词不能为空！")
        return
    else:
        found = False
        for i, case in enumerate(cases, 1):
            if keyword in case["名称"]:
                print(f"找到案例（序号[{i}]")
                print(f"  名称：{case['名称']}")
                print(f"  建筑师：{case['建筑师']}")
                print(f"  建成年份：{case['建成年份']}")
                print(f"  地点：{case['地点']}")
                print(f"  风格：{case['建筑风格']}")
                found = True
        if not found:
            print(f"未找到包含「{keyword}」的案例。")
            logging.info(f"搜索「{keyword}」：未找到匹配案例")
        else:
            logging.info(f"搜索「{keyword}」：找到匹配案例")

def delete_case(cases):
    print("\n--- 删除案例 ---")
    if not cases:
        print("暂无案例数据，无法删除。")
        return cases
    else:
        list_cases(cases)
        choice = input("请输入要删除的案例序号: ").strip()

        try:
            index = int(choice) - 1
            if index < 0 or index >= len(cases):
                print("序号超出范围！")
                logging.warning(f"删除案例失败, 序号{choice}超出范围")
                return cases
            else:
                deleted_name = cases[index]["名称"]
                cases.pop(index)
                logging.info(f"删除了案例：{deleted_name} (序号{choice})")
                print(f"案例「{deleted_name}」删除成功！")
                save_data(cases)
                return cases
        except ValueError:
            print("输入错误！请输入一个有效的数字序号。")
            logging.warning(f"删除案例失败：输入「{choice}」不是有效数字")
            return cases

# ========== 主程序 ==========
def main():
    logging.info("建筑案例管理系统 v3 启动")
    cases = load_data()

    while True:
        print("\n" + "=" * 40)
        print("  建筑案例管理系统 v3")
        print("  1. 添加案例")
        print("  2. 查看所有案例")
        print("  3. 搜索案例")
        print("  4. 删除案例")
        print("  5. 保存并退出")
        print("=" * 40)

        choice = input("请输入选项 (1 - 5): ").strip()

        try:
            option = int(choice)
        except ValueError:
            print("输入错误！请输入 1-5 之间的数字。")
            logging.warning(f"菜单输入错误：「{choice}」不是有效数字")
            continue

        if option == 1:
            cases = add_case(cases)
        elif option == 2:
            list_cases(cases)
        elif option == 3:
            search_case(cases)
        elif option == 4:
            cases = delete_case(cases)
        elif option == 5:
            if save_data(cases):
                print("数据已保存，再见！")
                logging.info("建筑案例管理系统 v3 正常退出")
            else:
                print("数据保存失败，但程序仍将退出。请检查日志文件了解详情。")
                logging.error("程序退出时数据保存失败")
            break
        else:
            print("选项超出范围！请输入 1-5 之间的数字。")
            logging.warning(f"菜单输入错误：选项 {option} 超出范围")

if __name__ == "__main__":
    main()
    