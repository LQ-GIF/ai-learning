with open("projects/week2/copy.txt", "r+", encoding="utf-8") as f:
    f.write("最新写入内容")

with open("projects/week2/copy.txt", "a", encoding="utf-8") as f:
    f.write("\n分析完成日期: 2026/10/16")
