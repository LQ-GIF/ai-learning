# W6 Day1 对比分析：闭卷重写 vs W3原版

## 今天重写的版本
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
        except requests.exceptions.ConnectionError:
            print(f"{u} 连接失败, 请重试")
        except Exception as e:
            print(f"未知错误, 错误信息为: {e}")

if __name__ == "__main__":
    main()
```

## W3 原版
```
import requests
url = "https://api.github.com/users/torvalds/repos"
param = {
    "page": 1,
    "per_page": 10,
    "sort": "update"
}
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, params=param, headers=headers, timeout=10)

# 打印状态码
print("=" * 50)
print(f"状态码: {response.status_code}")

print("=" * 50)
print(f"响应头: {response.headers}")
print("=" * 50)

try:
    if response.status_code == 200:
        repos = response.json()
        print(f"获取到{len(repos)}个仓库")
        print("=" * 50)

        for i, repo in enumerate(repos, 1):
            print(f"【仓库{i}】")
            print(f"名称: {repo['name']}")
            print(f"描述: {repo['description']}")
            print(f"星数: {repo['stargazers_count']}")
            print(f"语言: {repo['language']}")
            print(f"最后更新:{repo['updated_at']}")
            print("-" * 50)

        # 额外练习：找出星数最多的仓库
        print("\n" + "=" * 50)
        print("星数最多的仓库:")
        most_starred = max(repos, key=lambda r: r['stargazers_count'])
        print(f"{most_starred['name']} - {most_starred['stargazers_count']}星")
        print("=" * 50)

        print("\n" + "=" * 50)
        print("按照星数从多到少给仓库排序")
        sorted_starred = sorted(repos, key=lambda r: r['stargazers_count'], reverse=True)
        for j, ssed in enumerate(sorted_starred, 1):
            print(f"【仓库{j}】")
            print(f"名称: {ssed['name']}")
            print(f"描述: {ssed['description']}")
            print(f"星数: {ssed['stargazers_count']}")
            print(f"语言: {ssed['language']}")
            print(f"最后更新:{ssed['updated_at']}")
            print("-" * 50)
    else:
        print(f"请求失败, 状态码: {response.status_code}")
        print("信息错误")
        print(response.text)
except Exception as e:
    print(f"未知错误: {e}")
```

## 我写出来的脚本做了什么
- 请求了文件中 URL 1-6 的所有地址，分别返回了状态码 200，300，404，500，还有两个连接失败的异常被捕获
- 解析了状态码 200 网址返回的请求内容，并用 with 写入 output.json 文件中

## 和 W3 版本逐项对比
| 项目 | 我盲写的写法 | W3 当时的写法 | 差异说明 |
|---|---|---|---|
| 请求方式 | requests.get(url, timeout) | requests.get(url, params, header, timeout) | 我重写的请求只有网址和超时，W3 的请求在我重写版的基础上还添加了 params 查询参数和 header 请求头 |
| 有没有设 timeout | 有 | 有 | 超时限制都是 10 s 无差异 |
| 状态码怎么判断 | try + if 来判断返回的状态码，并捕获其他异常 | try + if 来判断返回的状态码，并捕获其他异常 | 我重写的状态码判断对每个类型的状态码都有独立的判断分支，W3 的状态码判断只对状态码 200 进行判断，其他状态码一律按请求失败处理 |
| JSON 怎么解析 | 用打印命令`print(data['headers']['User-Agent'])`直接输出 | 将返回的响应内容通过遍历获取想要的信息 | 由于访问地址的不同，我重写的版本返回的响应内容有限，所以用 print 直接打印，而 W3 版本的访问地址是一个 GitHub 仓库，所以需要遍历来获取想要的信息 |
| 文件怎么写 | 用 json 模块写入文件 | 用 json 模块写入文件 | 无差异 |
| 中文有没有转义 | 有 | 有 | 无差异 |
| 异常怎么处理 | 用 except 去捕获异常 | 用 except 去捕获异常 | 我重写的版本捕获了连接超时和连接失败两条具体异常，其余异常用 Exception；W3 版本直接用 exception 捕获所有异常 |

## 今天忘掉 / 写错的地方
- 忘记的：
    - requests 模块的 get 要传入的参数只记得一个网址 url 其他的 header 请求头，params 查询参数，timeout 超时限制的用法都忘记了
    - 返回的响应内容的 JSON 解析，以及获取其中信息的方法都忘记了
    - 返回请求网址的状态码的方法忘记了
    
- 写错的：
    - 问题：捕获特定异常的命令写错了
        - 原因：捕获异常时用了 Python 内置的异常，但是 requests 模块有专用的异常捕获代码，出现问题时，Python 的内置异常根本捕获不到，全由 Exception 进行兜底
        - 解决方法：将内置异常改为 requests 模块专用的异常
    - 问题：连用 3 个 if 语句，却没写 else 进行兜底，导致漏掉了状态码 300 
        - 原因：连用 3 给 if 语句来判断状态码，却应为没有 else 兜底，漏掉了状态码 300
        - 解决方法：用 if + elif + else 来判断状态码
    - 问题：常量应该写在文件开头，我重写的第一版常量却分散在文件中的各个地方
        - 解决方法：将所有常量集中起来放置再文件开头
    - 问题：path 写死为绝对路径，没有考虑到其他人的文件夹结构和我的不一样，拷贝下来直接运行会导致程序崩溃
        - 解决方法：将 path 的路径改为相对路径
    - 问题：没有先判断状态码再解析数据，如果状态码不是 200，会导致解析出现错误
        - 解决方法：在解析代码前写一条 if 判断语句来判断状态码是否为 200
    - 问题：我用了 6 个 URL 地址，for 循环遍历测试每个地址的请求状态，却没在最后的结果中输出对应的网址，导致我根本分不清每个网址是什么状态
        - 解决方法：在输出的结果中写明对应的网址
    - 问题：一次请求只会出现一种异常状态，捕获该异常后就可以用 continue 直接跳过这一轮，进入下一轮遍历去测试新网址，而我的重写版再捕获异常后会继续往下运行，去判断其他异常，属于无效判断
        - 在每个异常判断后加 continue，捕获到第一个异常后立刻进入下一轮去测试新的网址
    - 问题：我想用 json 模块中的 "a" 追加模式去进行文件写入，但是 JSON 文件中的内容是一整块完整对象，而用 "a" 追加模式写入的是多个的对象，这样的多对象内容会破坏 JSON 的文件格式，导致 JSON 文件损坏
        - 解决方法：先用列表收集所有的返回内容，收集完成后再一次性写入文件

## 今天比 W3 做得更好的地方
今天的重写版对每个状态码都建立了对应的判断分支，还写了两个特定的异常捕获

## 我对 W3 的掌握情况
- 完全记得、抬手就写：3 项
    - import requests
    - with open 写入文件
    - get 请求中 url 的用法
- 模糊、要查一下：5 项
    - timeout 的用法
    - header 请求头，params 查询参数的用法
    - response.status_code 状态码获取方法
    - response.json 解析响应内容的方法
    - requests 模块专用的异常捕获命令
- 完全忘了、当新知识学：1 项
    - post 请求