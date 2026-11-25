import requests

def call_API(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        print(f"{url} 连接异常, 状态码: {response.status_code}")
        return None
    except requests.exceptions.ConnectionError:
        print(f"{url} 连接失败, 请检查网络")
        return None
    except requests.exceptions.Timeout:
        print(f"{url} 连接超时, 请刷新网络或稍后重试")
        return None
    except requests.exceptions.JSONDecodeError:
        print(f"{url} 返回内容为非 JSON 格式, 状态码为 {response.status_code}, 请检查网址是否正确")
        return None
    except Exception as e:
        print(f"{url} 出现未知错误, 错误信息为: {e}")


if __name__ =="__main__":
    URL = [
        "https://httpbin.org/get",
        "https://httpbin.org/status/404",
        "https://nonexistent-abcxyz.com",
        "https://httpbin.org/delay/6",
        "https://httpbin.org/status/300"
    ]
    for u in URL:
        data = call_API(u, timeout=3)
        if data is None:
            print("调用 API 失败, 停止解析")
        else:
            print("解析成功")
            print(data['headers']['User-Agent'])