# 创建待办列表和已完成列表（创建空列表）
todo_list = []
completed_list = []
# 添加待办事项（.append()命令练习）
todo_list.append("写作业")
todo_list.append("看书")
todo_list.append("健身")
todo_list.append("学习Python")
todo_list.append("看岗位")
todo_list.append("写简历")
todo_list.append("改简历")
todo_list.append("投递简历")
# 查看所有待办事项
print("===当前待办事项===")
print(todo_list)
print(f"当前共有{len(todo_list)}个待办事项")
print(f"第一个待办事项是:{todo_list[0]}")

# 修改待办事项（列表数据修改练习）
todo_list[1] = "看AI知识相关书籍"
print("修改后的待办事项：")
print(todo_list)

# 插入待办事项（列表数据插入练习）
todo_list.insert(5, "读岗位JD")
print("插入\"读岗位JD\"后的待办事项：")
print(todo_list)

# 完成一个待办事项（.pop() 和 .append() 练习）
done = todo_list.pop(0)
completed_list.append(done)
print(f"完成了{done}事项")
print("剩余的待办事项：")
print(todo_list)
print(f"已完成待办事项：{completed_list}")

# 删除待办事项（.remove() 练习）
todo_list.remove("改简历")
print("删除\"改简历\"后的待办事项：")
print(todo_list)

# 对待办事项进行排序（.sort() 练习）
todo_list.sort()
print("排序后的待办事项：")
print(todo_list)

# 判断某个事项是否在列表（了解 if 语句 ）
if "健身" in todo_list:
    print("\"健身\"在待办事项内")
else:
    print("\"健身\"不在待办事项内")

if "喝水" in todo_list:
    print("\"喝水\"在待办事项内")
else:
    print("\"喝水\"不在待办事项内")

print("===最终状态===")
print(todo_list)
print(completed_list)

# .pop() 和 .append() 练习
done2 = todo_list.pop(0)
completed_list.append(done2)
print(done2)
print(completed_list)
print(todo_list)

# .insert() 和 .count() 练习
todo_list.insert(-1, "写简历")
print(todo_list)
print(f"待办事项中有几个\"写简历\":{todo_list.count("写简历")}")

# index()练习
first = todo_list.index("看岗位")
print(f"\"看岗位\"第一次出现的索引位置是：{first}")

# 切片练习
todo_list1 = todo_list[:6:1]
todo_list2 = todo_list[:-1:1]
todo_list3 = todo_list[1:6:2]
todo_list.reverse()
todo_list4 = todo_list[::-1]
todo_list5 = todo_list[-1:-7:-3]

print(todo_list1)
print(todo_list2)
print(todo_list3)
print(todo_list)
print(todo_list4)
print(todo_list5)