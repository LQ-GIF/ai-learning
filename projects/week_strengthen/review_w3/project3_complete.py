import requests

def request_json(method, url, timeout=10, **kwargs):
    if method.upper() not in ("GET", "POST"):
        raise ValueError(f"不支持请求方法: {method}, 仅支持 GET/POST")
    try:
        if method.upper() == "GET":
            response = requests.get(url, timeout=timeout, **kwargs)
        else:
            response = requests.post(url, timeout=timeout, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print(f"{url} 连接失败, 请检查网络")
        return None
    except requests.exceptions.Timeout:
        print(f"{url} 连接超时, 请检查网络后重试")
        return None
    except requests.exceptions.HTTPError:
        print(f"{url} 连接异常, 状态码为 {response.status_code}")
        return None
    except requests.exceptions.JSONDecodeError:
        print(f"{url} 返回的的内容不是 JSON, 状态码为 {response.status_code}, 请核对该地址返回的内容是否为 JSON 格式")
        return None
    except Exception as e:
        print(f"{url} 出现未知错误, 错误信息: {e}")
        return None


if __name__ == "__main__":
    print(">>> 这是新版 project3_complete")
    URLS = [
        "https://httpbin.org/get",
        "https://httpbin.org/status/404",
        "https://httpbin.org/status/500",
        "https://httpbin.org/status/300",
        "https://nonexistent-abcxyz.com",
        "https://httpbin.org/delay/3",
    ]

    for u in URLS:
        print(f"\n>>> {u}")
        data = request_json("GET", u, timeout=5)
        if data is None:
            print("    [返回 None —— 调用方应该跳过写文件]")
        else:
            print(f"    [拿到数据，请求头为：{list(data.keys())[:4]}]")

