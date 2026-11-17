import requests

def fetch_json(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError :
        print(f"{url} 异常, 状态码为: {response.status_code}")
        return None
    except requests.exceptions.Timeout:
        print(f"{url} 连接超时, 请检查网络")
        return None
    except requests.exceptions.ConnectionError:
        print(f"{url} 连接失败, 请检查网络")
        return None
    except Exception as e:
        print(f"{url} 出现未知错误, 错误信息: {e}")
        return None


if __name__ == "__main__":
    url = "https://httpbin.org/get"
    a = fetch_json(url)
    print(a)