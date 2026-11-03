import os
import csv
from datetime import datetime

TARGET_FOLDER = r"E:/AI-Learning/projects/week2"
OUTPUT_CSV = "projects/week5/result_2.csv"

def count_lines(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return sum(1 for line in f)
    except Exception as e:
        print(f"读取失败, 错误信息为: {e}")

def collect_py_files(folder):
    py_list = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.endswith(".py"):
                full_path = os.path.join(root, filename)
                py_list.append(full_path)
    return py_list

def save_to_csv(file_list, output_path):
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(['文件名', '行数', '完整路径'])
        for full_path in file_list:
            filename = os.path.basename(full_path)
            lines = count_lines(full_path)
            writer.writerow([filename, lines, full_path])

def save_time():
    now = datetime.now()
    time = now.strftime('%Y年%m月%d日 %H:%M:%S')
    return time

if __name__ == "__main__":
    print(f"开始遍历文件夹: {TARGET_FOLDER}")
    files = collect_py_files(TARGET_FOLDER)
    print(f"找到 {len(files)} 个 .py 文件")

    save_to_csv(files, OUTPUT_CSV)
    print(f"结果已保存到 {OUTPUT_CSV}")
    now_time = save_time()
    print(f"保存时间: {now_time}")

    print("\n后 8 个文件：")
    for fp in files[-1:-9:-1]:
        print(fp)
