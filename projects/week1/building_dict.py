buildings = {
    "流水别墅": {
        "建筑师": "弗兰克·劳埃德·赖特",
        "地点": "美国宾夕法尼亚州",
        "建成年份": 1935,
        "建筑风格": "有机建筑"
    },
    "萨伏伊别墅": {
        "建筑师": "勒·柯布西耶",
        "地点": "法国巴黎",
        "建成年份": 1929,
        "建筑风格": "现代主义"
    },
    "巴塞罗那德国馆": {
        "建筑师": "路德维希·密斯·凡德罗",
        "地点": "西班牙巴塞罗那",
        "建成年份": 1929,
        "建筑风格": "现代主义"
    },
    "光之教堂": {
        "建筑师": "安藤忠雄",
        "地点": "日本大阪",
        "建成年份": 1989,
        "建筑风格": "极简主义",
    },
    "苏州博物馆": {
        "建筑师": "贝聿铭",
        "地点": "中国苏州",
        "建成年份": 2006,
        "建筑风格": "新中式"
    }
}

print("===所有建筑案例===")
for name in buildings:
    print(f"- {name}")
print(f"一共{len(buildings)}个建筑案例")

print("\n===查询建筑案例===")
query_name = "流水别墅"
info = buildings.get(query_name)
if info:
    print(f"建筑名称: {query_name}")
    print(f"建筑师: {info["建筑师"]}")
    print(f"地点: {info["地点"]}")
    print(f"建成年份: {info["建成年份"]}")
    print(f"建筑风格: {info["建筑风格"]}")
else:
    print(f"未找到名为'{query_name}'的建筑案例")

print("\n===查询不存在的案例===")
query_name2 = "故宫"
info2 = buildings.get(query_name2, "未找到该建筑案例")
print(f"查询'{query_name2}'的结果：{info2}")

print("\n===添加新的建筑案例===")
buildings["蓬皮杜中心"] = {
    "建筑师": "伦佐·皮亚特、理查德·罗杰斯",
    "地点": "法国巴黎",
    "建成年份": 1977,
    "建筑风格": "高技派"
}
print(f"已添加'蓬皮杜中心', 现共有{len(buildings)}建筑案例")

print("\n===修改案例信息===")
buildings["光之教堂"]["建成年份"] = 1989
buildings["光之教堂"]["建筑风格"] = "极简主义 (清水混凝土)"
print("已更新'光之教堂'的案例信息")
print(f"'光之教堂'的最新风格: {buildings['光之教堂']['建筑风格']}")

print("\n===删除案例信息===")
removed = buildings.pop("巴塞罗那德国馆")
print(f"已删除'巴塞罗那德国馆', 删除的案例信息是: {removed}")
print(f"现在共有{len(buildings)}个建筑案例")

print("\n===字典的三个方法===")
print(f"所有建筑名称: {list(buildings.keys())}")
print(f"所有案例数量: {len(buildings.values())}")
print(f"所有键值对数量: {len(buildings.items())}")

print("\n===最终所有建筑案例===")
for name, info in buildings.items():
    print(f"\n【{name}】")
    print(f"建筑师: {info['建筑师']}")
    print(f"地点: {info['地点']}")
    print(f"建成年份: {info['建成年份']}")
    print(f"建筑风格: {info['建筑风格']}")

print("\n===动态查询建筑案例===")
query_name3 = input("请输入需要查询的建筑名称: ")
info = buildings.get(query_name3)
if info:
    print(f"建筑名称：{query_name3}")
    print(f"建筑师：{info['建筑师']}")
    print(f"地点：{info['地点']}")
    print(f"建成年份：{info['建成年份']}")
    print(f"建筑风格：{info['建筑风格']}")
else:
    print(f"未找到名为'{query_name3}'的建筑案例")

print("\n===字典常用方法练习===")
# 创建空字典
num = {}

#查询数据类型
print(type(num))

# 键值对的添加
num["李一"] = 99
num["张二"] = 98
num["刘三"] = 100
num["季四"] = 88
num["钱五"] = 60
print(f"目前成绩单上共有{len(num)}人")

# 键值对的修改
num["刘三"] = 99
print(f"修改后刘三的成绩为: {num['刘三']}")

# 键值对的删除
removed = num.pop("钱五")
del num["季四"]
print(f"删除'季四'和'钱五'的成绩后, 成绩单上共有{len(num)}人, 其中钱五的成绩为{removed}")

# 判断键存在
print("李一" in num)
print("钱五" in num)


# 字典查询
print(num["刘三"])
print(num.get("李一"))

# 三种方法
print(list(num.keys()))
print(list(num.values()))
print(list(num.items()))
print(num.items())

print("\n===元组tuple===")
# 元组的创建
t1 = (1, 2, 3, 4.5, "小李", "True")
print(type(t1))

#索引访问
print(t1[0])
print(t1[-1])

#切片
print(t1[::-1])
print(t1[:6])

# 统计数据个数
print(t1.count(1))

# 获取元组内的数据索引位置
print(t1.index(4.5))

# 单数据元组创建方法
t2 = (100)
print(type(t2))
t3 = (100,)
print(type(t3))

print("\n===集合set===")
# 创建集合
s1 = {1, 2, 3, 4, 4.5, 5, 6}

# 创建空集合
s2 = set()

# 添加数据到集合
s2.add(1)
s2.add(3)
s2.add(6)
s2.add(9)
s2.add(10)
print(s2)

# 删除集合中的数据
s3 = {1, 2, 3, 4, 5}
s3.remove(3)
s4 = s3.pop()
print(s4)
print(s3)
s3.clear()
print(s3)

# 集合的差集、交集、并集
# 差集
print(s1.difference(s2))
print(s2.difference(s1))
# 并集
print(s1.union(s2))
# 交集
print(s1.intersection(s2))