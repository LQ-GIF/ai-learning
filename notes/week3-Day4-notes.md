# W3 Day4 学习笔记：API 鉴权
日期：2026/10/22

## 今日学习内容
- API 鉴权：服务器验证"你是谁，你有没有权限"的过程
- API Key：平台发的长期密钥（通行证）
- Bearer Token：登陆后服务器发的临时通行证（验证码）
- Authorization 请求头：`Authorization: Bearer <key>` 标准格式
- python-dotenv 库：读取 .env 文件中的环境变量
- .env 文件：存敏感信息（API Key、密码）的配置文件
- .gitignore：忽略上传清单，告诉 Git 哪些文件不需要上传

## API Key 与 Bearer Token 的区别
| 对比 | API Key | Bearer Token |
|---|---|---|
| 是什么 | 平台发放的长期密钥 | 登陆后服务器发放的临时通行证 |
| 比喻 | 会员卡（长期有效） | 门票（当日有效） |
| 有效期 | 长期（除非主动重置） | 短期（几个小时或几天） |
| 怎么来的 | 平台在网站手动生成 | 调用登陆接口后返回 |

## 为什么不把 API Key 硬编码在代码中
- 安全风险：提交到 GitHub 后任何人都能看到，极易被别人盗用
- 不方便管理：Key 泄露重置时要去代码中一个个改
- 不符合行业规范：正规公司都要求密钥放在环境变量里

## .env 文件的工作流程
- 把 API Key 写入 .env 文件里（API_KEY=xxx）
- 代码里用 load_dotenv() 加载 .env 文件
- 用 os.getenv("API_KEY") 读取 API_Key
- 把 .env 加入 .gitignore，防止提交到 GitHub

## 今天写的代码
- auth_test.py：从 .env 中读取 API Key，设置 Authorization: Bearer 头，发送请求到 https://httpbin.org/headers，验证鉴权头正确设置

## 遇到的问题
无

## 没搞懂的地方
虽然今天学习的知识基本的运行逻辑理解了，但仍然不了解今天学的东西在真实的工程环境中会起什么具体作用，以及会返回什么具体内容

## 今天的收获
提高了我保护密钥不被泄露的安全意识以及操作方法