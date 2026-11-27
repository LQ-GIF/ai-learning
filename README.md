# AI 应用工程师学习仓库

> W1–W6 练习项目合集：Python 基础 → API 调用 → pytest 测试 → 命令行工具。

## 这是什么

记录 8 周 AI 应用开发学习过程，每周一个主题，产物都在 `projects/` 下。

| 周次 | 主题 | 主要产物 |
|---|---|---|
| W1 | Python 基础 | 报价计算、循环练习 |
| W2 | 数据结构与文件 | 案例管理（增删改查、排序筛选） |
| W3 | HTTP 与 API | requests 调用、JSON 处理、鉴权 |
| W4 | 类型与测试 | mypy 类型标注、pytest 测试、Git |
| W5 | 数据与项目设计 | 建筑案例工具 |
| W6 | 项目验收 | 独立重写、异常测试、完整性检查 |

## 环境要求

- Python 3.13
- Windows PowerShell（以下命令均在此环境）
- 本项目所有依赖模块已在 requirements.txt 中全部写明，运行程序前务必检查依赖模块是否安装齐全

## 安装

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
> 国内网络安装较慢时，可临时指定镜像源：
> pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


## 运行示例
> 以下命令均假设在本人仓库根目录（`AI-Learning/`）下执行，若需要实际运行，请根据用户当前的实际情况对命令进行微调。
### 示例 1 (day1_rebuild.py)：调用 API 并保存 JSON
- 运行命令（测试版）：
```
python projects\week6\day1_rebuild.py
```

> 在仓库根目录执行：`python projects\week6\day1_rebuild.py` 时 `output.json` 会生成在你执行命令时所在的目录，不是脚本所在的 week6 目录。如果想保存到单独的文件夹，请按以下命令操作：
```
mkdir 文件夹名称 -Force                           # 新建文件夹
cd (新建文件夹的绝对路径)                          # 将运行目录跳转到新建文件夹所在的位置
python (day1_rebuild.py 在当前设备中的绝对路径)    # 跳转完成后用 day1_rebuild.py 的绝对路径运行该程序
```

- 预期输出（6 个 URL 各一种结果）:
```
https://httpbin.org/get 解析完成, 已保存到 output.json 
https://httpbin.org/status/404 异常, 状态码为: 404
https://httpbin.org/status/500 异常, 状态码为: 500
https://httpbin.org/status/300 返回的内容不是 JSON(状态码 300)，请核对该地址是否返回 JSON
https://nonexistent-abcxyz.com 连接失败, 请检查网络
https://github.com/LQ-GIF 连接失败 / 或返回非 JSON（取决于当时网络）
```
> `https://github.com/LQ-GIF` 网站为真实网络地址，测试结果会根据网络情况、IP 地址等外在因素而有所不同，以个人实际输出结果为准，本结果仅供参考，特此提醒！！！

- 保存多个写入文件
  若要对不同的返回结果进行单独保存，可在 `projects\week6` 文件夹中找到 `day1_rebuild.py` 程序，对该程序中的 `path` 变量的值（第 10 行代码）进行修改，只改 `.json` 之前的内容，`.json` 这个文件格式后缀不能动

**当状态码为 200 时，程序会把响应内容写进 `output.json`，位置是「你执行命令时所在的目录」，不是脚本所在的目录。在根目录执行，文件就落在根目录；想让文件落到指定文件夹，就先 `cd 文件夹绝对路径` 再运行。**

### 示例 2 (test_network_errors.py)：运行测试
- 运行命令:
```
cd projects\week6
python -m pytest test_network_errors.py -v
```
- 预期输出（6 个测试项目全部通过）：
```
================================================= test session starts ==================================================
platform win32 -- Python 3.13.15, pytest-9.1.1, pluggy-1.7.0 -- E:\AI-Learning\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: E:\AI-Learning\projects\week6
collected 6 items                                                                                                                                               

test_network_errors.py::test_domain_not_exist PASSED                                                                                                      [ 16%]
test_network_errors.py::test_url_timeout PASSED                                                                                                      [ 33%]
test_network_errors.py::test_url_httperror PASSED                                                                                                      [ 50%]
test_network_errors.py::test_domain_not_exist_1 PASSED                                                                                                      [ 66%]
test_network_errors.py::test_url_timeout_1 PASSED                                                                                                      [ 83%]
test_network_errors.py::test_url_httperror_1 PASSED                                                                                                      [100%]

================================================== 6 passed in 38.78s==================================================
```
**运行该程序时，必须将运行地址定位到该程序所在的文件夹内。否则，该程序会运行失败**

### 示例 3 (building_case_tool)：建筑案例搜索工具
- 该项目的详细使用方法在 `E:\AI-Learning\projects\week5\building_case_tool\README.md` 路径下的 REDME.md 文档中已写明，若有需要可以按路径打开文档查看具体使用方法，这里不再重复说明

## 目录结构
AI-Learning/
├── notes/                          # 学习笔记
├── projects/
│   ├── week0/                      # W0 工具安装与准备
│   ├── week1/                      # W1 Python 基础
│   ├── week2/                      # W2 数据结构与文件
│   ├── week3/                      # W3 HTTP 与 API
│   ├── week4/                      # W4 类型与测试
│   ├── week5/                      # W5 数据与项目设计
│   ├── week6/                      # W6 验收周
│   │   ├── day1_rebuild.py         # 独立重写：API + JSON
│   │   ├── day1_compare.md         # 重写版与 W3 原版对比文档
│   │   ├── api_utils_2.py          # 网络失败测试（测试对象）
│   │   └── test_network_errors.py  # 网络失败测试（测试程序）
│   └── week_strengthen/            # 巩固测验
├── screenshots/                    # 每日练习作业截图
├── .gitignore/                     # 忽略上传清单
├── README.md                       # 项目说明文档
└── requirements.txt                # 依赖清单

## 已知限制
- 本项目中的所有程序为个人学习产物，仅限于对学习内容做简单演示，不具备联网功能，不支持多人同时编辑
- 本项目不设置任何权限拦截（用户登陆、权限管理等）措施，所有计算机设备均可通过拷贝代码来浏览本项目的全部内容，切勿将个人敏感或重要信息上传至本项目，若因此造成的任何损失，本人概不负责

## 许可证
本项目仅用于个人学习，不提供任何形式的担保