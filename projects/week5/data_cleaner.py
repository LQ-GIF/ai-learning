"""
CSV数据清洗工具
1. 去重（完全相同的行只保留一条）
2. 去空行（案例名为空的行删掉）
3. 去特殊字符（名字里的换行符、前后空格）
"""

import csv

def clean_name(name):
    """清洗单个案例名：去掉前后空格、去掉换行符\\n和制表符\\t"""
    name = name.strip()                   # 去掉前后空格
    name = name.replace("\n", "")         # 去掉换行符
    name = name.replace("\t", "")         # 去掉制表符
    return name

def clean_csv(input_path, output_path):
    # 1. 读脏数据
    with open(input_path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]        # 表头
    rows_data = rows[1:]    # 数据行

    print(f"清洗前 {len(rows_data)} 行数据")

    # 2. 去特殊字符 + 去空行
    cleaned = []
    for row in rows_data:
        if len(row) < 2:      # 行不完整（没有面积列）
            continue
        name = clean_name(row[0])
        area = row[1].strip()
        if name == "":        # 案例名为空，删掉
            continue
        cleaned.append([name, area])

    # 3. 去重（用集合，把行转成元组）
    seen = set()
    unique = []
    for row in cleaned:
        key = tuple(row)
        if key not in seen:
            seen.add(key)
            unique.append(row)
    print(f"清洗后：{len(unique)} 行数据")

    # 4. 写干净数据
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(unique)

def main():
    clean_csv("projects/week5/dirty_data.csv", "projects/week5/clean_data.csv")
    print("已清洗并保存到 clean_data.csv")

if __name__ == "__main__":
    main()