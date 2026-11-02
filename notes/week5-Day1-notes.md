# W5 Day1 学习笔记：CSV 读写与文件夹遍历
日期：2026/11/2

## 今日学习内容
- csv.writer / csv.reader 读写 CSV 文件
- os.walk 遍历文件夹（root/dirs/files 三元组）
- os.path.join 拼路径、os.path.barename 取文件名
- 文件行数统计：sum(1 for line in f)

## 知识点对比
### CSV vs Excel
| 对比项 | CSV | Excel |
|---|---|---|
| 格式 | 纯文本，逗号分隔 | 二进制，带格式 |
| 用什么打开 | 记事本/VS Code/Python | Excel/WPS |
| Python 读写 | csv 模块直接读写 | 需要 openpyxl 等第三方库 |
| 文件大小 | 小 | 大 |

### os.walk 三个返回值
| 返回值 | 意思 | 例子 |
|---|---|---|
| root | 当前遍历到的文件夹路径 | E:\AI-Learning\projects\week4 |
| dirs | 里面有哪些子文件夹 | `['tests', '__pycache__']` |
| files | 里面有哪些文件 | `['area.py', 'xxx']` |

## 今天写的代码
- projects/week5/file_sorter.py：遍历文件夹，统计 .py 文件的行数存 CSV

## 遇到的问题
无

## 没搞懂的地方
今天学的知识点基本原理都懂了，但是实际应用对现在的我来说有点难

## 今天的收获
今天了解了 CSV 读写的基本原理和 os.walk 的作用