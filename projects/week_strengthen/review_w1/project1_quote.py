projects = []
serial = 0
while True:
    project_info = input("请按 (项目名称,城市,面积,类型) 的顺序依次输入项目信息,若要结束录入, 请输入 'done': ").split(",")

    if len(project_info) != 4 and project_info[0] != "done":
        print("格式错误，应该是 (名称,城市,面积,类型), 请重新输入")
        continue

    if project_info[0] != "done":
        a = project_info[2].isdigit()
    else:
        break

    if not a:
        print("输入的面积必须为数字, 请重新输入")
        continue

    serial += 1
    pj = {
        "i": serial,
        "name": project_info[0],
        "city": project_info[1],
        "area": int(project_info[2]),
        "type": project_info[3]
    }
    projects.append(pj)

print(f"一共录入了 {len(projects)} 个项目")
for j in projects:
    print(f"{[j['i']]}  {j['name']} | {j['city']} | {j['area']}㎡ | {j['type']}")

areas = []
for b in projects:
    areas.append(b['area'])
total_area = sum(areas)
if serial == 0:
    print("目前项目为空, 无法计算平均面积")
    average_area = 0
    max_area = 0
else:
    average_area = total_area / serial
    max_area = max(areas)
    max_name = [p['name'] for p in projects if p['area'] == max_area]


print(f"总面积为 {total_area}、平均面积为 {average_area:.2f}")
print(f"面积最大的项目名称是: {max_name}")

