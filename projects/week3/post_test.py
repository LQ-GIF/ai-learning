import requests
url = "https://httpbin.org/post"

data = {
    "name": "流水别墅",
    "architect": "弗兰克·劳埃德·赖特",
    "year": 1935,
    "location": "美国宾夕法尼亚州",
    "style": "有机建筑",
    "tags": ["有机建筑", "现代主义", "别墅"]
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

print("=" * 50)
print("发送 POST 请求...")
print(f"URL: {url}")
print(f"发送的数据: {data}")
print("=" * 50)

try:
    response = requests.post(url, json=data, headers=headers, timeout=10)

    print(f"\n状态码: {response.status_code}")

    if response.status_code == 200:
        result = response.json()
        print("\n" + "=" * 50)
        print("服务器返回的完整 JSON: ")
        print(response.text)

        print("\n" + "=" * 50)
        print("提取关键信息:")
        print(f"  你发送的 JSON 数据: {result['json']}")
        print(f"  你发送的 URL: {result['url']}")
        print(f"  你的 IP 地址: {result['origin']}")
        print(f"  你发送的 Content-Type: {result['headers']['Content-Type']}")
        print("=" * 50)

        if result['json'] == data:
            print("\n✅ 验证成功！服务器收到的数据和你发送的完全一致！")
        else:
            print("\n❌ 验证失败！服务器收到的数据和你发送的不一致。")
    else:
        print(f"\n请求错误, 状态码{response.status_code}")
        print("错误信息: ")
        print(response.text)
except requests.exceptions.Timeout:
    print("\n❌ 请求超时！网络不好或者服务器太慢，请检查网络后重试。")
except requests.exceptions.ConnectionError:
    print("\n❌ 连接失败！请检查网络连接。")
except Exception as e:
    print(f"\n❌ 发生未知错误: {e}")


print("\n\n" + "=" * 50)
print("对比: GET 请求（参数在 URL 上）")
print("=" * 50)

get_url = "https://httpbin.org/get"
get_params = {"name": "张三", "age": 23, "city": "杭州"}
get_headers = {"User-Agent": "Mozilla/5.0"}

get_response = requests.get(get_url, params=get_params, headers=get_headers, timeout=10)
get_result = get_response.json()

print(f"GET 请求的 URL: {get_result['url']}")
print(f"  → 你看，参数 name 和 age 都显示在 URL 上了！")
print(f"GET 请求的参数: {get_result['args']}")

print("\n" + "=" * 50)
print("GET vs POST 总结:")
print("  GET: 参数在 URL 上，适合获取数据，不安全（不能发密码）")
print("  POST: 参数在请求体里，适合提交数据，相对安全（可以发密码）")
print("=" * 50)
