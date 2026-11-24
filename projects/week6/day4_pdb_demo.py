
import requests

def request_json(url, timeout=10):
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    # return response.json      # 错误写法：返回绑定方法，后续 .keys() 报 AttributeError
    return response.json()      # 正确写法：返回解析后的 dict


if __name__ == "__main__":
    data = request_json("https://httpbin.org/get")
    breakpoint()
    print(data.keys())