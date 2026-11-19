import requests
import json

URL = "https://httpbin.org/get"
params = {
    "keyword": "图书馆",
    "city": "杭州",
    "page": 1
}
headers = {"User-Agent": "LQ-GiF-Review-W3"}
path = "params_result.json"

def get_check(url, param, header, timeout=10):
    try:
        response = requests.get(url, params=param, headers=header, timeout=timeout)
        response.raise_for_status()      # 查
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
    data = get_check(url=URL, param=params, header=headers)
    if data is None:
        print("内容获取失败, 跳过解析")
    else:
        print(data['args'])
        print(data["headers"]["User-Agent"])
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()