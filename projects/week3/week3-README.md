# W3 HTTP 与 API 项目说明
## 一句话简介
本周用 Python requests 库公开调用 API，覆盖 GET/POST、请求参数、鉴权、分页、限速、重试，并把公共请求逻辑封装为可复用的工具函数

## 环境依赖
- Python 3.13
- 第三方库：requests、python-dotenv
- 安装命令：pip install requests python-dotenv

## 文件清单与运行方法
（在项目根目录 E:\AI-Learning 下，虚拟环境已激活后运行）
| 文件 | 作用 | 运行命令 |
|---|---|---|
| http_test.py | 基础 GET 请求、状态码与响应头 | python projects/week3/http_test.py |
| github_api.py | 带 params/timeout 解析仓库列表 | python projects/week3/github_api.py |
| post_test.py | POST 发送 JSON，对比 GET | python projects/week3/post_test.py |
| auth_test.py | 环境变量读 Key、Bearer 鉴权验证 | python projects/week3/auth_test.py |
| pagination.py | 分页拉取仓库并保存 repos.json | python projects/week3/pagination.py |
| api_utils.py | 通用 api_call 工具函数（被 v2 调用） | 无需单独运行 |
| github_api_v2.py | 用 api_utils 重写的仓库查询脚本 | python projects/week3/github_api_v2.py |
| repos.json | Day5 保存的数据产物 | 无需单独运行 |

## 环境变量说明
- 根目录 .env 中 API_KEY 为测试假值，不对应真实平台。
- 真实项目中 Key 只放 .env，.gitignore 已忽略 .env，禁止提交到 GitHub。

## 已知限制
- GitHub 国内直连不稳定，可能出现 ConnectionError，重试或切换网络即可。
- httpbin.org 只原样回显请求头，不校验 Key 真假；真实 API 的错误 Key 会返回 401。