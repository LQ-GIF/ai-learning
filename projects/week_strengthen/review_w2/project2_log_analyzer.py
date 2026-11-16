def read_log(path="access.log"):
    """
    读取日志，返回【每条日志按空格切分后的字段列表】。
    例：[["2026-11-12", "09:01:23", "INFO", "用户", "张三", "登录成功"], ...]
    注意：返回的不是原始行字符串。
    """
    result = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                line_list = line.strip().split()
                if not line_list:
                    print(f"第 {i} 行为空行, 已忽略")
                    continue
                if len(line_list) < 4:
                    print(f"第 {i} 行日志内容出现数据缺失, 请返回日志文件核对")
                    continue
                result.append(line_list)
        return result


    except FileNotFoundError:
        print("日志文件不存在")
        return []
    except Exception as e:
        print(f"未知错误, 错误信息为: {e}")
        return[]


def count_levels(lines):
    """统计 INFO / WARN / ERROR 各多少条，返回字典。
    返回格式: {"INFO": 5, "WARN": 3, "ERROR": 2}
    """
    levels = {}
    for line in lines:
        levels[line[2]] = levels.get(line[2], 0) + 1
    return levels


def filter_level(lines, level):
    """筛出指定级别的行，返回列表。
    提示: filter + lambda
    """
    if not level:
        return lines[:]
    else:
        return list(filter(lambda line: line[2] == level, lines))

    """
    filter 用法:
    list(filter(lambda x: 条件, 筛选对象))
    从筛选对象中找出符合 lambda 条件的, 并装成一个列表(最前面的 list 就是将筛选出来的数据装成一个列表的意思)
    """    


def write_report(stats, path="report.txt"):
    """把统计结果写进文本文件。
    要求用 w 模式，内容形如：
    日志级别统计报告
    INFO: 5 条
    WARN: 3 条
    ERROR: 2 条
    """
    if not stats:
        print("未检测到统计结果")
        return
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write("日志级别统计报告\n")
            for level in stats:
                f.write(f"{level}: {stats.get(level)} 条\n")


def main():
    """
    1. 读日志
    2. 统计并打印（格式 INFO: 5 条）
    3. 用 filter_level 筛出所有 ERROR 行，逐行打印
    4. 调用 write_report 写报告，打印 “报告已写入 report.txt”
    """
    #  1. 读日志
    print("正在读取日志内容")
    data = read_log()
    print("日志内容读取完成,内容如下")
    for j, content in enumerate(data, 1):
        data_content = " ".join(content)
        print(f"[{j}]  {data_content}")
    print()

    # 2. 统计并打印（格式 INFO: 5 条）
    print("正在统计日志等级")
    stats = count_levels(data)
    for key, value in stats.items():
        print(f"{key}: {value} 条")
    print("统计完成")
    print()

    # 3. 用 filter_level 筛出所有 ERROR 行，逐行打印
    result = filter_level(data, level="ERROR")
    print(f"正在按要求筛选日志内容")
    for i, line in enumerate(result, 1):
        line_content = " ".join(line)
        print(f"[{i}]  {line_content}")
    print("筛选完成")
    print()

    # 4. 调用 write_report 写报告，打印 “报告已写入 report.txt”
    write_report(stats=stats)
    print("报告已写入 report.txt")

if __name__ == "__main__":
    main()