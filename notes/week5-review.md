# W5 周复盘笔记：数据与项目设计
日期：2026/11/8

## 本周学习内容
| 天 | 主题 | 关键收获 |
|---|---|---|
| Day1 | CSV 读写 + os.walk | csv.writer 写表格，os.walk 遍历文件夹，utf-8-sig 防 Excel 表格出现乱码 |
| Day2 | time/datetime | datetime.now() 获取当前时间，strftime 格式化，两个日期相减得到天数 |
| Day3 | random + 数据清洗 | choice 随机抽取一个列表中的数据，randint 随机整数，set() 集合去重，strip 去空格 |
| Day4 | argparse | 命令行传参，--help 自动生成帮助，type=int 指定参数类型为数字 |
| Day5 | 项目模块化 | 拆分为 data/models/main 三层，各管一件事 |
| Day6 | MVP 整合 | 把本周所有知识点拼成一个能跑的工具 |

## 本周最有价值的收获
本周最有价值的收获就是在 Day5 学到的模块化拆分思维，将一整个项目按功能拆分为几个不同的模块，既有利于项目的维护，又大大提高了项目的安全性

## 本周印象最深刻的错误
- 问题：在测试项目的 --export 参数时出现报错，报错信息为：`_csv.Error: iterable expected, not int`
- 原因：在写数据导出函数时，将 writerow 写为 writerows，writerows() 期望接收到的数据是二维列表（多行数据），而运行该命令前数据经过 for 循环遍历，writerows() 实际接收到的数据为一维列表（单行数据），不符合 writerows() 的接受期望，故出现报错
- 解决方法：将writerows 改写为 writerow，writerow() 期望接收到的数据是一维列表（单行数据）

## 本周短板
- argparse 运用还不熟练
- 独立写数据清洗函数还有困难
- 拆分思维还不足以应付真实工程

## 下周目标
1. 学新内容时，每个知识点都动手敲代码，笔记里必须留下对应代码，不能只看不练
2. 周末把现在这个建筑案例工具改造成"能被别人使用"的形式（具体形式等明天看计划）
3. 每天遇到报错都要记进笔记的"遇到的问题"栏，一周至少积累 5 条

## 本周成果清单
- 代码：file_sorter.py / time_calc.py / random_gen.py / data_cleaner.py / case_cli.py / case_app/ / building_case_tool/
- 数据：result.csv / random_cases.csv / dirty_data.csv / clean_data.csv / result_case.csv
- 文档：building_case_tool/README.md（完整项目说明）
- 笔记：Day1-Day6 共 6 篇
- Git：W5 共 6 次提交，全部 push 到 main

## 本周最大的变化
通过本周的学习，最大的变化就是可以看懂一些简单的代码逻辑了，在之前的学习过程中，许多代码逻辑要通过教程来一点点理解。