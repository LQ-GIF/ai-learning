"""
typed_funcs.py - W4 Day1 类型标注练习
练习: 函数参数标注、返回值标注、变量标注、List/Dict/Optional 类型
"""

# List / Dict / Optional 都要从 typing 导入
from typing import List, Dict, Optional

# List / Dict / Optional 都要从 typing 导入
def calculate_area(length: float, width: float) -> float:
    """计算矩形面积。

    参数:
        length: 长度（数字）
        width: 宽度（数字）
    返回:
        面积（数字）
    """
    return length * width

# 函数2：按年份筛选建筑案例（List[Dict], int -> List[Dict]）
def filter_cases_by_year(cases: List[Dict], min_year: int) -> List[Dict]:
    """筛选出建造年份不早于 min_year 的案例。

    参数:
        cases: 建筑案例字典列表
        min_year: 最早年份（整数）
    返回:
        符合条件的案例字典列表
    """
    result: List[Dict] = []
    for case in cases:
        if case['year'] >= min_year:
            result.append(case)
    return result

# 补充练习：按名称查找案例（Optional[Dict]：找到返回字典，找不到返回 None）
def filter_cases_by_name(cases: List[Dict], name: str) -> Optional[Dict]:
    """按名称查找案例，找不到时返回 None。"""
    for case in cases:
        if case['name'] == name:
            return case
    return None

# 按姓名查找成绩
def check_grades_by_name(report_card: List[Dict], name: str) -> Optional[Dict]:
    for student in report_card:
        if student['name'] == name:
            return student
    return None

# 按成绩筛选名单
def check_grades_by_grades(report_card: List[Dict], grades: float) -> List[Dict]:
    grades_result: List[Dict] = []
    for student in report_card:
        if student['grades'] >= grades:
            grades_result.append(student)
    return grades_result

if __name__ == "__main__":
    # 测试数据：变量标注 cases 是字典列表
    cases: List[Dict] = [
        {"name": "流水别墅", "year": 1935, "city": "美国宾夕法尼亚州"},
        {"name": "苏州博物馆", "year": 2006, "city": "苏州"},
        {"name": "朗香教堂", "year": 1955, "city": "法国"},
    ]

    report_card: List[Dict] = [
        {"name": "张三", "grades": 99.6},
        {"name": "李四", "grades": 58.2},
        {"name": "王五", "grades": 100.0},
        {"name": "赵六", "grades": 44.5},
        {"name": "钱七", "grades": 78.3},
        {"name": "孙悟空", "grades": 66.2},
        {"name": "猪八戒", "grades": 28.0},
        {"name": "哪吒", "grades": 40.8},
        {"name": "李世民", "grades": 81.1},
        {"name": "朱棣", "grades": 86.9}
    ]

    # 函数1 调用：area 标注为 float
    arer: float = calculate_area(12.5, 8.0)
    print(f"矩形面积: {arer}")

    # 函数2 调用：筛选 1960 年之后的案例
    recent: List[Dict] = filter_cases_by_year(cases, 1950)
    print(f"\n1960 年之后的案例 ({len(recent)}) 个")
    for i, case in enumerate(recent, 1):
        print(f"[{i}] {case['name']} ({case['year']}, {case['city']})")

    # 补充练习：找得到 / 找不到两种情况
    found: Optional[Dict] = filter_cases_by_name(cases, "苏州博物馆")
    print(f"\n查找「苏州博物馆」: {found}")

    missing: Optional[Dict] = filter_cases_by_name(cases, "故宫")
    print(f"\n查找「故宫」: {missing}")

    # 筛选 60 分以上的成绩名单
    qualified: List[Dict] = check_grades_by_grades(report_card, 60)
    print(f"\n60 分以上的同学有 ({len(qualified)}) 个")
    for j, student in enumerate(sorted(qualified, key=lambda r: r['grades'], reverse=True), 1):
        print(f"[{j}] {student['name']} - {student['grades']}")

    # 按照姓名查询成绩
    found1: Optional[Dict] = check_grades_by_name(report_card, "孙悟空")
    print(f"查询结果为: {found1}")

    