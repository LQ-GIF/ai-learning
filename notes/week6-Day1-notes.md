# W6 Day1 学习笔记
日期：2026.11.16

## 今日学习内容
- 今天重写了 W3 的 HTTP 请求代码，主要重写了以下功能
    - 用 requests 请求模块的 get 函数向对应网址发送请求
    - 获取返回的状态码
    - 对返回的状态码建立 if 判断，当返回状态码为 200 时，对返回的 JSON 格式的响应内容进行解析，并将解析内容通过 with 方法写入指定文件
    - 建立异常捕获机制，对返回的其他状态码，用 if 判断进行捕获，对于连接失败等其他非状态码异常，用 try 进行捕获

## 项目对比
| 项目 | 我盲写的写法 | W3 当时的写法 | 差异说明 |
|---|---|---|---|
| 请求方式 | requests.get(url, timeout) | requests.get(url, params, header, timeout) | 我重写的请求只有网址和超时，W3 的请求在我重写版的基础上还添加了 params 查询参数和 header 请求头 |
| 有没有设 timeout | 有 | 有 | 超时限制都是 10 s 无差异 |
| 状态码怎么判断 | try + if 来判断返回的状态码，并捕获其他异常 | try + if 来判断返回的状态码，并捕获其他异常 | 我重写的状态码判断对每个类型的状态码都有独立的判断分支，W3 的状态码判断只对状态码 200 进行判断，其他状态码一律按请求失败处理 |
| JSON 怎么解析 | 用打印命令`print(data['headers']['User-Agent'])`直接输出 | 将返回的响应内容通过遍历获取想要的信息 | 由于访问地址的不同，我重写的版本返回的响应内容有限，所以用 print 直接打印，而 W3 版本的访问地址是一个 GitHub 仓库，所以需要遍历来获取想要的信息 |
| 文件怎么写 | 用 json 模块写入文件 | 用 json 模块写入文件 | 无差异 |
| 中文有没有转义 | 有 | 有 | 无差异 |
| 异常怎么处理 | 用 except 去捕获异常 | 用 except 去捕获异常 | 我重写的版本捕获了连接超时和连接失败两条具体异常，其余异常用 Exception；W3 版本直接用 exception 捕获所有异常 |

## 今天写的代码
- 文件名：day1_rebuild.py
```
import requests
import json
URL1 = "https://httpbin.org/get"
URL2 = "https://httpbin.org/status/404"
URL3 = "https://httpbin.org/status/500"
URL4 = "https://httpbin.org/status/300"
URL5 = "https://nonexistent-abcxyz.com"
URL6 = "https://github.com/LQ-GIF"
path = "output.json"

def main():
    URL_list = [URL1, URL2, URL3, URL4, URL5, URL6]
    for u in URL_list:
        try:
            response = requests.get(url=u, timeout=10)
            if response.status_code == 200:
                if u == URL1:
                    data = response.json()
                    print(data['headers']['User-Agent'])
                    with open(path, "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"{u} 连接正常, 状态码为： {response.status_code}")
                print(f"{u} 解析完成, 已保存到 {path} 文件中")
            elif response.status_code == 404:
                print(f"{u} 服务器不存在, 状态码为: {response.status_code}")
            elif response.status_code == 500:
                print(f"{u} 服务器出现问题, 状态码为: {response.status_code}")
            else:
                print(f"状态码: {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"{u} 请求超时, 请检查网络")
            continue
        except requests.exceptions.ConnectionError:
            print(f"{u} 连接失败, 请重试")
            continue
        except Exception as e:
            print(f"未知错误, 错误信息为: {e}")

if __name__ == "__main__":
    main()
```
## 遇到的问题
- 问题：再写异常捕获模块时，用的是 Python 内置的异常，而不是 requests 模块专用的异常捕获代码，但是程序运行正常，后来经过 AI 提醒才发现问题，原来是 Exception 帮我兜住了异常，但是这导致我写的特定异常捕获完全失效
    - 解决方法：将两处特定异常捕获代码全部改写为 requests 专用的异常捕获，最后再用 Excertion 捕获其他未知异常

- 问题：构想了一套通过追加模式记录全部返回状态码为 200 网址的响应内容并写入文件，被 AI 制止
    - 原因：通过追加模式多次写入文件的内容为多个独立的个体，而 JSON 文件支持写入的是一整块完整的个体，用多次追加的方式写入 JSON 文件，会破坏 JSON 文件的数据格式，从而导致文件损坏
    - 解决方法：想要写入多个内容，可以新建空列表，并将想要写入的内容加入到空列表中，最后再将收录完成的列表一次性写入文件中

## 没搞懂的地方
- 对于这部分内容中的 header 请求头和 params 查询参数的相关知识有点忘记了
- 对于调用返回的响应内容中的指定信息的方法有点生疏
- 对于 requests 模块的另一个功能 post 印象有点淡了

## 今天的收获
通过今天的学习，我发现对于 W3 这个阶段的知识掌握还远远不够，很多基础的功能和代码逻辑都忘了，所以今天的学习对于我来说是一次复习，让我发现了我再这个阶段知识的短板与不足，方便后续精准的进行查漏补缺