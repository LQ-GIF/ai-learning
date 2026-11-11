cases = [
    {"name": "西湖边现代咖啡馆", "city": "杭州", "type": "商业", "area": 150},
    {"name": "西溪湿地图书馆", "city": "杭州", "type": "文化", "area": 800},
    {"name": "上海外滩美术馆", "city": "上海", "type": "文化", "area": 1200},
    {"name": "南京新中式别墅", "city": "南京", "type": "住宅", "area": 350},
    {"name": "杭州未来幼儿园", "city": "杭州", "type": "教育", "area": 600},
    {"name": "上海工业风书店", "city": "上海", "type": "商业", "area": 200},
    {"name": "苏州复古餐厅", "city": "苏州", "type": "商业", "area": 280},
    {"name": "杭州极简办公楼", "city": "杭州", "type": "办公", "area": 2000}
]

hangzhou_cases = [a for a in cases if a['city'] == "杭州"]    # 用列表推导式筛选地点为杭州的案例
print("-" * 40)
print("所在地为杭州的案例")
for case in hangzhou_cases:    # 遍历筛选出的结果，并输出
    print(f"{case['name']} | {case['city']} | {case['type']} | {case['area']}")

big_cases = [b for b in cases if b['area'] >= 500]    # 用列表推导式筛选面积大于等于 500 的案例
print("-" * 40)
print("面积 ≥ 500 平方米的案例")
for d in big_cases:    # 遍历筛选出的结果，并输出
    print(f"{d['name']} | {d['city']} | {d['type']} | {d['area']}")

print("-" * 40)
print("统计各个城市案例数量")
stat_dict = {}
for p in cases:
    stat_dict[p['city']] = 0

for q in cases:
    if q['city'] in stat_dict.keys():    # 这里的 .key 是多余的，in 一个字典默认判断该字典的键
        stat_dict[q['city']] += 1
for ct in stat_dict.items():      # 这里可以用解包: for city, count in stat_dict.items, 最后 print(f"{city}: {count} 个")
    print(f"{ct[0]}: {ct[1]}")
"""
统计各个城市案例数量模块正确写法:
stat_dict = {}
for p in cases
    city = p['city']
    if city in stat_dict
        stat_dict[city] += 1
    else
        stat_dict[city] = 0

统计各个城市案例数量模块简洁写法:
stat_dict = {}
for p in cases:
    city = p['city']
    stat_dict[city] = stat_dict.get(city, 0) + 1

这两个方法用到的知识点：
1. 字典添加和修改数据的方法: dict["键"] = 值
2. 访问字典数据, 数据不存在返回默认值: dict,get("键", "默认值")
"""

print("-" * 40)
print("计算各案例报价及总报价")
quote_list = []
total_quote = 0
for c in cases:
    if c['type'] == "商业":
        quote = c['area'] * 800
    elif c['type'] == "住宅":
        quote = c['area'] * 500
    elif c['type'] == "文化":
        quote = c['area'] * 600
    elif c['type'] == "教育":
        quote = c['area'] * 550
    else:
        quote = c['area'] * 400
    print(f"{c['name']} 的报价为 {quote} 元")
    total_quote += quote
    item = {
        "name": c["name"],
        "quote": quote
    }
    quote_list.append(item)
print(f"总报价为 {total_quote}")

print("-" * 40)
print("最高报价案例")
max_quote = quote_list[0]
for qt in quote_list:
    if qt['quote'] > max_quote['quote']:
        max_quote = qt
print(f"最高报价案例为 {max_quote['name']}, 报价 {max_quote['quote']} 元")

print("-" * 40)
print("面积最大的三个案例")
all_areas = []
for k in cases:
    all_areas.append(k['area'])
all_areas.sort(reverse=True)  # W1 Day3 学过列表排序，reverse=True 是从大到小
top3 = all_areas[:3]  # 切片取前 3 个

print("面积前三名")
rank = 0
for m in top3:      #先遍历最大的三个面积
    for y in cases:  #再遍历列表
        if y['area'] == m: # 内层遍历的所有数据与外层第一轮遍历得到的数据做对比，完成后进入外层第二轮遍历，以此类推，直到外层数据遍历完成
            rank += 1
            print(f"[{rank}] {y['name']} | {y['city']} | {m}㎡")

