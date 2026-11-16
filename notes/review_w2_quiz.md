# W2 笔试题
## 第 1 题 `[填空]`
- def f1():
    print("A")

  def f2(n):
    if n > 0:
        return "正"
    print("X")
- 调用 `f1()`，它的返回值是什么？
- 调用 `f1()` 时屏幕上打印什么？
- 调用 `f2(5)`，`print("X")` 会执行吗？为什么？
- `f2(5)` 和 `f2(-1)` 各返回什么？

- 答案：
    - None
    - "A"
    - 不会，因为 n = 5 满足 if 条件，所以代码会直接 return "正" 后结束函数, print("X") 不执行
    - f2(5) 返回 "正" f2(-1) 返回 None


## 第 2 题 `[简答]`
- def greet(name, city="杭州", title="先生"):
    return f"{name}{title}，来自{city}"
- `greet("张三")` 返回什么？
- `greet("张三", "上海")` 返回什么？
- `greet(name="张三", title="女士")` 返回什么？
- 默认参数能不能写在必须参数前面（例如 `def greet(city="杭州", name)`）？为什么？

- 答案：
    - "张三先生, 来自杭州"
    - "张三先生, 来自上海"
    - "张三女士, 来自杭州"
    - 不可以，位置参数接收数据的本质就是通过形参和实参位置的一一对应来接收的，如果把默认参数写在位置参数前面，那么输入的实参顺序就会被打乱，形参就会接收到错误的实参，导致返回值错误

- 正确答案：
    **[4] 现实情况中，若出现这种情况，Python 会直接阻止该操作，并标红提示，连进入运行的机会都没有**

## 第 3 题 `[写输出]`
- x = 10

  def change():
    x = 20
    print("函数内:", x)

  change()
  print("函数外:", x)
- 写出完整输出。再回答：函数里的 `x = 20` 有没有改到外面的 `x`？为什么？如果函数里想改外面的 `x`，需要怎么做？

- 答案：
    - "函数内:20"
      "函数外:10"
    - 没有, 因为 x = 10 为全局变量，x = 20 为局部变量，如果要再函数内部修改全局变量，需要调用 global，此处若要修改全局变量，函数内应写为 global x: x = 20


## 第 4 题 `[写输出]`（进阶）
- def add_item(item, lst=[]):
    lst.append(item)
    return lst

  print(add_item(1))
  print(add_item(2))
  print(add_item(3))
- 写出三行输出。再解释为什么第二行不是 `[2]`，以及正确写法应该怎么改。

- 答案：
    - [1]
      [1, 2]
      [1, 2, 3]
    - 因为列表是可以修改的，函数中的 lst.append(item) 改变的是 lst 这个列表的本身，在运行过 print(add_item(1)) 后，函数中的 lst 的参数就从 [] 变成了 [1] ,因此后续的两次函数调用会输出以上结果
    - 正确的写法应该是：
      def add_item(item, lst=[]):
        new_lst = lst[:]
        new_lst.append(item)
        return new_lst
      先用 lst[:] 复制一个新的列表 new_lst 出来，后续的添加数据和返回列表都在新的列表上进行操作，这样就不会改动初始列表 lst


## 第 5 题 `[简答]`
- def show(*args, **kwargs):
    print(args)
    print(kwargs)

  show(1, 2, 3, name="张三", city="杭州")
- 两行输出分别是什么？
- `args` 是什么数据类型？`kwargs` 是什么数据类型？
- 如果调用 `show()`（不传任何参数），`args` 和 `kwargs` 分别是什么？

- 答案：
    - (1, 2, 3)
      {"name": "张三", "city": "杭州"}
    - args 是元组，kwargs 是字典
    - args 是 ()，kwargs 是 {}


## 第 6 题 `[写输出]`（进阶）
- cases = [
    {"name": "A", "area": 800},
    {"name": "B", "area": 1200},
    {"name": "C", "area": 350},
  ]

  result = sorted(cases, key=lambda c: c["area"], reverse=True)
  print([c["name"] for c in result])
- 输出什么？
- 把 `reverse=True` 删掉后，输出什么？
- `key=lambda c: c["area"]` 里的 `c` 代表什么？`lambda` 在这里的作用是什么（用一句话说）？

- 答案：
    - "B"
      "A"
      "C"
    - "C"
      "A"
      "B"
    - c 在当前代码中代表 cases 列表里的单个数据；lambda 在当前代码的作用是为 sorted 排序命令指定排序的对象

