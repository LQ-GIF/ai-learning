# W0环境周检查清单
检查日期：2026/10/03

## 工具安装检查
- [x] Python 已安装
  - 版本：Python 3.13.15
  - 检查命令：`python --version`
  - 结果：已通过

- [x] Git 已安装
  - 版本：Git 2.56.0.Windows1
  - 命令：`git --version`
  - 结果：已通过

- [x] VS Code 已安装
  - 能正常打开，能编辑代码，能运行Python
  - 结果：已通过

## 环境配置检查
- [x] 虚拟环境能正常进入
  - 能正常激活（提示符前出现 `(.venv)`）
  - `pip list` 能看到已安装的包（requests、python-dotenv 等）
  - 结果：已通过

- [x] .gitignore 生效
  - `git status` 看不到 `.env`
  - GitHub 仓库里看不到 `.env`
  - 结果：已通过

- [x] pip 镜像源已配置
  - 使用清华镜像源，下载不超时
  - 结果：已通过

## 代码运行检查
- [x] hello_text.py 能运行
  - 新建 hello_text.py 文件，不看笔记写入代码，独立运行成功
  - 终端结果输出正确的 print 内容
  - 结果：已通过

- [x] env_text.py 能运行
  - 能读取 .env 里的 DEMO_KEY
  - 能输出 not-a-real-key 和 None、
  - 结果： 已通过

## GitHub 检查
- [x] 能正常 push 代码到 GitHub 仓库
  - 最近一次提交：update Day5 folder
  - GitHub能看到最新提交的文件
  - 结果：已通过

- [x] 仓库文件结构清晰
  - 有 projects/、notes/、screenshots/ 三个文件夹
  - 代码按周分类，笔记完整，截图按天归档
  - 结果：已通过

## 检查总结

- 总检查项：10项
- 已通过：10项
- 未通过：0项
- 结论：W0环境周所有工具和环境均正常运行，可以进入 P1 Python 基础阶段学习