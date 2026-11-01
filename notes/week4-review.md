# W4 周复盘笔记：类型标注，测试与 Git
日期：2026/11/1

## 本周学习内容
| 天 | 主题 | 关键收获 |
|---|---|---|
| Day1 | 类型标注 + mypy | 明确函数输入的数据类型，mypy 检查输入的数据类型是否正确
| Day2 | pytest 入门 | 测试程序/函数的文件/函数名必须以 test_ 开头，assert 断言，pytest -v 运行所有函数 |
| Day3 | 边界测试 + raises | 测负数/None/非法 method，用 pytest.raises |
| Day4 | Git 分支与 PR | 切换分支、merge 冲突、push 分支到远程仓库、PR |
| Day5 | README | 8 大模块，GitHub 自动渲染 |
| Day6 | 综合 tests/ 目录 | 业务代码和测试分离，正常 PR 流程 |

## 本周最有价值的收获点
学会了正确的 PR 流程，理解了 PR 流程的具体功能以及存在的意义

## 本周印象深刻的一个错误
在副分支修改完代码后，直接本地 merge 合并到主分支，后续进行对副分支 PR 时，显示"没有可比" ，导致第一次 PR 流程失败，这次失败让我理解了正确 PR 流程的发起顺序

| 错误现象 | 原因 | 解决 |
|---|---|---|
| 本地 merge 后发起 PR 流程显示"没有可比" | 本地 merge 后，主副分支代码一样，所以显示"没有可比" | 创建新分支修改代码后直接 push 提交，并发起 PR，不在本地进行 merge 合并 |

## 下周目标
下周开始学习数据与项目设计，下周的学习目标就是将相关的知识点做到基本理解并在练习项目中得到充分运用

## 本周成果清单
- 代码：area.py、api_utils.py、case_manager_v3.py、tests/ 目录、shopping_cart_module.py
- 测试：11 个 pytest 用例全过
- 文档：projects/week2/README.md
- Git：2 个 PR（#1 三角形面积、#2 tests 套件整合）
- 笔记：Day1-Day6 + 本周复盘