# 建筑案例搜索工具
一个用于搜索建筑案例的命令行小工具，从 CSV 文件中读取建筑案例数据，支持按关键词/城市/类型/面积对数据进行筛选，并导出结果到新建的 CSV 文件，并记录导出时间

## 功能列表
- 🔍 关键词搜索案例名
- 🏙️ 按城市筛选
- 🏷️ 按类型筛选（商业/文化/住宅/教育/办公）
- 📐 按最小面积筛选
- 📤 导出筛选结果到新建的 CSV 文件

## 环境要求
- Python 3.6 及以上（开发环境为3.13）
- 不需要额外安装第三方库（只用 python 自带的 datatime/csv/argpars）

## 安装与运行
### 1. 克隆仓库
``` git clone https://github.com/LQ-GIF/AI-Learning.git ```

### 进入项目目录
``` cd E:/AI-Learning/projects/week5/building_case_tool ```

### 运行程序
``` python main.py --xxx xxx ``` (命令行工具在运行时必须带有相应的搜索参数，可以单参数运行，也可多参数运行)

## 使用方法
### 查看帮助
``` python main.py --help ```

### 按关键词搜索案例名
``` python main.py --keyword 关键词 ```

### 按城市筛选
``` python main.py --city 城市 ```

### 按类型筛选
``` python main.py --type 类型 ```

### 按输入的最小面积进行筛选
``` python main.py --min-area 最小面积 ```

### 多参数组合筛选 + 导出
``` python main.py --city 城市 --type 类型 --export result.csv ```
**--export 后的文件名可随意修改，但必须是 CSV 格式文件**

## 项目结构
```
building_case_tool/
├── __init__.py          
├── data_loader.py     # 数据读写模块(CSV 导入/导出)
├── models.py          # 筛选逻辑模块
├── main.py            # 命令行入口
├── cases.csv          # 案例数据
└── README.md          # 本项目使用说明文档
```

## 已知限制
- 本项目为简易的演示程序，不支持联网搜索
- 程序的筛选对象来源均为项目文件夹中 cases.csv 文件收录的案例数据，不支持搜索 cases.csv 文件中未收录的案例
- 界面为命令行形式，没有图像界面

## 许可证
本项目仅用于个人学习，不提供任何形式的担保