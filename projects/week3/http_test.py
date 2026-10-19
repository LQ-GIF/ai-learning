# 导入 requests 库
import requests

# 定义要调用的 API 地址
# 这是 GitHub 的公开 API，获取用户 torvalds（Linux 创始人）的信息
url = "https://api.github.com/users/torvalds"

# 发送 GET 请求
# headers 里设置 User-Agent，告诉 GitHub 是谁在调用
# 不设置的话 GitHub 可能会拒绝请求（返回 403）
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# 打印状态码
# 200 表示成功，404 表示找不到，500 表示服务器出错
print("=" * 50)
print("状态码: ", response.status_code)

# 打印响应头
# 响应头是服务器返回的附加信息，比如内容类型、日期、服务器类型等
print("=" * 50)
print("响应头: ")
for key, value in response.headers.items():
    print(f"  {key}: {value}")

try:
    if response.status_code == 200:
        # 打印响应内容（JSON 格式）
        print("=" * 50)
        print("响应内容(JSON): ")
        print(response.text)

        # 把 JSON 解析成 Python 字典，提取关键信息
        print("=" * 50)
        print("用户信息提取: ")
        data = response.json()
        print(data)

        print(f"  用户名: {data['login']}")
        print(f"  姓名: {data['name']}")
        print(f"  公司: {data['company']}")
        print(f"  博客: {data['blog']}")
        print(f"  公开仓库数: {data['public_repos']}")
        print(f"  粉丝数: {data['followers']}")
        print("=" * 50)
    else:
        print(f"请求失败, 状态码{response.status_code}")
        print(f"错误信息")
        print(response.text)
except Exception as e:
    print(f"失败原因: {e}")


print("\n" + "=" * 50)
print("测试不同状态码:")
print("=" * 50)

# 测试1：正常的用户（应该返回 200）
response1 = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
print(f"访问存在的用户 torvalds --> 状态码: {response1.status_code}(200=访问成功)")

# 测试2：不存在的用户（应该返回 404）
url1 = "https://api.github.com/users/this_done_not_exist_12345"
response2 = requests.get(url1, headers={"User-Agent": "Mozilla/5.0"})
print(f"访问不存在的用户 --> 状态码: {response2.status_code}(404=找不到)")

# 测试3：用 httpbin 测试各种状态码
# httpbin 是一个专门用来测试 HTTP 请求的网站
url2 = "https://httpbin.org/status/500"
response3 = requests.get(url2, headers={"User-Agent": "Mozilla/5.0"})
print(f"访问 httpbin.org/status/500 --> 状态码: {response3.status_code}(500=服务器出错)")

url3 = "https://httpbin.org/status/403"
response4 = requests.get(url3, headers={"User-Agent": "Mozilla/5.0"})
print(f"访问 httpbin.org/status/403 --> 状态码: {response4.status_code}(403=禁止访问)")

url4 = "https://httpbin.org/status/300"
response5 = requests.get(url4, headers={"User-Agent": "Mozilla/5.0"})
print(f"访问 httpbin.org/status/300 --> 状态码: {response5.status_code}")

print("=" * 50)
print("状态码总结:")
print("  2xx (200) --> 成功, 请求正常处理")
print("  3xx (300) --> 重定向, 地址变了")
print("  4xx (400/401/403/404) --> 客户端出错, 请求有问题")
print("  5xx (500) --> 服务器错误, 对方服务器出问题了")

