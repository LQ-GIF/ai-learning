# W2 Day4 学习日记：虚拟环境 venv 与 requirements.txt
日期：2026/10/15

## 今日学习内容
### 为什么需要虚拟环境
- 问题场景：多个不同项目依赖不同版本的库，库与库之间会因版本问题而相互冲突，导致某个项目因无法正常运行
- 虚拟环境就是一个文件夹，文件夹内装了独立的 python 运行环境
- 激活虚拟环境后，python 和 pip 都只作用于对应的虚拟环境，不同虚拟环境中安装的库互不干扰
- 三个核心作用：
    1.隔离依赖：每个项目有自己独立的库
    2.版本管理：每个项目可以锁定自己需要的版本
    3.项目可复现：用 requirements.txt 记录依赖，别人能一键安装
- 虚拟环境的四个优点：
    1.项目隔离：不同项目使用不同版本的 python 和第三方库，互不干扰
    2.避免污染：安装的包只影响当前环境，不影响全局 python
    3.依赖可控：通过 requirements.txt 精确记录和复现环境
    4.安全测试：可放心升级或者试用新包，不影响其他项目

### 虚拟环境创建的完整流程
- 创建：`python -m venv .venv`
- 激活：`.venv\Scripts\Activate.ps1`
- 激活成功标准：终端提示符前面出现 `(.venv)` 
- 退出虚拟环境：`deacitvate`
- 查看已安装的库：`pip list`
- 安装库：`pip install 库名`

### requirements.txt
- 是什么：纯文本文件，用来记录项目依赖的所有库及版本号
- 为什么需要：团队协作，项目部署，项目可复现
- 生成：`pip freeze > requirements.txt`
- 通过该文件安装库：`pip install -r requirements.txt`
- 格式：每行一个库，库名==版本号，如 `requests==2.34.2`

### 验证隔离效果（今天的重要试验）
- 在全新的虚拟环境里 pip list 只有 pip 和 setuptools（从 python 3.12版本开始，全新虚拟环境里只有 pip）
- import requests 会报 ModuleNotFoundError
- 安装了 requests 后才能 import
- 两个虚拟环境里的库互不干扰

## 今天的练习
- 在E:\venv_test 全新文件夹里从零创建虚拟环境
- 验证隔离效果（新的虚拟环境中没有 requests）
- 安装 requests 并生成 requirement.txt
- 删除虚拟环境文件夹，重启后用 requirements.txt 一键还原所有依赖
- 关键点：`pip freeze > requirements.txt` 导出所有依赖，`pip install -r requirements.txt` 一键安装

## 今天遇到的问题
无

## 没搞懂的地方
今天学习的内容是对之前学过的虚拟环境这一内容的复习和底层原理的拆解，今天学完后，我对这一方面的内容理解更加深刻了