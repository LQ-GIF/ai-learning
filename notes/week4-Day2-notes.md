# W4 Day2 学习笔记：pytest 入门
日期：2026/10/27

## 今日学习内容
- 安装 pytest （`pip install pytest`）
- 测试文件命名：test_ 开头；测试函数命名：test_ 开头
- assert 断言：我认为结果应该是什么，输出的结果与我认为的结果不相等就报错
- 运行命令：`python -m pytest test_area.py -v`
- 输出读法：PASSED 通过 / FAILED 失败 / 底部 x passed in xxs 统计通过的总数及所用的时间

## 知识点对比表
### 手动验证 vs 自动测试
| 对比项 | 手动验证 | pytest 自动测试 |
|---|---|---|
| 每次验证 | 手动 print 再肉眼对 | 跑一条命令全自动核对 |
| 改坏代码 | 局部检查，问题代码可能在未检测到的区域里 | 全局检测，有错误立刻报告并定位错误位置 |
| 适用场景 | 临时看一眼 | 长期反复验证 |

### pytest 命名规则
| 元素 | 正确 | 错误 |
|---|---|---|
| 文件名 | test_area.py | areatest.py |
| 函数名 | def test_x() | def check_x() |

## 今天写的代码
- area.py：calculate_rectangle_area(矩形)、calculate_circle_area(圆形)，带类型标注和负数校验
- test_area.py：3 个测试（正常输入/边界值/圆形正常）
- 运行结果：3 passed in 0.03s；故意改错看 FAILED 报告

## 遇到的问题
无

## 没搞懂的地方
今天学的 pytest 只是对一些基础的函数进行了测试，但在真实的工程项目里，函数的逻辑一般都比较复杂，对于复杂函数的 pytest 测试，我目前还不了解

## 今天的收获
通过今天的学习，我了解了 pytest 这个自动检测的功能，后续要确定代码中是否有错误，我就不用一个个的去手动验证了，大大提高了我的效率