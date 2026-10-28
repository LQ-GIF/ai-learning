# W4 Day3 学习笔记：边界测试与 pytest.raises
日期：2026/10/28

## 今日学习内容
- 边界测试：测 0、空值、负数等边缘输入
- pytest.raises(异常类型)：with 代码块内的代码必须抛出指定异常
- 跨目录 import：sys.path.insert 告诉 Python 去隔壁文件夹找模块
- pytest 跑整个目录：`python -m pytest -v` 不带文件名

## 知识点对比表
### 普通测试 vs 异常测试
| 对比项 | 普通 assert 测试 | pytest.raises 异常测试 |
|---|---|---|
| 测什么 | 返回值对不对 | 该报错的时候有没有真的报错 |
| 写法 | assert f(...) == 值 | with pytest.raises(异常)：f(...) |
| 函数没报错 | 不影响 | 测试失败（DID NOT RAISE） |

注：在用 pytest.raises 进行异常测试时，不要测试合法参数，合法参数用 assert 测试返回值对不对，而 pytest.raises 异常测试只测在代码运行前就该被拦截的非法输入

### 异常类型
| 异常 | 适用场景 |
|---|---|
| ValueError | 输入值不满足设定的要求 |
| TypeError | 输入的数据类型不对 |
| FileNotFoundError | 文件不存在 |

## 今天写的代码
- test_area.py:补充了两个 raises 异常测试（矩形负数和圆半径负数）
- test_api_utils.py：新建了 3 个 raises 异常测试（DELETE/PUT/XXX method）
- 运行结果：8 passed in 0.10s
- 关键点：pytest.raises 异常测试是用来测试在代码拦截非法参数后抛出的异常类型是否是设定好的异常类型

## 遇到的问题
无

## 没搞懂的地方
今天补齐了 pytest 的异常测试板块，但是对于代码会出现的异常类型以及为什么会出现这种类型的异常，目前了解的还不多，这方面的知识还需要尽快补齐

## 今天的收获
通过今天的学习，我又了解了对于输入数据错误引发的异常在运行前如何用 pytest 功能进行排查