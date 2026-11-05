# W5 Day4 学习笔记：argparse 命令行参数
日期：2026/11/5

## 今日学习内容
- argparse.Argumentparser：创建解析器
- add_argument：登记参数（--keyword, --city, --type, --min-area）
- parse_args：读取参数
- type=int：指定参数类型
- --help：自动生成帮助信息

## argparse vs input()
| 对比项 | input() | argparse |
|---|---|---|
| 传参时机 | 程序跑起来后用户根据提示输入 | 准备运行时在命令行一次性给完 |
| 传参方式 | 交互打字 | 命令行输入 |
| 适用场景 | 小游戏 | 工具脚本 |
| 能否自动化 | 不能 | 能 |

## 常用命令
| 命令 | 作用 |
|---|---|
| python case_cli.py --help | 看帮助 |
| python case_cli.py --keyword 咖啡馆 | 关键词搜索 |
| python case_cli.py --city 杭州 | 按城市筛 |
| python case_cli.py --min-area 500 | 按面积筛 |

## 今天写的代码
- projects/week5/case_cli.py：命令行案例搜索工具

## 遇到的问题
无

## 没搞懂的地方
对于今天学的内容运用还不熟练，还有几处地方了解的还不彻底，需要在看一遍资料

## 今天的收获
了解了 argparse 的功能与用法，同时也了解到 argparse 写的代码可以自动化