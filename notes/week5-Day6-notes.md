# W5 Day6 学习笔记：建筑案例工具MVP整合
日期：2026/11/7

## 今日学习内容
- 整合本周所有知识点做一个完整 MVP
- csv.DictReader：按列名读 CSV （比 reader 更方便）
- 新增 --export 参数导出结果，并记录导出时间
- README 编写项目规范

## 本周知识回顾
| 天 | 学习内容 | 应用方式 |
|---|---|---|
| Day1 | csv 读写 + os.walk | data_loader.py |
| Day2 | datetime | 导出时间戳 |
| Day3 | random + 数据清洗 | cases.csv 数据准备 |
| Day4 | argparse | 为 main.py 提供参数解析 |
| Day5 | 模块化拆分 | 三层结构 |

## 三、今天写的代码
- building_case_tool/ 完整MVP（data_loader + models + main + cases.csv + README）

## 遇到的问题
- 问题：在测试项目的 --export 参数时出现报错，报错信息为：`_csv.Error: iterable expected, not int`
- 原因：在写数据导出函数时，将 writerow 写为 writerows，writerows() 期望接收到的数据是二维列表（多行数据），而运行该命令前数据经过 for 循环遍历，writerows() 实际接收到的数据为一维列表（单行数据），不符合 writerows() 的接受期望，故出现报错
- 解决方法：将writerows 改写为 writerow，writerow() 期望接收到的数据是一维列表（单行数据）
- 关键知识点：
    - writerow() 期望接收到的数据是一维列表（单行数据），常用于接收 for 循环遍历后的单行数据结果
    - writerows() 期望接收到的数据是二维列表（多行数据），常用于直接接收整个数据列表

## 没搞懂的地方
今天对这一周的知识进行了整合运用，明显感觉到之前学的知识点在运用方面还有很大的提示空间，尤其是 Day5 学的 argparse 模块的知识还未熟练掌握，后续要勤加练习

## 今天的收获
第一次把一周的零散知识点拼成一个能跑的完整工具，不仅是对旧知识的一次巩固，更从这次项目练习中发现了几个掌握不牢固的知识点