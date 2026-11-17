import json
from api_utils_2 import fetch_json

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
        data = fetch_json(u)
        if data == None:
            continue
        else:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"{u} 解析完成, 已保存到 {path} ")

if __name__ == "__main__":
    main()