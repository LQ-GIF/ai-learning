# W3 Day2 学习笔记：requests.get() 详解
日期：2026/10/20

## 今日学习知识
- param 传参：把查询参数放进字典里，requests 自动拼接到 URL 后面
- timeout 超时：设置请求最大等待时间，请求时间超过设定时间会发生报错，防止请求时间过长导致程序卡死
- 数组类型 JSON 解析：`response.json()`返回列表，用 for 循环遍历来获取列表中的信息
- GitHub 仓库 API：获取用户的仓库列表，每个仓库包含名称/描述/星数/语言等字段
- enumerate 函数：遍历列表时同时获取序号和对应的数据
- max 函数 + lambda：找出列表中某个字段最大的元素，lambda 用来定义具体字段

## param 和 headers 的区别
| 对比 | param | headers |
|---|---|---|
| 作用 | 查询参数（告诉服务器要什么数据） | 请求头（告诉服务器你是谁，接受什么格式） |
| 位置 | 拼在 URL 后面（?key=value） | 放在请求的头部 |
| 例子 | page=1, per_page=10, sort=updated | User-Agent: Mozilla/5.0 |

## 常见的 GitHub 仓库字段
- name：仓库名
- description：仓库描述
- stargazers_count：仓库星数（收藏数）
- language：主要编程语言
- updated_at：最后更新时间
- created_at：创建时间
- forks_count：分叉数
- open_issues_count：未解决的 Issues 数

## 今天的代码
- github_api.py：调用 GitHub API 获取 torvalds 的仓库列表，打印每个仓库的详细信息，找出星数最多的仓库

## 遇到的问题
无

## 没搞懂的地方
昨天用 requests.json 命令去解析 API 返回的字符串数据，今天又用同样的命令去解析列表数据，那 API 返回的所有类型的数据都可以用这个命令解析吗？还是说有其他情况。

## 最大的收获
通过昨天和今天的学习，使我对 API 的作用和使用方法有了一个基本的理解