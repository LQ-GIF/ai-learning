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
                        print(f"{u} 解析完成, 已保存到 {path} 文件中")
                print(f"{u} 连接正常, 状态码为： {response.status_code}")
            elif response.status_code == 404:
                print(f"{u} 服务器不存在, 状态码为: {response.status_code}")
            elif response.status_code == 500:
                print(f"{u} 服务器出现问题, 状态码为: {response.status_code}")
            else:
                print(f"状态码: {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"{u} 请求超时, 请检查网络")
            continue
        except requests.exceptions.ConnectionError:
            print(f"{u} 连接失败, 请重试")
            continue
        except Exception as e:
            print(f"未知错误, 错误信息为: {e}")

if __name__ == "__main__":
    main()