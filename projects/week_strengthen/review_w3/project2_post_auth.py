import requests

URL = "https://httpbin.org/post"
DATA = {
    "name": "张三",
    "city": "杭州"
    }
HEADERS = {
    "Authorization": "Bearer my_token_123",
    "User-Agent": "LQ-GiF-Review-W3"
}
types1 = "json"
types2 = "data"

def post_check(data_type, url, data, headers, timeout=10):
    data_type = data_type.upper()
    try:
        if data_type == "JSON":
            response = requests.post(url, json=data, headers=headers, timeout=timeout)
        elif data_type == "DATA":
            response = requests.post(url, data=data, headers=headers, timeout=timeout)
        else:
            print(f"期望数据格式不在可传输范围内")
            return None
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


def main():
    post_data_json = post_check(data_type=types1, url=URL, data=DATA, headers=HEADERS)
    if post_data_json is None:
        print("内容获取失败, 跳过解析")
    else:
        print(post_data_json['json'])
        print(post_data_json['headers']['Authorization'])

    
    post_data = post_check(data_type=types2, url=URL, data=DATA, headers=HEADERS)
    if post_data is None:
        print("内容获取失败, 跳过解析")
    else:
        print(post_data['form'])
        print(post_data['headers']['Authorization'])


if __name__ == "__main__":
    main()