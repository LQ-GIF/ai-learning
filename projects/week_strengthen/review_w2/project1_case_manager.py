import os
import json
DATA_FILE = "cases_test.json"

def load_cases():
    """读取 JSON 文件，返回案例列表。
    要求:
    - 文件不存在 → 返回 []，并打印"暂无数据文件，已创建空列表"
    - 文件内容不是合法 JSON → 捕获异常，返回 []，打印"数据文件格式错误，已忽略"
    """
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            print("暂无数据文件，已创建空列表")
            return []
    except json.JSONDecodeError:
        print("数据文件格式错误，已忽略")
        return []
    except Exception as e:
        print(f"未知错误, 错误信息: {e}")
        return[]

def save_cases(cases_test):
    """把案例列表写入 JSON 文件。
    要求: 中文不转义、缩进 2 格，用 with open
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cases_test, f, ensure_ascii=False, indent=2)

def add_case(cases_test):
    """往列表里追加一条案例字典，返回追加后的新列表。
    字典结构：{"name":..., "city":..., "area": 数字, "type":...}
    """
    case_info = input("请按 (案例名称,城市,面积,类型) 的顺序依次输入案例信息: ").split(",")
    a = case_info[2].isdigit()
    if not a:
        print("输入的面积必须为数字")
    else:
        case = {
            "name": case_info[0],
            "city": case_info[1],
            "area": int(case_info[2]),
            "case_type": case_info[3]
        }
        cases_test.append(case)
    save_cases(cases_test)
    return cases_test

def filter_cases(cases_test, **conditions):
    """按任意字段筛选，返回筛选后的列表。
    例如: filter_cases(cases_test, city="杭州")
         filter_cases(cases_test, city="杭州", type="商业")
    要求：字段名和字典的键一致才匹配；没传条件就返回全部
    """
    
    results = cases_test
    if not conditions:
        return results
    for key, value in conditions.items():
        if key == "name":
            results = [c for c in results if value in c['neme']]
        elif key == "city":
            results = [c for c in results if value == c['city']]
        elif key == "area":
            results = [c for c in results if value <= c['area']]
        elif key == "case_type":
            results = [c for c in results if value == c['case_type']]
    for j, r in enumerate(results, 1):
        print(f"[{j}]  {r['name']} | {r['city']} | {r['area']} | {r['case_type']}")
    return results



def sort_cases(cases_test, by="area", reverse=False):
    """按指定字段排序，返回排序后的列表（不改原列表）。
    提示: sorted + lambda
    """
    sort_list = sorted(cases_test, key=lambda r: r[by], reverse=reverse)
    for i, c in enumerate(sort_list[:3], 1):
        print(f"[{i}]  {c['name']} | {c['city']} | {c['area']} | {c['case_type']}")
    return sort_list



if __name__ == "__main__":
    cases_test = load_cases()   # 调用 load_cases() 读一次

    print()
    
    for i in range(1):          # 用 input() 循环录入 3 条（格式 名称,城市,面积,类型，英文逗号）
        add_case(cases_test)
    
    print()   

    save_cases(cases_test)      # 调用 save_cases() 存盘

    print()
    print("再次读取案例数据")
    print(f"读回 {len(load_cases())} 个案例信息")# 重新调用 load_cases() 再读一遍，打印 “读回 X 条”，确认数据真的落到文件里了

    print()   
    print("地址在杭州的案例")
    filter_cases(cases_test, city="杭州") # 调用 filter_cases(cases, city="杭州")，打印杭州的案例

    print()
    print("按面积从大到小排名前三的案例")
    sort_cases(cases_test, reverse=True) # 调用 `sort_cases(cases, by="area", reverse=True)`，打印面积从大到小的前 3 条（带序号）
    


