# W0环境周学习笔记

## 本周学习内容
- Day1：安装了 Python 和 VS Code ，并写了第一个 python 程序 hello.py
- Day2：安装了 git ，创建了 GitHub 账号，还创建了 GitHub 远程仓库，并把周一写的 hello.py 上传到了 GitHub 的远程仓库中
- Day3：学了创建虚拟环境 `.venv` ，并学会用 pip 安装包，生成 `requirements.txt`
- Day4：学了保护密钥，用 `.env` 文件存项目配置和密钥、用 `.gitignore` 文件防止上传、用 `python-dotenv` 读取环境变量

## 遇到的问题和解决方法
### 问题1：找不到运行按钮
- 现象：hello.py 代码写完后找不到运行按钮
- 原因：VS Code 开启了受限模式
- 解决：关闭该模式

### 问题2：Git 用户名和邮箱的配置命令输入错误
- 现象：输入 `git config global user.name"LQ-GIF"` 和 `git config-global user.name "LQ-GIF"` 代码时报错
- 原因：`global` 前是两个减号（--），不是一个，也不是一个也没有；`user.name` 与 `"LQ-GIF"` 中间有空格
- 解决：输入正确代码 `git config --global user.name "LQ-GIF"`，问题得以解决

### 问题3：提交 git 本地仓库代码输入错误
- 现象：输入 `git config -m "add hello.py, first commit"` 代码时报错
- 原因：`git config` 是“配置 git”的命令，`git commit` 才是提交命令
- 解决：输入正确代码 `git commit -m "add hello.py, first commit"`，文件成功提交

### 问题4：本地分支名称不一致
- 现象：输入 `git push -u origin main` 代码时提示找不到 `main` 分支，上传失败
- 原因：我用的 git 的默认分支名是 `master`（老版本git的默认命名），不是 `main`；但我提交的时候用的分支名是 `main`，两边名字不一样，所以上传失败
- 解决：输入 `git branch -M main` 修改分支名称，再输入 `git push -u origin main` 上传文件，文件成功上传

### 问题5：用 pip 下载 requests 工具包时请求超时，下载失败
- 现象：输入 `pip install requests` 代码时显示请求超时
- 原因：pip 默认从 PyPI 官方下载工具包，该网站在国外，国内访问大概率会出现请求超时、下载慢等问题
- 解决：输入 `pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple` 代码，从清华大学的镜像源中下载，；并输入 `git config set goldal.index-url https://pypi.tuna.tsinghua.edu.cn/simple` 代码，永久配置该下载源

### 问题6：重启终端后，不知道如何再次进入虚拟环境
- 现象：重启终端后，终端退出虚拟环境，提示符前不显示 `(.venv)`
- 原因：虚拟环境的激活只对当前的终端窗口有效，关掉或者重启终端，虚拟环境自动退出
- 解决：输入 `.venv\Scripts\Activate.ps1` 代码重新进入虚拟环境

### 问题7：进入虚拟环境时发生错误
- 现象：输入 `.venv\scripts\activate.ps1` 代码时，进入虚拟环境失败，出现报错
- 原因：PowerShell 把 `.venv` 当成了一个“模块”而不是文件夹路径，解析出错了
- 解决：代码 `.venv\Scripts\Activate.ps1` 中 `“Scripts”` 和 `“Activate”` 这两个代码的首字母大写

### 问题8：.gitignore 文件不生效，.env 文件出现在 git status 里
- 现象：创建了 `.gitignore` 文件，并把 `.env` 写入该文件内，但 `git status` 里还能看到 `.env`
- 原因：`.gitignore` 文件写完未保存
- 解决：`Ctrl+S` 保存 `.gitignore` 文件后，`git status` 里 `.env` 消失

## 本周收获
- 搭建好了完整的开发环境（python + VS Code + Git + GitHub + 虚拟环境）
- 了解了程序员最基础的工具链操作
- 理解了 Git 与 GitHub 的概念，以及为什么要创建虚拟环境、为什么要保护密钥，并了解了他们的操作步骤
- 遇到了一系列问题，有简单的，也有棘手的，但是都解决了

## 下周计划
- 开始 P1 Python 基础阶段，系统学习 Python 语法