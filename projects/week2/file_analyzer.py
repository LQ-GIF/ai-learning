# file_analyzer.py - 文件分析工具
# 功能：读取一个txt文件，统计字数、行数、词频最高的5个词，结果写入新文件
import re

def analyze_file(input_file, output_file):

    # ========== 第一步：读取文件 ==========
    print(f"正在读取文件: {input_file}")

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.splitlines()

    # ========== 第二步：统计基本信息 ==========
    total_chars = len(content)
    total_lines = len(lines)
    non_empty_lines = len([l for l in lines if l.split()])
    chinese_chars = len([c for c in content if '\u4e00' <= c <= '\u9fff'])

    print(f"总字数: {total_chars}")
    print(f"总行数: {total_lines}")
    print(f"非空行数: {non_empty_lines}")
    print(f"中文字数: {chinese_chars}")

    # ========== 第三步：统计词频 ==========
    print("\n正在统计词频...")

    words = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z]+', content)
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    top5 = sorted_words[:5]

    print("词频最高的5个词: ")
    for i, (word, count) in enumerate(top5, 1):
        print(f"第{i}名: {word}(出现{count}次)")

    # ========== 第三步：统计最长一行和最短一行 ========== 
    non_empty_lines1 = [l for l in lines if l.split()]
    sorted_lines = sorted(non_empty_lines1, key=lambda l: len(l), reverse=True)
    lines_top5 = sorted_lines[:3]
    print("字数最长的3行: ")
    for j, line in enumerate(lines_top5, 1):
        print(f"第{j}名: {line}({len(sorted_lines[j - 1])}字)")
    print(f"最长的一行共有{len(sorted_lines[0])}字, 内容是: {sorted_lines[0]}")
    print(f"最短的一行共有{len(sorted_lines[-1])}字, 内容是: {sorted_lines[-1]}")
    
    
    # ========== 第四步：把结果写入输出文件 ==========
    print(f"正在写入结果到: {output_file}")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("文件分析报告\n")
        f.write("=" * 40 + "\n")

        f.write(f"分析文件: {input_file}\n\n")

        f.write("--- 基本统计---\n")
        f.write(f"总字符数: {total_chars}\n")
        f.write(f"总行数: {total_lines}\n")
        f.write(f"非空行数: {non_empty_lines}\n")
        f.write(f"中文字数: {chinese_chars}\n")

        f.write(f"---词频最高的5个词---\n")
        for i, (word, count) in enumerate(top5, 1):
            f.write(f"第{i}名: {word}(出现{count}次)\n")

        f.write(f"---字数最长的3行---\n")
        for j, line in enumerate(lines_top5, 1):
            f.write(f"第{j}名: {line}({len(sorted_lines[j - 1])}字)\n")

        f.write(f"---最长一行和最短一行---\n")
        f.write(f"最长的一行共有{len(sorted_lines[0])}字, 内容是: {sorted_lines[0]}\n")
        f.write(f"最短的一行共有{len(sorted_lines[-1])}字, 内容是: {sorted_lines[-1]}\n")

        f.write("\n" + "=" * 40 +"\n")
        f.write("  分析完成\n")
        f.write("=" * 40 + "\n")

    print("写入完成")

# ========== 主程序 ==========
if __name__ == "__main__":
    input_file = "projects/week2/test.txt"
    output_file = "projects/week2/result.txt"

    print("=" * 45)
    print("  文件分析工具")
    print("=" * 45)

    analyze_file(input_file, output_file)

    print("\n" + "=" * 45)
    print(f"分析结果已保存到{output_file}")
    print("=" * 45)
