"""数据层: 从CSV读案例、导出筛选结果到CSV"""

import csv
from datetime import datetime

def load_case(csv_path="cases.csv"):
    """从CSV读取所有案例, 返回列表"""
    cases = []
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['面积'] = int(row["面积"])
            cases.append(row)
    return cases

def export_result(results, output_path="projects/week5/output_case.csv"):
    """把筛选结果导出到CSV, 带时间戳"""
    now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(['序号','案例名', '城市', '类型', '面积(㎡)'])
        for i, c in enumerate(results, 1):
            writer.writerow([i, c['案例名'], c['城市'], c['类型'], c['面积']])
    print(f"已导出 {len(results)} 条结果到 {output_path}(导出时间: {now})")