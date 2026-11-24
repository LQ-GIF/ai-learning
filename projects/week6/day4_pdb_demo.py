
import requests

def request_json1(url, timeout=10):
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = request_json1("https://httpbin.org/get")
    print(data.keys())
    breakpoint()
    print("11111")