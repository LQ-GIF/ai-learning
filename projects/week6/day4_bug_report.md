# Bug 记录：AttributeError 'function' object has no attribute 'keys'
## 1. 现象
时间：2026.11.24
在运行 project3_complete.py 程序获取 `https://httpbin.org/get` 返回的响应内容时出现程序报错，导致程序中断，报错信息为 AttributeError: 'function' object has no attribute 'keys' 

## 2. 报错信息
```
> e:\ai-learning\projects\week6\day4_pdb_demo.py(12)<module>()
-> breakpoint()
(Pdb) p data
<bound method Response.json of <Response [200]>>
(Pdb) p type(data)
<class 'method'>
(Pdb) c
Traceback (most recent call last):
  File "e:\AI-Learning\projects\week6\day4_pdb_demo.py", line 13, in <module>
    print(data.keys())
          ^^^^^^^^^
AttributeError: 'function' object has no attribute 'keys'
```
> 为了排除项目里其他代码的干扰，我另建了 `day4_pdb_demo.py`，只保留最核心的调用逻辑来复现同一个问题，下面的调试过程基于这个脚本。

## 3. 原因分析
- 主要原因：
    在使用 pdb 进行代码调试时发现，data 返回的数据类型是 method；而程序正常时，data 接收到的数据类型应该是 dict。所以判断是函数对返回的响应内容的处理上出现了问题，而函数中对返回响应内容的处理代码只有一条，就是当网址返回的状态码为 200 时，对该网址返回的响应内容进行解析，自此定位到问题所在，就是程序代码中第 12 行对返回的响应内容进行解析的代码 return response.json 后面没有加括号，导致程序并没有调用这个方法进行解析
- 衍生问题：
    按照 pdb 调试器显示的数据类型来看，最后返回的报错信息应该是 AttributeError: 'method' object has no attribute 'keys'，但实际返回的确是 AttributeError: 'function' object has no attribute 'keys'，出现该问题的原因如下：
        - 在 return response.json 这串代码中，response.json 指代的是一个解析方法，相当于告诉 Python 我可以用来解析 JSON，但这条命令并不会执行解析这个动作，因为它没有加调用括号，所以 data 最后接收到的是绑定方法本身，而不是解析后的 JSON；那为什么最后报错的类型会显示 function （函数）呢，在程序的最后一行代码中，需要打印显示 data 的 key，此时程序会调用 data 接收到的数据，在其中寻找对应的 key 的值，但是由于之前的解析命令没有加调用括号，导致 data 接收到的是绑定方法本身，数据类型是 method 而不是 dict，导致程序找不到对应的值，于是程序将查找目标转移到 response.json 这个函数本身，在函数层面进行查找，但因为少了调用括号，response.json 函数命令并没有执行，所以程序在函数层面也查找不到想要的值，因此程序直接在当前的函数层面触发报错，所以返回的报错信息出现了 function 这个数据类型

## 4. 修改方案
- 在 return response.json 代码后加一个调用括号，改为 return response.json()

## 5. 验证结果
```
>>> 这是新版 project3_complete

>>> https://httpbin.org/get
    [拿到数据，请求头为：['args', 'headers', 'method', 'origin']]

>>> https://httpbin.org/status/404
https://httpbin.org/status/404 连接异常, 状态码为 404
    [返回 None —— 调用方应该跳过写文件]

>>> https://httpbin.org/status/500
https://httpbin.org/status/500 连接异常, 状态码为 500
    [返回 None —— 调用方应该跳过写文件]

>>> https://httpbin.org/status/300
https://httpbin.org/status/300 返回的的内容不是 JSON, 状态码为 300, 请核对该地址返回的内容是否为 JSON 格式
    [返回 None —— 调用方应该跳过写文件]

>>> https://nonexistent-abcxyz.com
https://nonexistent-abcxyz.com 连接失败, 请检查网络
    [返回 None —— 调用方应该跳过写文件]

>>> https://httpbin.org/delay/6
https://httpbin.org/delay/6 连接超时, 请检查网络后重试
    [返回 None —— 调用方应该跳过写文件]
```
> 程序原代码为 https://httpbin.org/delay/3，此处改为 delay/6 是为测试程序是否能承接住超时报错，修改并未上传远程仓库

## 调试思路复盘
- 先看报错的最后一行，确定 "是哪一类错误"；
- 再看 traceback 的行号，定位报错位置，找到 "程序在哪一步死的"；
- 定位报错位置后，用 `print` 或 `breakpoint()` 把可疑的变量打印出来，看它到底是什么类型、什么值。不要根据报错信息直接猜（今天的错误就是最好的例子，data 接收的数据类型为 method，但返回的报错信息中，数据类型为 function）；
- 只改一处，马上重跑，用现象是否消失来验证，不要一次改多处。
- 出现 pdb 调试得到的数据类型与报错信息中的数据类型不一样的情况时，要先了解报错代码的具体运行机制和逻辑
