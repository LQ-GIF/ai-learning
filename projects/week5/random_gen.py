"""
随机建筑案例名称生成器
从前缀、风格、主体、后缀四个词库随机组合, 生成10个不重复的案例名
"""

import random
import csv

# ========== 词库 ==========
prefixes = ["现代", "极简", "新中式", "工业风", "轻奢", "自然", "复古", "未来感"]
styles  = ["", "简约", "高级", "温暖", "冷调"]          # 风格可以为空（不拼）
buildings = ["别墅", "咖啡馆", "图书馆", "美术馆", "幼儿园", "办公楼", "书店", "餐厅"]
suffixes = ["设计", "改造", "翻新", "扩建", "更新"]

# ========== 生成10个不重复的案例名 ==========
def generate_names(n=10):
    names = set()       # 用集合自动去重
    while len(names) < n:
        prefix = random.choice(prefixes)
        style = random.choice(styles)
        building = random.choice(buildings)
        suffix = random.choice(suffixes)
        name = prefix + style + building + suffix
        names.add(name)
    return list(names)

# ========== 保存到CSV ==========
def save_to_csv(names, output_path="projects/week5/random_cases.csv"):
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(['序号', '案例名称', '建筑面积(㎡)'])
        for i, name in enumerate(names, 1):
            area = random.randint(100, 2000)      # 随机面积100-2000㎡
            writer.writerow([i, name, area])

# ========== 主流程 ==========
if __name__ == "__main__":
    print("生成随机建筑案例名称：")
    cases = generate_names(10)
    for i, name in enumerate(cases, 1):
        print(f"  {i}. {name}")
    save_to_csv(cases)
    print(f"\n已保存到 random_cases.csv")