- 正确答案：
    **[1]  ['B', 'A', 'C'] 这道题目中 print 输出的是一个列表，所以打印出来应该是列表的形式，只有在 for 循环遍历的代码块内部的 print 打印出来的结果才是一行一行的**
    **[2]  ['C', 'A', 'B']**

## 第 7 题 `[简答]` 
- def main():
    print("跑起来了")

  if __name__ == "__main__":
    main()
- 这个 `if` 判断的作用是什么？
- 如果另一个文件写了 `import project1_case_manager`，这个文件的 `main()` 会执行吗？为什么？
- 如果不写这个判断，直接在最外层调用 `main()`，被 import 时会发生什么？

- 答案：
    - 分离函数代码和运行代码，确保在其他项目中调用该函数时，if 判断下的运行代码块不会执行
    - 不会，在当前文件中运行代码，文件的 __name__ 为 "__main__"，if 判断条件成立，所以当前文件中会执行 main()，若在另一个文件中 import 调用当前文件的函数，这时文件的 __name__ 就不是 "__main__"，if 判断条件就不成立，所以 main() 不会执行
    - 如果不写这个判断，import 调用时，文件会直接执行 main() 导致调用方代码报错崩溃


## 第 8 题 `[填空]`
- `open("a.txt", "r")`、`open("a.txt", "w")`、`open("a.txt", "a")` 三种模式分别是什么行为？
- 如果 `a.txt` 里原本有内容，用 `"w"` 打开后原内容还在吗？
- 想在原有内容后面接着写，该用哪个模式？
- 用 `with open(...) as f:` 相比 `f = open(...)` 再手动 `f.close()`，好处是什么（用一句话说）？

- 答案：
    - open("a.txt", "r") 为读取模式，行为是打开 a.txt 文件并读取文件的内容
      open("a.txt", "w") 为写入模式，行为是打开 a.txt 文件清空文件的旧内容并写入新的内容
      open("a.txt", "a") 为追加模式，行为是打开 a.txt 文件并在文件原有内容的末尾追加新的内容(该模式不会清空原有内容)
    - 用 "a" 模式
    - 手动打开和关闭文件容易出现打开后忘记关闭的情况，此时若再次打开并修改文件就会出现该文件被占用的报错，而 with open(...) as f: 会对打开并完成操作的文件进行自动关闭，既提高了代码的安全性，也提高了代码的简洁性


## 第 9 题 `[写输出]`（进阶）
- try:
    num = int("abc")
    print("A")
  except ValueError:
    print("B")
  else:
    print("C")
  finally:
    print("D")
- 输出什么？（按顺序写出打印了哪几行）
- 如果把 `int("abc")` 改成 `int("123")`，输出什么？
- 用一句话说清 `else` 和 `finally` 各在什么时候执行。

- 答案：
    - "B"
      "D"
    - "A"
      "C"
      "D"
    - else 是在 except 没有捕获到异常时执行，finally 是在整个异常处理流程执行完后，不管有没有捕获到异常，都会执行


## 第 10 题 `[简答]`
- with open("cases.json", "w", encoding="utf-8") as f:
    json.dump(cases, f, ensure_ascii=False, indent=2)
- `ensure_ascii=False` 是干什么的？不加这行会出现什么现象？
- `json.dump` 和 `json.dumps` 有什么区别？（提示：看名字最后多出来的 `s`）
- 读文件时用 `json.load` 还是 `json.load` 的反义？它接收的是文件名还是文件对象？

- 答案：
    - 用来确保写入文件后内容正确可读，不加这行会出现乱码   **正确答案：让中文以汉字形式写进文件，方便人直接阅读，而不是写成一串 `\u897f` 编码。**
    - json.dump 是将读取的数据写入一份文件，json.dumps 是将读取的数据写入多个文件（json.dumps没讲过，我猜的）
    - 用 json.load，它接收的是文件对象

    正确答案：
    **[1] 让中文以汉字形式写进文件，方便人直接阅读，而不是写成一串 `\u897f` 编码。**
    **[2] json.dumps 中的 s 是 string 的意思，整个命令的具体作用就是将 Python 对象转换为字符串并返回，你可以用一个变量来接住返回值，并打印出来用来预览要写入的内容，若通过预览发现内容有错误，可以直接在这个返回值上进行修改，修改后的返回值依旧可以进行写入文件操作；你也可以用这个返回值进行一切字符串允许的操作**

    **json.dumps 的具体用法：变量 = json.dumps(要写入文件的数据, ensure_ascii=False)**



