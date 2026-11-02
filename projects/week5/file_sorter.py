"""
文件行数统计工具
遍历指定文件夹，统计所有 .py 文件的行数，结果保存为 CSV
"""

import os
import csv

# ========== 第 1 步：定义要遍历的文件夹路径 ==========
# 你想统计哪个文件夹，就改成哪个路径
# 用 r"" 是为了让 Windows 路径里的 \ 不被转义
TARGET_FOLDER = r"E:/AI-Learning/projects/week3"
OUTPUT_CSV = "result.csv"

# ========== 第 2 步：写一个函数统计单个文件的行数 ==========
def count_lines(file_path):
    """读取一个文件，返回它有多少行"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # 用生成器表达式逐行计数，大文件也不占内存
            return sum(1 for line in f)
    except Exception as e:
        print(f"读取失败{file_path}, 错误信息: {e}")
        return 0

def collect_py_files(folder):
    """遍历 folder, 返回所有 .py 文件的完整路径列表"""
    py_files = []
    # os.walk 每次返回三元组：(当前文件夹路径, 子文件夹列表, 文件列表)
    for root, dirs, files in os.walk(folder):
        for filename in files:
            # 判断是不是 .py 文件
            if filename.endswith(".py"):
                # 拼成完整路径：E:\xxx\week4\area.py
                full_path = os.path.join(root, filename)
                py_files.append(full_path)
    return py_files

# ========== 第 4 步：把结果写入 CSV ==========
def save_to_csv(file_list, output_path):
    """把文件列表和行数写入 CSV 文件"""
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        # 创建 csv.writer 对象
        writer = csv.writer(f)
        # 先写表头
        writer.writerow(["文件名", "行数", "完整路径"])
        # 逐个写数据行
        for full_path in file_list:
            filename = os.path.basename(full_path)  # 只要文件名，不要路径
            lines = count_lines(full_path)  # 调用函数统计行数
            writer.writerow([filename, lines, full_path])

# ========== 第 5 步：主流程 ==========
if __name__ == "__main__":
    print(f"开始遍历文件夹: {TARGET_FOLDER}")
    files = collect_py_files(TARGET_FOLDER)
    print(f"找到 {len(files)} 个 .py 文件")

    save_to_csv(files, OUTPUT_CSV)
    print(f"结果已保存到 {OUTPUT_CSV}")

    # 顺便打印前几个文件看看
    print("\n前 5 个文件：")
    for fp in files[:5]:
        print(f"  {os.path.basename(fp)} {count_lines(fp)}行")
