# W3 Day3 学习笔记：POST 请求
日期：2026/10/21

## 今日学习内容
- post 请求：给服务器提交数据（登陆/注册/发表评论/上传文件）
- requests.post()：发送 post 请求
- json 参数：把提交的数据自动转换为 JSON 格式放在请求体里
- Content-Type 请求头：告诉服务器发送的数据格式
- Postman：图形化 API 测试工具，不用写代码就能测试请求
- https://httpbin.org/post：测试 POST 请求的工具网站，回原样返回你发送的数据

## GET 和 POST 的区别
| 对比 | GET | POST |
|---|---|---|
| 作用 | 从服务器获取数据 | 向服务器提交数据 |
| 参数位置 | 拼在 URL 后面（?key=value） | 放在请求体里，不在 URL 中显示 |
| 安全性 | 参数显示在 URL 上，不安全 | 参数在请求体里，相对安全 |
| 数据量 | 有长度限制 | 无长度限制 |
| 例子 | 搜索数据、查看用户信息 | 登陆、注册、发表评论 |

## json 和 data 参数的区别
| 参数 | 作用 | 发送的 Content-Type |
|---|---|---|
| json=data | 自动把提交的数据转换成 JSON 发送 | application/json |
| data=data | 发送表单格式的数据（key=value&key=value） | application/x-www-from-urlencoded |

## 今天的代码
- post_test.py：用 requests.post 发送 JSON 数据到 `https://httpbin.org/post`，打印返回 JSON，验证发送成功
- Postman 测试：用图形化工具发送同样的 POST 请求

## 今天遇到的问题
无

## 没搞懂的地方
今天学习了 POST 请求的内容，练习的项目都是在 `https://httpbin.org/post` 测试网站上练习的，对 POST 请求在真实的工程项目中的具体作用和返回的具体内容还不了解

## 今天的收获
学习了 POST 请求的用法，了解到 POST 的请求参数放在请求体内，相对于 GET 来说，相对于 GET 来说更加的安全